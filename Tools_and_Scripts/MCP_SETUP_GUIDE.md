# MCP Bridge Setup Guide

This document covers how both MCP connections (Unreal Engine and Blender) are configured so they can be restored if something breaks.

---

## Prerequisites

- **Python 3.13+** with `mcp` package installed
  ```
  pip install mcp
  ```
- **uv** installed (for Blender MCP)
  - Location: `C:\Users\kyler\.local\bin\uv.exe`
  - `uvx` is used to run the `blender-mcp` package without installing it globally
- **Blender 5.1** with the BlenderMCP addon installed
- **Unreal Engine 5.7** with the UnrealMCP plugin enabled

---

## 1. Unreal Engine MCP

### How it works

```
Claude Code  --stdio-->  unreal_mcp_bridge.py  --TCP:55557-->  UE5.7 UnrealMCP Plugin
```

Claude Code spawns `unreal_mcp_bridge.py` as a stdio MCP server. The bridge translates MCP tool calls into TCP messages sent to the UnrealMCP plugin running inside the UE5.7 editor on `127.0.0.1:55557`.

### Configuration

**Scope:** Project-level (shared via `.mcp.json` in repo root)

**Config file:** `<project_root>/.mcp.json`
```json
{
  "mcpServers": {
    "unreal-mcp": {
      "type": "stdio",
      "command": "python",
      "args": [
        "Tools_and_Scripts/unreal_mcp_bridge.py",
        "stdio"
      ],
      "env": {}
    }
  }
}
```

**Bridge script:** `Tools_and_Scripts/unreal_mcp_bridge.py`

### Setup steps (if broken)

1. **Make sure the UnrealMCP plugin is enabled in UE5.7**
   - Open UE5.7 editor
   - Go to Edit > Plugins
   - Search for "UnrealMCP" and ensure it's enabled
   - Restart editor if you just enabled it

2. **Verify the plugin is listening on port 55557**
   - The plugin starts a TCP server on `127.0.0.1:55557` when the editor opens
   - You can test with: `python -c "import socket; s=socket.socket(); s.connect(('127.0.0.1', 55557)); print('connected'); s.close()"`

3. **Verify `.mcp.json` exists in the project root** with the config shown above

4. **Verify the `mcp` Python package is installed**
   ```
   pip install mcp
   ```

5. **Restart Claude Code** so it picks up the `.mcp.json` config

6. **Test the connection** by asking Claude to run `ping` on the unreal-mcp

### Troubleshooting

| Problem | Fix |
|---|---|
| "No response from Unreal Engine" | UE5.7 editor is not running, or UnrealMCP plugin is not enabled |
| Bridge script crashes on startup | `mcp` Python package not installed — run `pip install mcp` |
| Tools don't appear in Claude Code | `.mcp.json` is missing or malformed — check the file and restart Claude Code |
| Connection timeout | Check if another process is using port 55557. Restart UE5.7 editor. |

### CLI commands

```bash
# Check status
claude mcp list

# Re-add if removed (run from project root)
claude mcp add unreal-mcp -s project -- python Tools_and_Scripts/unreal_mcp_bridge.py stdio

# Remove
claude mcp remove unreal-mcp -s project
```

---

## 2. Blender MCP

### How it works

```
Claude Code  --stdio-->  uvx blender-mcp  --TCP:9876-->  Blender Addon (BlenderMCP)
```

Claude Code runs `uvx blender-mcp` which starts the MCP server. That server connects to the BlenderMCP addon running inside Blender, which listens on `localhost:9876`.

### Configuration

**Scope:** Local (private to your machine, not in repo — stored in Claude Code local settings)

**Added via CLI:**
```bash
claude mcp add blender-mcp -s local -- uvx blender-mcp
```

### Blender addon location

```
%APPDATA%\Blender Foundation\Blender\5.1\scripts\addons\addon.py
```

This is the BlenderMCP addon (by Siddharth Ahuja). It runs a TCP server on `localhost:9876` inside Blender.

### Setup steps (if broken)

1. **Make sure the BlenderMCP addon is installed in Blender**
   - Open Blender 5.1
   - Go to Edit > Preferences > Add-ons
   - Search for "Blender MCP" — it should be listed and enabled
   - If not installed: download from the BlenderMCP GitHub repo and install via "Install from Disk"

2. **Start the MCP server inside Blender**
   - In the 3D Viewport, open the sidebar (press `N`)
   - Find the "BlenderMCP" tab
   - Click "Start MCP Server"
   - You should see "Server started on localhost:9876" in the panel

3. **Verify the `blender-mcp` Claude Code server is registered**
   ```bash
   claude mcp list
   ```
   If `blender-mcp` is missing, re-add it:
   ```bash
   claude mcp add blender-mcp -s local -- uvx blender-mcp
   ```

4. **Restart Claude Code** to pick up the MCP config

5. **Test the connection** by asking Claude to run `get_scene_info`

### Troubleshooting

| Problem | Fix |
|---|---|
| blender-mcp tools not appearing | Run `claude mcp add blender-mcp -s local -- uvx blender-mcp` and restart Claude Code |
| "Connection refused" errors | The BlenderMCP server isn't running inside Blender — open sidebar > BlenderMCP tab > Start MCP Server |
| `uvx` not found | Install uv: `pip install uv` or `winget install astral-sh.uv` |
| Blender addon not visible | Ensure `addon.py` exists at `%APPDATA%\Blender Foundation\Blender\5.1\scripts\addons\addon.py` |
| Port conflict on 9876 | Another Blender instance may be running. Close other instances and restart. |

### CLI commands

```bash
# Check status
claude mcp list

# Add (local scope — not shared with repo)
claude mcp add blender-mcp -s local -- uvx blender-mcp

# Remove
claude mcp remove blender-mcp -s local
```

---

## Startup Checklist (Both MCPs)

1. Open **Blender 5.1** > Sidebar > BlenderMCP > **Start MCP Server**
2. Open **UE5.7 editor** (UnrealMCP plugin starts automatically)
3. Open **Claude Code** in the ShatteredDominion project directory
4. Verify with `claude mcp list` — both should show "Connected"

If either shows disconnected, follow the troubleshooting steps for that MCP above.

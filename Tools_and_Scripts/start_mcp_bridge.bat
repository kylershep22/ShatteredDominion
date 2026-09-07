@echo off
title Unreal MCP Bridge (SSE on port 8100)
echo Starting Unreal MCP Bridge on http://127.0.0.1:8100/sse ...
echo Keep this window open while using Claude Code.
echo.
python "%~dp0unreal_mcp_bridge.py"
pause

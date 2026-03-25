"""
MCP Bridge for UnrealMCP Plugin
Translates Claude Code MCP tool calls into TCP messages
for the UnrealMCP plugin running inside UE5.7 editor on port 55557.
"""

import json
import socket
from mcp.server.fastmcp import FastMCP

UE_HOST = "127.0.0.1"
UE_PORT = 55557
TIMEOUT = 10

mcp = FastMCP("unreal-engine")


def send_command(cmd_type: str, params: dict | None = None) -> dict:
    """Send a command to the UnrealMCP TCP server and return the parsed response."""
    msg = json.dumps({"type": cmd_type, "params": params or {}}) + "\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        s.connect((UE_HOST, UE_PORT))
        s.sendall(msg.encode("utf-8"))
        # Read until we get a complete JSON response
        buf = b""
        while True:
            chunk = s.recv(8192)
            if not chunk:
                break
            buf += chunk
            # Try to parse - if valid JSON, we're done
            try:
                result = json.loads(buf.decode("utf-8"))
                return result
            except json.JSONDecodeError:
                continue
    return {"status": "error", "error": "No response from Unreal Engine"}


# ── Editor Commands ──────────────────────────────────────────────

@mcp.tool()
def ping() -> str:
    """Ping the Unreal Engine editor to verify the connection is alive."""
    return json.dumps(send_command("ping"))


@mcp.tool()
def get_actors_in_level() -> str:
    """Get a list of all actors currently in the active level."""
    return json.dumps(send_command("get_actors_in_level"))


@mcp.tool()
def find_actors_by_name(pattern: str) -> str:
    """Find actors in the level whose name contains the given pattern.

    Args:
        pattern: Substring to search for in actor names
    """
    return json.dumps(send_command("find_actors_by_name", {"pattern": pattern}))


@mcp.tool()
def spawn_actor(
    type: str,
    name: str,
    location_x: float = 0, location_y: float = 0, location_z: float = 0,
    rotation_pitch: float = 0, rotation_yaw: float = 0, rotation_roll: float = 0,
    scale_x: float = 1, scale_y: float = 1, scale_z: float = 1,
) -> str:
    """Spawn a new actor in the level.

    Args:
        type: Actor class type (StaticMeshActor, PointLight, SpotLight, DirectionalLight, CameraActor)
        name: Unique name for the actor
        location_x: X position
        location_y: Y position
        location_z: Z position
        rotation_pitch: Pitch rotation in degrees
        rotation_yaw: Yaw rotation in degrees
        rotation_roll: Roll rotation in degrees
        scale_x: X scale
        scale_y: Y scale
        scale_z: Z scale
    """
    params = {
        "type": type,
        "name": name,
        "location": {"x": location_x, "y": location_y, "z": location_z},
        "rotation": {"pitch": rotation_pitch, "yaw": rotation_yaw, "roll": rotation_roll},
        "scale": {"x": scale_x, "y": scale_y, "z": scale_z},
    }
    return json.dumps(send_command("spawn_actor", params))


@mcp.tool()
def delete_actor(name: str) -> str:
    """Delete an actor from the level by name.

    Args:
        name: The exact name of the actor to delete
    """
    return json.dumps(send_command("delete_actor", {"name": name}))


@mcp.tool()
def set_actor_transform(
    name: str,
    location_x: float | None = None, location_y: float | None = None, location_z: float | None = None,
    rotation_pitch: float | None = None, rotation_yaw: float | None = None, rotation_roll: float | None = None,
    scale_x: float | None = None, scale_y: float | None = None, scale_z: float | None = None,
) -> str:
    """Set the transform (location, rotation, scale) of an actor.

    Args:
        name: The exact name of the actor
        location_x: X position (optional)
        location_y: Y position (optional)
        location_z: Z position (optional)
        rotation_pitch: Pitch in degrees (optional)
        rotation_yaw: Yaw in degrees (optional)
        rotation_roll: Roll in degrees (optional)
        scale_x: X scale (optional)
        scale_y: Y scale (optional)
        scale_z: Z scale (optional)
    """
    params: dict = {"name": name}
    if any(v is not None for v in (location_x, location_y, location_z)):
        params["location"] = {"x": location_x or 0, "y": location_y or 0, "z": location_z or 0}
    if any(v is not None for v in (rotation_pitch, rotation_yaw, rotation_roll)):
        params["rotation"] = {"pitch": rotation_pitch or 0, "yaw": rotation_yaw or 0, "roll": rotation_roll or 0}
    if any(v is not None for v in (scale_x, scale_y, scale_z)):
        params["scale"] = {"x": scale_x or 1, "y": scale_y or 1, "z": scale_z or 1}
    return json.dumps(send_command("set_actor_transform", params))


@mcp.tool()
def get_actor_properties(name: str) -> str:
    """Get detailed properties of an actor by name.

    Args:
        name: The exact name of the actor
    """
    return json.dumps(send_command("get_actor_properties", {"name": name}))


@mcp.tool()
def set_actor_property(name: str, property_name: str, property_value: str) -> str:
    """Set a property on an actor.

    Args:
        name: The exact name of the actor
        property_name: The property to set
        property_value: The value to set (as JSON string for complex values)
    """
    # Try to parse as JSON for complex values, fall back to string
    try:
        parsed = json.loads(property_value)
    except (json.JSONDecodeError, TypeError):
        parsed = property_value
    return json.dumps(send_command("set_actor_property", {
        "name": name, "property_name": property_name, "property_value": parsed
    }))


@mcp.tool()
def spawn_blueprint_actor(
    blueprint_name: str,
    actor_name: str,
    location_x: float = 0, location_y: float = 0, location_z: float = 0,
    rotation_pitch: float = 0, rotation_yaw: float = 0, rotation_roll: float = 0,
    scale_x: float = 1, scale_y: float = 1, scale_z: float = 1,
) -> str:
    """Spawn an instance of a Blueprint actor in the level.

    Args:
        blueprint_name: Name of the Blueprint asset (must be under /Game/Blueprints/)
        actor_name: Unique name for the spawned actor
        location_x: X position
        location_y: Y position
        location_z: Z position
        rotation_pitch: Pitch rotation in degrees
        rotation_yaw: Yaw rotation in degrees
        rotation_roll: Roll rotation in degrees
        scale_x: X scale
        scale_y: Y scale
        scale_z: Z scale
    """
    params = {
        "blueprint_name": blueprint_name,
        "actor_name": actor_name,
        "location": {"x": location_x, "y": location_y, "z": location_z},
        "rotation": {"pitch": rotation_pitch, "yaw": rotation_yaw, "roll": rotation_roll},
        "scale": {"x": scale_x, "y": scale_y, "z": scale_z},
    }
    return json.dumps(send_command("spawn_blueprint_actor", params))


@mcp.tool()
def focus_viewport(
    target: str | None = None,
    location_x: float | None = None, location_y: float | None = None, location_z: float | None = None,
    distance: float = 1000,
    orientation_pitch: float | None = None, orientation_yaw: float | None = None, orientation_roll: float | None = None,
) -> str:
    """Focus the editor viewport on an actor or location.

    Args:
        target: Actor name to focus on (optional, use this OR location)
        location_x: X position to focus on (optional)
        location_y: Y position to focus on (optional)
        location_z: Z position to focus on (optional)
        distance: Camera distance from target
        orientation_pitch: Camera pitch (optional)
        orientation_yaw: Camera yaw (optional)
        orientation_roll: Camera roll (optional)
    """
    params: dict = {"distance": distance}
    if target:
        params["target"] = target
    if any(v is not None for v in (location_x, location_y, location_z)):
        params["location"] = {"x": location_x or 0, "y": location_y or 0, "z": location_z or 0}
    if any(v is not None for v in (orientation_pitch, orientation_yaw, orientation_roll)):
        params["orientation"] = {"pitch": orientation_pitch or 0, "yaw": orientation_yaw or 0, "roll": orientation_roll or 0}
    return json.dumps(send_command("focus_viewport", params))


@mcp.tool()
def take_screenshot(filepath: str) -> str:
    """Take a screenshot of the active editor viewport.

    Args:
        filepath: File path to save the screenshot (.png extension added if missing)
    """
    return json.dumps(send_command("take_screenshot", {"filepath": filepath}))


# ── Blueprint Commands ───────────────────────────────────────────

@mcp.tool()
def create_blueprint(name: str, parent_class: str = "Actor") -> str:
    """Create a new Blueprint asset.

    Args:
        name: Name for the new Blueprint
        parent_class: Parent class (default: Actor)
    """
    return json.dumps(send_command("create_blueprint", {"name": name, "parent_class": parent_class}))


@mcp.tool()
def add_component_to_blueprint(blueprint_name: str, component_type: str, component_name: str) -> str:
    """Add a component to a Blueprint.

    Args:
        blueprint_name: Name of the target Blueprint
        component_type: Type of component to add (e.g. StaticMeshComponent, BoxComponent)
        component_name: Name for the new component
    """
    return json.dumps(send_command("add_component_to_blueprint", {
        "blueprint_name": blueprint_name, "component_type": component_type, "component_name": component_name
    }))


@mcp.tool()
def set_component_property(blueprint_name: str, component_name: str, property_name: str, property_value: str) -> str:
    """Set a property on a Blueprint component.

    Args:
        blueprint_name: Name of the Blueprint
        component_name: Name of the component
        property_name: Property to set
        property_value: Value to set (JSON string for complex values)
    """
    try:
        parsed = json.loads(property_value)
    except (json.JSONDecodeError, TypeError):
        parsed = property_value
    return json.dumps(send_command("set_component_property", {
        "blueprint_name": blueprint_name, "component_name": component_name,
        "property_name": property_name, "property_value": parsed
    }))


@mcp.tool()
def set_physics_properties(blueprint_name: str, component_name: str, simulate_physics: bool = True, gravity_enabled: bool = True) -> str:
    """Set physics properties on a Blueprint component.

    Args:
        blueprint_name: Name of the Blueprint
        component_name: Name of the component
        simulate_physics: Whether to simulate physics
        gravity_enabled: Whether gravity is enabled
    """
    return json.dumps(send_command("set_physics_properties", {
        "blueprint_name": blueprint_name, "component_name": component_name,
        "simulate_physics": simulate_physics, "gravity_enabled": gravity_enabled
    }))


@mcp.tool()
def compile_blueprint(blueprint_name: str) -> str:
    """Compile a Blueprint.

    Args:
        blueprint_name: Name of the Blueprint to compile
    """
    return json.dumps(send_command("compile_blueprint", {"blueprint_name": blueprint_name}))


@mcp.tool()
def set_blueprint_property(blueprint_name: str, property_name: str, property_value: str) -> str:
    """Set a property on a Blueprint's default object.

    Args:
        blueprint_name: Name of the Blueprint
        property_name: Property to set
        property_value: Value to set (JSON string for complex values)
    """
    try:
        parsed = json.loads(property_value)
    except (json.JSONDecodeError, TypeError):
        parsed = property_value
    return json.dumps(send_command("set_blueprint_property", {
        "blueprint_name": blueprint_name, "property_name": property_name, "property_value": parsed
    }))


@mcp.tool()
def set_static_mesh_properties(blueprint_name: str, component_name: str, mesh_path: str) -> str:
    """Set the static mesh on a Blueprint's mesh component.

    Args:
        blueprint_name: Name of the Blueprint
        component_name: Name of the static mesh component
        mesh_path: Asset path to the static mesh
    """
    return json.dumps(send_command("set_static_mesh_properties", {
        "blueprint_name": blueprint_name, "component_name": component_name, "mesh_path": mesh_path
    }))


@mcp.tool()
def set_pawn_properties(blueprint_name: str, auto_possess_player: str = "Player0") -> str:
    """Set pawn-specific properties on a Blueprint.

    Args:
        blueprint_name: Name of the Blueprint
        auto_possess_player: Which player to auto-possess (e.g. Player0)
    """
    return json.dumps(send_command("set_pawn_properties", {
        "blueprint_name": blueprint_name, "auto_possess_player": auto_possess_player
    }))


# ── Blueprint Node Commands ──────────────────────────────────────

@mcp.tool()
def add_blueprint_event_node(blueprint_name: str, event_name: str) -> str:
    """Add an event node to a Blueprint's event graph.

    Args:
        blueprint_name: Name of the Blueprint
        event_name: Name of the event (e.g. BeginPlay, Tick)
    """
    return json.dumps(send_command("add_blueprint_event_node", {
        "blueprint_name": blueprint_name, "event_name": event_name
    }))


@mcp.tool()
def add_blueprint_function_node(blueprint_name: str, function_name: str, target: str = "") -> str:
    """Add a function call node to a Blueprint's event graph.

    Args:
        blueprint_name: Name of the Blueprint
        function_name: Name of the function to call
        target: Optional target class for the function
    """
    params = {"blueprint_name": blueprint_name, "function_name": function_name}
    if target:
        params["target"] = target
    return json.dumps(send_command("add_blueprint_function_node", params))


@mcp.tool()
def add_blueprint_input_action_node(blueprint_name: str, action_name: str) -> str:
    """Add an input action node to a Blueprint's event graph.

    Args:
        blueprint_name: Name of the Blueprint
        action_name: Name of the input action
    """
    return json.dumps(send_command("add_blueprint_input_action_node", {
        "blueprint_name": blueprint_name, "action_name": action_name
    }))


@mcp.tool()
def add_blueprint_variable(blueprint_name: str, variable_name: str, variable_type: str, default_value: str = "") -> str:
    """Add a variable to a Blueprint.

    Args:
        blueprint_name: Name of the Blueprint
        variable_name: Name for the new variable
        variable_type: Type of the variable (e.g. Float, Integer, Boolean, Vector, String)
        default_value: Optional default value
    """
    params = {"blueprint_name": blueprint_name, "variable_name": variable_name, "variable_type": variable_type}
    if default_value:
        params["default_value"] = default_value
    return json.dumps(send_command("add_blueprint_variable", params))


@mcp.tool()
def connect_blueprint_nodes(blueprint_name: str, source_node: str, source_pin: str, target_node: str, target_pin: str) -> str:
    """Connect two nodes in a Blueprint's event graph.

    Args:
        blueprint_name: Name of the Blueprint
        source_node: Name/ID of the source node
        source_pin: Name of the output pin on the source node
        target_node: Name/ID of the target node
        target_pin: Name of the input pin on the target node
    """
    return json.dumps(send_command("connect_blueprint_nodes", {
        "blueprint_name": blueprint_name, "source_node": source_node, "source_pin": source_pin,
        "target_node": target_node, "target_pin": target_pin
    }))


@mcp.tool()
def find_blueprint_nodes(blueprint_name: str, node_type: str = "") -> str:
    """Find nodes in a Blueprint's event graph.

    Args:
        blueprint_name: Name of the Blueprint
        node_type: Optional filter by node type
    """
    params = {"blueprint_name": blueprint_name}
    if node_type:
        params["node_type"] = node_type
    return json.dumps(send_command("find_blueprint_nodes", params))


@mcp.tool()
def add_blueprint_get_component_node(blueprint_name: str, component_name: str) -> str:
    """Add a GetComponent reference node to a Blueprint's event graph.

    Args:
        blueprint_name: Name of the Blueprint
        component_name: Name of the component to reference
    """
    return json.dumps(send_command("add_blueprint_get_component_node", {
        "blueprint_name": blueprint_name, "component_name": component_name
    }))


@mcp.tool()
def add_blueprint_self_reference(blueprint_name: str) -> str:
    """Add a Self reference node to a Blueprint's event graph.

    Args:
        blueprint_name: Name of the Blueprint
    """
    return json.dumps(send_command("add_blueprint_self_reference", {"blueprint_name": blueprint_name}))


@mcp.tool()
def add_blueprint_get_self_component_reference(blueprint_name: str, component_name: str) -> str:
    """Add a node that gets a component reference from Self in a Blueprint.

    Args:
        blueprint_name: Name of the Blueprint
        component_name: Name of the component
    """
    return json.dumps(send_command("add_blueprint_get_self_component_reference", {
        "blueprint_name": blueprint_name, "component_name": component_name
    }))


# ── Project Commands ─────────────────────────────────────────────

@mcp.tool()
def create_input_mapping(action_name: str, key: str) -> str:
    """Create an input action mapping in project settings.

    Args:
        action_name: Name for the input action
        key: Key to bind (e.g. SpaceBar, LeftMouseButton, W, A, S, D)
    """
    return json.dumps(send_command("create_input_mapping", {"action_name": action_name, "key": key}))


# ── UMG Widget Commands ─────────────────────────────────────────

@mcp.tool()
def create_umg_widget_blueprint(name: str) -> str:
    """Create a new UMG Widget Blueprint.

    Args:
        name: Name for the widget Blueprint
    """
    return json.dumps(send_command("create_umg_widget_blueprint", {"name": name}))


@mcp.tool()
def add_text_block_to_widget(widget_name: str, text: str, text_block_name: str = "TextBlock") -> str:
    """Add a text block to a UMG widget.

    Args:
        widget_name: Name of the widget Blueprint
        text: The text content
        text_block_name: Name for the text block element
    """
    return json.dumps(send_command("add_text_block_to_widget", {
        "widget_name": widget_name, "text": text, "text_block_name": text_block_name
    }))


@mcp.tool()
def add_button_to_widget(widget_name: str, button_name: str, button_text: str = "") -> str:
    """Add a button to a UMG widget.

    Args:
        widget_name: Name of the widget Blueprint
        button_name: Name for the button element
        button_text: Optional text to display on the button
    """
    params = {"widget_name": widget_name, "button_name": button_name}
    if button_text:
        params["button_text"] = button_text
    return json.dumps(send_command("add_button_to_widget", params))


@mcp.tool()
def bind_widget_event(widget_name: str, widget_element: str, event_name: str) -> str:
    """Bind an event on a UMG widget element.

    Args:
        widget_name: Name of the widget Blueprint
        widget_element: Name of the widget element (e.g. button name)
        event_name: Event to bind (e.g. OnClicked)
    """
    return json.dumps(send_command("bind_widget_event", {
        "widget_name": widget_name, "widget_element": widget_element, "event_name": event_name
    }))


@mcp.tool()
def set_text_block_binding(widget_name: str, text_block_name: str, binding_function: str) -> str:
    """Set a dynamic text binding on a text block.

    Args:
        widget_name: Name of the widget Blueprint
        text_block_name: Name of the text block
        binding_function: Name of the function to bind for dynamic text
    """
    return json.dumps(send_command("set_text_block_binding", {
        "widget_name": widget_name, "text_block_name": text_block_name, "binding_function": binding_function
    }))


@mcp.tool()
def add_widget_to_viewport(widget_name: str) -> str:
    """Add a UMG widget to the viewport at runtime.

    Args:
        widget_name: Name of the widget Blueprint to display
    """
    return json.dumps(send_command("add_widget_to_viewport", {"widget_name": widget_name}))


if __name__ == "__main__":
    mcp.run(transport="stdio")

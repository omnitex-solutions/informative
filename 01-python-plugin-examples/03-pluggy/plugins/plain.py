# 03-pluggy/plugins/plain.py

import pluggy

hookimpl = pluggy.HookimplMarker("myapp")


@hookimpl
def format_data(data: dict) -> str:
    """Simple key: value formatter."""
    lines = [f"{key}: {value}" for key, value in data.items()]
    return "\n".join(lines)

# 03-pluggy/plugins/json_fmt.py

import json
import pluggy

hookimpl = pluggy.HookimplMarker("myapp")


@hookimpl
def format_data(data: dict) -> str:
    """Pretty-print as JSON."""
    return json.dumps(data, indent=2)

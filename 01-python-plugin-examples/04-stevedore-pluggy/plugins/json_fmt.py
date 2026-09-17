# 04-stevedore-pluggy/plugins/json_fmt.py

import json

import pluggy

hookimpl = pluggy.HookimplMarker("myapp")


class JSONFormatter:
    """Pretty-print as JSON."""

    @hookimpl
    def format_data(self, data: dict) -> str:
        return json.dumps(data, indent=2)

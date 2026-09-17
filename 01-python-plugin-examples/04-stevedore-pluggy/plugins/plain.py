# 04-stevedore-pluggy/plugins/plain.py

import pluggy

hookimpl = pluggy.HookimplMarker("myapp")


class PlainFormatter:
    """Simple key: value formatter."""

    @hookimpl
    def format_data(self, data: dict) -> str:
        lines = [f"{key}: {value}" for key, value in data.items()]
        return "\n".join(lines)

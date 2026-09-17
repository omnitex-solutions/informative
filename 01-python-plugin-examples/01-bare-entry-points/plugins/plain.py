# 01-bare-entry-points/plugins/plain.py

class PlainFormatter:
    """Simple key: value formatter."""

    def format(self, data: dict) -> str:
        lines = [f"{key}: {value}" for key, value in data.items()]
        return "\n".join(lines)

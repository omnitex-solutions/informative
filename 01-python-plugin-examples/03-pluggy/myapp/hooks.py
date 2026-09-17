# 03-pluggy/myapp/hooks.py

"""
Hook specifications for the formatter system.
"""

import pluggy

hookspec = pluggy.HookspecMarker("myapp")


class FormatterSpec:
    """Specification that every formatter plugin must implement."""

    @hookspec
    def format_data(self, data: dict) -> str:
        """Return a string representation of the data."""

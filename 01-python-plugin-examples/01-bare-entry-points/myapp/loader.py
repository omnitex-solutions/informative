# 01-bare-entry-points/myapp/loader.py

"""
Bare-bones plugin loader using only the standard library.
No third-party dependencies.
"""

from importlib.metadata import entry_points
from typing import Any


def load_formatters(group: str = "myapp.formatters") -> dict[str, type]:
    """
    Discover and load all formatters registered under the given entry-point group.

    Returns a dict mapping plugin name -> formatter class.
    Failed plugins are skipped with a warning printed to stdout.
    """
    formatters: dict[str, type] = {}

    eps = entry_points(group=group)
    for ep in eps:
        try:
            cls = ep.load()
            formatters[ep.name] = cls
        except Exception as exc:
            print(f"[warning] Failed to load formatter '{ep.name}': {exc}")

    return formatters


def get_formatter(name: str, group: str = "myapp.formatters") -> Any:
    """Load a single formatter by name. Raises KeyError if not found."""
    formatters = load_formatters(group)
    if name not in formatters:
        available = ", ".join(sorted(formatters)) or "(none)"
        raise KeyError(f"Formatter '{name}' not found. Available: {available}")
    return formatters[name]()


if __name__ == "__main__":
    # Demo
    data = {"name": "Alice", "role": "Engineer", "level": 4}

    print("=== Available formatters ===")
    formatters = load_formatters()
    for name in sorted(formatters):
        print(f"  - {name}")

    print("\n=== plain ===")
    fmt = get_formatter("plain")
    print(fmt.format(data))

    print("\n=== json ===")
    fmt = get_formatter("json")
    print(fmt.format(data))

    print("\n=== table ===")
    fmt = get_formatter("table")
    print(fmt.format(data))

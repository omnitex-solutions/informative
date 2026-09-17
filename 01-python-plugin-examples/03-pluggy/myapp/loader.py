# 03-pluggy/myapp/loader.py

"""
Plugin system built with Pluggy (hook-based).
"""

import pluggy
from myapp.hooks import FormatterSpec, hookspec
from plugins import plain, json_fmt, table


def create_plugin_manager() -> pluggy.PluginManager:
    """Create and configure the PluginManager with all formatters."""
    pm = pluggy.PluginManager("myapp")
    pm.add_hookspecs(FormatterSpec)

    # Register the concrete plugins
    pm.register(plain)
    pm.register(json_fmt)
    pm.register(table)

    return pm


if __name__ == "__main__":
    data = {"name": "Alice", "role": "Engineer", "level": 4}

    pm = create_plugin_manager()

    print("=== Calling format_data hook on all plugins ===")
    # Pluggy collects results from every implementation
    results = pm.hook.format_data(data=data)

    for result in results:
        print(result)
        print("---")

# 04-stevedore-pluggy/myapp/loader.py

"""
Plugin system using Stevedore for discovery and Pluggy for behavior.
"""

import pluggy
from stevedore import extension

from myapp.hooks import FormatterSpec


PLUGIN_NAMESPACE = "myapp.formatters"


def create_plugin_manager() -> pluggy.PluginManager:
    """
    Discover formatter plugins with Stevedore and register them with Pluggy.

    Stevedore handles entry-point discovery and plugin construction. Pluggy
    handles the hook specification and invocation once the plugins are loaded.
    """
    pm = pluggy.PluginManager("myapp")
    pm.add_hookspecs(FormatterSpec)

    manager = extension.ExtensionManager(
        namespace=PLUGIN_NAMESPACE,
        invoke_on_load=True,
    )

    for ext in manager:
        pm.register(ext.obj, name=ext.name)

    return pm


if __name__ == "__main__":
    data = {"name": "Alice", "role": "Engineer", "level": 4}

    pm = create_plugin_manager()

    print("=== Discovered plugins ===")
    for name in sorted(pm.list_name_plugin()[0]):
        print(f"  - {name}")

    print("\n=== Calling format_data hook ===")
    results = pm.hook.format_data(data=data)

    for result in results:
        print(result)
        print("---")

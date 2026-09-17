# 02-stevedore/myapp/loader.py

"""
Plugin loading with Stevedore – quality-of-life layer on top of entry points.
"""

from stevedore import driver, extension


def load_single_formatter(name: str):
    """
    Load exactly one formatter by name using DriverManager.
    Instantiates it immediately (invoke_on_load=True).
    """
    mgr = driver.DriverManager(
        namespace="myapp.formatters",
        name=name,
        invoke_on_load=True,
    )
    return mgr.driver


def load_all_formatters():
    """
    Load every formatter in the namespace using ExtensionManager.
    Returns a dict of name -> live instance.
    """
    mgr = extension.ExtensionManager(
        namespace="myapp.formatters",
        invoke_on_load=True,
    )
    return {ext.name: ext.obj for ext in mgr}


def format_with_all(data: dict) -> dict[str, str]:
    """
    Call .format(data) on every discovered formatter.
    Demonstrates the convenient map() helper.
    """
    mgr = extension.ExtensionManager(
        namespace="myapp.formatters",
        invoke_on_load=True,
    )
    # map() calls the function for every extension
    results = mgr.map(lambda ext, d: (ext.name, ext.obj.format(d)), data)
    return dict(results)


if __name__ == "__main__":
    data = {"name": "Alice", "role": "Engineer", "level": 4}

    print("=== Single driver (json) ===")
    fmt = load_single_formatter("json")
    print(fmt.format(data))

    print("\n=== All formatters via map() ===")
    for name, output in format_with_all(data).items():
        print(f"\n--- {name} ---")
        print(output)

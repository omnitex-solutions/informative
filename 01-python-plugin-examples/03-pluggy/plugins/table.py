# 03-pluggy/plugins/table.py

import pluggy

hookimpl = pluggy.HookimplMarker("myapp")


@hookimpl
def format_data(data: dict) -> str:
    """Very simple fixed-width table."""
    if not data:
        return ""
    key_width = max(len(str(k)) for k in data)
    val_width = max(len(str(v)) for v in data.values())
    lines = [
        f"{'Key'.ljust(key_width)} | {'Value'.ljust(val_width)}",
        f"{'-' * key_width}-+-{'-' * val_width}",
    ]
    for k, v in data.items():
        lines.append(f"{str(k).ljust(key_width)} | {str(v).ljust(val_width)}")
    return "\n".join(lines)

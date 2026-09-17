# 02-stevedore/plugins/json_fmnt.py

import json


class JSONFormatter:
    """Pretty-print as JSON."""

    def format(self, data: dict) -> str:
        return json.dumps(data, indent=2)

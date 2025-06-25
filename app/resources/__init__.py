"""Load resource metadata for FastMCP components."""
from pathlib import Path
import yaml

RESOURCE_DIR = Path(__file__).parent


def load_resource(name: str) -> dict:
    """Return YAML data for the given resource name."""
    path = RESOURCE_DIR / f"{name}.yaml"
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)

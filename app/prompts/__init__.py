
"""Utilities for loading YAML prompt configurations."""

from pathlib import Path
import yaml


PROMPT_DIR = Path(__file__).parent


def load_prompt(name: str) -> dict:
    """Return YAML data for the given prompt name."""
    path = PROMPT_DIR / f"{name}.yaml"
    with open(path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh)

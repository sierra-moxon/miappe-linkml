"""Data model package for miappe-linkml."""

from pathlib import Path
from .miappe_linkml import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "miappe_linkml.yaml"

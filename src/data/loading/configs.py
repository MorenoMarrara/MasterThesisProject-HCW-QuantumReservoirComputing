from pathlib import Path
import os

DIR_SRC_UTILS = Path(os.path.dirname(__file__))
DIR_PROJECT_ROOT = DIR_SRC_UTILS.parent.parent.parent

DEV_DATA_DIR = DIR_PROJECT_ROOT / "data" / "107"
MODEL_DIR = DIR_PROJECT_ROOT / "models"
MODEL_DIR_CLASSICAL = MODEL_DIR / "classical"
MODEL_DIR_QRC = MODEL_DIR / "QRC"
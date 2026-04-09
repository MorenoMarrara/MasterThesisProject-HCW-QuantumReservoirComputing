import os
from pathlib import Path

DIR_SRC_UTILS = Path(os.path.dirname(__file__))
DIR_PROJECT_ROOT = DIR_SRC_UTILS.parent.parent

print(DIR_PROJECT_ROOT)

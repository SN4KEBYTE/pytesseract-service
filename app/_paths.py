from pathlib import Path

_CWD = Path(__file__).parents[1]

IMAGES_DIR = _CWD / 'images'
IMAGES_DIR.mkdir(
    exist_ok=True,
    parents=True,
)

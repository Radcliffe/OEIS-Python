# Make a shallow clone of the OEIS repository https://github.com/oeis/oeisdata
# into the directory ../oeisdata.
# If the directory already exists, fetch the newest changes.

import subprocess
import sys
from pathlib import Path
import logging


# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("oeis_data.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def clone_or_update_oeis_data(oeis_data_dir: Path, repo: str) -> None:
    """
    Clone the OEIS data repository if it doesn't exist, or update it if it does.
    """
    if not oeis_data_dir.exists():
        logging.info(f"Cloning OEIS data repository into {oeis_data_dir}...")
        subprocess.run(["git", "clone", "--depth", "1", repo, str(oeis_data_dir)], check=True)
    else:
        logging.info(f"Updating OEIS data repository in {oeis_data_dir}...")
        subprocess.run(["git", "-C", str(oeis_data_dir), "pull"], check=True)


if __name__ == "__main__":
    oeis_data_dir = Path("../oeisdata")
    repo = "https://github.com/Radcliffe/oeisdata"
    clone_or_update_oeis_data(oeis_data_dir, repo)

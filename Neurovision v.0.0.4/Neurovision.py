from subprocess import call
import time
from pathlib import Path
url = str(Path(__file__).parent.resolve())

call(["python", f"{url}/project.py"])
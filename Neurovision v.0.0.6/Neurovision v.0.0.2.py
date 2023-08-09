from subprocess import call
import time
from pathlib import Path
url = str(Path().absolute()).replace("\\", "/")
call(["python", f"{url}/project.py"])
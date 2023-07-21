from subprocess import call
import os
local_url = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
print(local_url)
call(["python", f"{local_url}/project.py"])


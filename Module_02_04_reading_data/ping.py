import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())


import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)      


import subprocess

subprocess.run(['ls', '-l'], cwd='/path/to/directory')

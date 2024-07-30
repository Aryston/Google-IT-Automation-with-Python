import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)


import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)

import subprocess
result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)
#subprocess.run(["pip", "install", "arrow"])
#import subprocess

import datetime
#import arrow
#import area


import sys

# Get a list of available module names
module_names = list(sys.modules.keys())

# Sort the list alphabetically
module_names.sort()  

# Print the list in a human-readable format
for name in module_names:
    print(name)

#iPconfig with python

import subprocess

result = subprocess.run(['IPconfig'], shell=True, capture_output=True, text=True)

print(result.stdout)



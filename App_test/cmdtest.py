import subprocess

result = subprocess.run("ipconfig", shell=True, capture_output=True, text=True)
x = result.stdout.split("\n")
print(x)
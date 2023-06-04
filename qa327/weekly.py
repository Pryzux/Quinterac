import subprocess
import os

# Set Python command depending on OS
if os.name == "nt":
    python_cmd = "python"
else:
    python_cmd = "python3"

# Run 5 days per week
for i in range(5):
    subprocess.run([python_cmd, "daily.py"])

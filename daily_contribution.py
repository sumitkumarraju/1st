import os
import subprocess
import time
from datetime import datetime

def make_commit():
    timestamp = datetime.now().isoformat()
    with open("contribution_log.txt", "a") as f:
        f.write(f"Contribution at {timestamp}\n")

    subprocess.run(["git", "add", "contribution_log.txt"], check=True)
    subprocess.run(["git", "commit", "-m", "verify files"], check=True)

if __name__ == "__main__":
    for i in range(10):
        print(f"Making commit {i+1}/10")
        make_commit()
        # Sleep for a short while to ensure timestamps differ slightly
        time.sleep(1)

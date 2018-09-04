import subprocess
import sys
import os

def run_cmd(cmd):
    try:
        proc = subprocess.Popen(cmd,
				shell=True,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE)
        proc.communicate()
    except Exception as err:
        print(err)
    finally:
        return proc.returncode

if __name__ == "__main__":
    rc = run_cmd("which git")
    if rc != 0:
        print("Error: Please install git first")
        sys.exit(rc)

    if not os.path.exists("pacemaker/xml"):
        print("#### Downloading pacemaker")
        cmd = "git clone https://github.com/ClusterLabs/pacemaker.git --depth=1 --branch master"
        rc = run_cmd(cmd)
        if rc != 0:
            print("Error: Download pacemaker failed!")
            sys.exit(rc)
        print("#### Done\n")

    #for f in os.listdir("pacemaker/xml"):
    #    if f.endswith(".rng"):
    #        print(f)

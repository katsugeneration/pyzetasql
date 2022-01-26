import sys
import subprocess


def build(setup_kwargs):
    subprocess.check_call('sh build.sh', shell=True, stdout=sys.stdout, stderr=sys.stderr)

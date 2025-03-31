import subprocess
from logger import logger

def setup_runner(service):
    try:
        logger("starting installing")
        res = subprocess.run([".", "/c/users/home/serviceInstaller", service], capture_output=True, text=True)
        if res.returncode == 1:
            logger(f'installing {service} failed, info: {res.stderr}', "ERROR")
        else:
            logger(f'{service} installing: {res.stdout}')
    except Exception as e:
        logger(f'failed to install: {e}', "ERROR")

logger("script running")

ans = str(input("please enter the service: "))

setup_runner(ans)
        
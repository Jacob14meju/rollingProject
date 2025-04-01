import sys
sys.path.append('infra-Automation/src')
from logger import logger

# function to input service name and then he installs it
def setup_runner(service):
    try:
        logger("starting installing")
        logger(f'{service} installing:')
        logger(f'{service} installed')
    except Exception as e:
        logger(f'failed to install: {e}', "ERROR")

logger("installer script running")

#script to check if the code is working

if __name__ == "__main__":
    ans = str(input("please enter the service: "))

    setup_runner(ans)
        
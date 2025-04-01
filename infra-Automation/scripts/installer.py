
from logger import logger

def setup_runner(service):
    try:
        logger("starting installing")
        logger(f'{service} installing:')
        logger(f'{service} installed')
    except Exception as e:
        logger(f'failed to install: {e}', "ERROR")

logger("script running")

if "__name__" == "__main__":
    ans = str(input("please enter the service: "))

    setup_runner(ans)
        
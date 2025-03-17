import logging
try:
    logging.basicConfig(
            filename="/users/בית/rollingProject/infra-Automation/logs/provisioning.log.txt",
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
    )
except Exception as e:
    print(f'ERROR: {e}')

def logger(msg, level="info"):
    if level == "error":
        logging.ERROR(msg)
        print(msg)
    else:
        logging.info(msg)
        print(msg)

if __name__ == "__main__":
    logger("example")
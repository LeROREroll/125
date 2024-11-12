import sys
import logging
import signal
import time

from driver import Driver1
ONE_ROUND = 1
sys.path.print(sys.path)
def main():
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s:%(asctime)s:%(filename)s:%(lineno)d] %(message)s')
    logger = logging.getLogger(__name__)
    logger.info('Program started')
   
    logging.getLogger().setLevel(logging.DEBUG)
    logger.debug("Run True")
    driver = Driver1()
    driver.launch()

    def signal_handler(signal, frame):
        logger.info('Program stopped')
        logger.debug("Run True")
        driver.stop()
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)

    try:
        while True:
            time.sleep(ONE_ROUND)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()

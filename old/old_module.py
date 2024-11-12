import threading
import time
import logging
"""
class Driver:
    ONE_SPEEN = 3  # seconds

    def __init__(self):
        self.param = 'driver'
        self.param_a = '000'
        self.param_b = ['a', 'b', 'c']
        self.param_c = '000'
        self.logger = logging.getLogger(__name__)

    def get_name(self):
        return f"{self.__class__.__name__}-{id(self)}"

    def launch(self):
        thread = threading.Thread(target=self.run)
        thread.daemon = True  # Set the thread as a daemon thread
        thread.start()

    def run(self):
        logger.debug("Run True")
        self.logger.info(f"thread started [{self.get_name()}]")
        while True:
            self.logger.info(f"{self.get_name()}")
            self.logger.info(f"\t{self.param_a}")
            self.logger.info(f"\t{self.param_b}")
            self.logger.info(f"\t{self.param_c}")
            time.sleep(self.ONE_SPEEN)

    def stop(self):
        self.logger.info(f"thread [{self.get_name()}] stopped")

def main():
    driver = Driver()
    driver.launch()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        driver.stop()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s:%(filename)s:%(lineno)d] %(message)s')
    main()
"""
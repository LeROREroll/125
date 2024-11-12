
import logging
import time
from config import ParamA, ParamB
from ..core.module import Module 

#from ..core.module import Driver as Module
ONE_SPEEN = 3  # seconds

class Driver1(Module):
    param_c = '000'  # class variable

    def __init__(self):
        super().__init__()
        self.param = 'driver'
        self.param_a = ParamA
        self.param_b = ParamB
        self.logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info(f'Thread [{self.get_name()}] started')
        while True:
            self.logger.info(self.get_name())
            self.logger.info('\t{}'.format(self.param_a))
            self.logger.info('\t{}'.format(self.param_b))
            self.logger.info('\t{}'.format(self.param_c))
            time.sleep(ONE_SPEEN)
        self.logger.info(f'Thread [{self.get_name()}] stopped')

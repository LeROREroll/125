import threading
from .logs.config import ParamB

class Module:
    def __init__(self):
        self.param = 'module'
        self.param_b = ParamB

    def get_name(self):
        return f"{self.__class__.__name__}-{id(self)}"

    def launch(self, successor):
        thread = threading.Thread(name=self.get_name(), target=successor.run)
        thread.start()
print(dir())
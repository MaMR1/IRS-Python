
from abc import ABC, abstractmethod

class Application(ABC):

    @abstractmethod
    def app_launch(self):
        ...

    @abstractmethod
    def app_menu(self):
        ...
    
    @abstractmethod
    def app_options(self):
        ...
        
    @abstractmethod
    def app_close(self):
        ...

    
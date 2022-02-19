from abc import (ABCMeta, abstractmethod)


class Crawler(metaclass=ABCMeta):
    
    @abstractmethod
    def get_link(self):
        pass
    
    @abstractmethod
    def download(self):
        pass


class Factory(metaclass=ABCMeta):
    
    @abstractmethod
    def get_crawler(self):
        pass
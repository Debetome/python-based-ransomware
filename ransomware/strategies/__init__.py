from abc import ABCMeta, abstractclassmethod, abstractmethod
from enum import Enum, auto

class Strategy(metaclass=ABCMeta):
    def log(self, text: str) -> None:
        print(f" - {text}")

    @abstractmethod
    def execute(self, file_path: str) -> None:
        pass

class StrategyType(Enum):
    DIRECTORY = auto()
    FILE = auto()
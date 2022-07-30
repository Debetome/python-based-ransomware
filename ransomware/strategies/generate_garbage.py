import random
import string
import os

from . import Strategy
from . import StrategyType

class GenerateRandomGarbage(Strategy):
    TYPE = StrategyType.DIRECTORY
    
    def __init__(self) -> None:
        super().__init__()
        self._exts = [".pdf", ".txt", ".xls", ".pkt", ".doc"]

    def execute(self, file_path: str) -> None:
        random_count = random.randint(5, 10)

        for i in range(random_count):
            random_ext = random.choice(self._exts)
            random_text = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, 47)))
            with open(f"{file_path}\\file{i}{random_ext}", "w+") as f:
                f.write(random_text)
                print(f"'file{i}.{random_ext}'")
import pickle
import os

from cryptography.fernet import Fernet
from typing import Any

from . import Strategy
from . import StrategyType

class DecryptFile(Strategy):
    TYPE = StrategyType.FILE

    def __init__(self, key=None) -> None:
        self._key = None
        if not self._key:
            self._deserialize_key()

    def _deserialize_key(self) -> None:
        key_file = open("key.fer", "rb")
        self._key = pickle.load(key_file)

    def execute(self, file_path: str) -> None:
        pass
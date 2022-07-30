import pickle
import os

from cryptography.fernet import Fernet
from typing import Any

from . import Strategy
from . import StrategyType

class EncryptFile(Strategy):
    TYPE = StrategyType.FILE

    def __init__(self, key=None) -> None:
        super().__init__()
        self._key = key
        if not self._key:
            self._key = Fernet.generate_key()
        self._serialize_key()

    def _serialize_key(self) -> None:
        if os.path.exists("key.fer"):
            self._deserialize_key()
            return None
        
        with open("key.fer", "wb") as f:
            pickle.dump(self._key, f)

    def _deserialize_key(self) -> None:
        if not os.path.exists("key.fer"):
            return None
        key_file = open("key.fer", "rb")
        self._key = pickle.load(key_file)

    def execute(self, file_path: str) -> None:
        cipher = Fernet(self._key)
        with open(f"{file_path}", "rb") as f:
            content = f.read()
            f.close()

        new_encrypted_filename = f"{file_path}.crypt"
        os.remove(file_path)

        with open(new_encrypted_filename, "wb") as f:
            encrypted = cipher.encrypt(content)
            f.write(encrypted)

        self.log(f"'{file_path}' encrypted!")
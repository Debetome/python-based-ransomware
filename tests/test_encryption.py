import unittest

from ransomware.strategies.encrypt import EncryptFile

class TestEncryption(unittest.TestCase):
    def test_instantiate_strategy(self):
        try:
            encrypt = EncryptFile()
        except Exception as ex:
            print(f"[-] {ex}")
            print(f"[-] Unable to instantiate strategy {EncryptFile}")

    def test_execute_encryption(self):
        try:
            with open("test_file.txt", "w+") as f:
                f.write("This is just a test file!")

            encrypt = EncryptFile()
            encrypt.execute("test_file.txt")

        except Exception as ex:
            print(f"[-] {ex}")
            print(f"[-] Unable to encrypt test file! ...")
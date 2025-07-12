from abc import ABC, abstractmethod
import subprocess
from pprint import pprint

"""
Base Command class implementing both Singleton and Command Handler patterns.

The Singleton pattern ensures only one instance of each command exists,
managed through the get_instance() class method.

The Command Handler pattern decouples command execution from its implementation,
allowing new commands to be added by extending this base class and implementing
the execute() method.

Example:
    class MyCommand(Command):
        def execute(self, *args):
            # Command implementation
            pass

    # Get singleton instance
    cmd = MyCommand.get_instance()
    cmd.execute('arg1', 'arg2')
"""
class Base(ABC):
    instance = {}

    @classmethod
    def get_instance(cls):
        if cls not in cls.instance:
            cls.instance[cls] = cls()
        return cls.instance[cls]
    
    @abstractmethod
    def execute(self, *args):
        pass

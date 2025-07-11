from .base import Command

"""
Command Bus implementing both Singleton and Command Registry patterns.

The Command Bus acts as a central registry and dispatcher for commands in the system.
It maintains a mapping of command names to their handler classes and routes command
execution requests to the appropriate handler.

Commands are registered via add_command() and executed via execute().

Example:
    # Register a command
    bus = BusCommand.get_instance()
    bus.add_command(MyCommand)

    # Execute a command
    bus.execute('mycommand', 'arg1', 'arg2')

Attributes:
    commands (dict): Mapping of command names to handler classes
"""

class BusCommand(Command):
    def __init__(self):
        self.commands = {}

    def add_command(self, command: Command):
        name = command.__name__.lower().replace("command", "")
        self.commands[name] = command

    def execute(self, name: str, *args):
        handler_class = self.commands.get(name)
        
        if not handler_class:
            raise ValueError(f"Command {name} not found")
        
        command = handler_class.get_instance()

        if not args:
            raise ValueError(f"No arguments provided for command {name}")
        
        command.execute(*args)
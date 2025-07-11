import importlib
import pkgutil

from fastapi import FastAPI

"""
Bootstrap module for registering controllers and commands.

This module is responsible for initializing the application by:
    - Registering controllers with FastAPI
    - Registering commands with the Command Bus
"""
def register_controllers(app: FastAPI) -> None:
    import controllers

    modules = pkgutil.iter_modules(controllers.__path__)
    for _, module_name, _ in modules:
        module = importlib.import_module(f"controllers.{module_name}")
        if hasattr(module, "router"):
            app.include_router(module.router)

"""
Register commands with the Command Bus.

This function iterates through the commands package and registers each command
with the Command Bus. Commands are identified by their class name ending with "Command".
Only one command class per module is supported - if multiple command classes exist in
a module, only the first one will be registered.
"""
def register_commands() -> None:
    import re
    from services import commands
    from services.commands.bus import Bus as BusCommand

    modules = pkgutil.iter_modules(commands.__path__)
    pattern = re.compile(r"^.+Command$")
    for _, module_name, _ in modules:
        module = importlib.import_module(f"services.commands.{module_name}")
        classes = [name for name in dir(module) if pattern.match(name)]
        if classes:
            class_name = getattr(module, classes[0])
            BusCommand.get_instance().add_command(class_name)

"""
Main entry point for application initialization.

This function orchestrates the registration of controllers and commands,
ensuring the application is properly configured before starting.
"""
def run(app: FastAPI) -> None:
    register_commands()
    register_controllers(app)

import importlib
import pkgutil

from fastapi import FastAPI

import controllers

def register_controllers(app: FastAPI) -> None:
    modules = pkgutil.iter_modules(controllers.__path__)
    for _, module_name, _ in modules:
        module = importlib.import_module(f"controllers.{module_name}")
        if hasattr(module, "router"):
            app.include_router(module.router)

def run(app: FastAPI) -> None:
    register_controllers(app)

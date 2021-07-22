from fastapi import FastAPI

import importlib
import os

def find_routes():
    """Looks in the modules directory for files that start with
    the name mod_. ex: mod_users.py
    
    Returns a list of dicts"""
    routes = []
    files = os.listdir("routes")
    for f in files:
        if "route_" in f:
            route_file = f.replace(".py", "")
            route_name = route_file.replace("route_", "")
            routes.append({
                "route_file": route_file, 
                "name": route_name, 
                "my_module": f"{route_name}_module",  
                "my_instance": f"{route_name}_instance"
            })
    return routes

app = FastAPI()

@app.get("/")
async def main_hello():
    return {"msg": "main page"}

for route in find_routes():
    route_file = route["route_file"]
    name = route["name"]
    route["my_module"] = importlib.import_module(f"routes.{route_file}")
    route["my_instance"] = getattr(route["my_module"], f"app_{name}") 
    app.mount(f"/{name}", route["my_instance"])
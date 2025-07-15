import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump({}, f)

def read_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def write_memory(key, value):
    data = read_memory()
    data[key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f)

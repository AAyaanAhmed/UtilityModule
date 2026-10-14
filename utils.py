import os
from datetime import datetime

def is_num(v):
    try:
        float(v)
        return True
    except:
        return False

def cap(txt):
    return txt.strip().title()

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def exists(file):
    return os.path.exists(file)

def read(file):
    if exists(file):
        with open(file, "r") as f:
            return f.read()
    return "File not found"

def write(file, data):
    with open(file, "w") as f:
        f.write(data)

def today():
    return datetime.now().strftime("%d-%m-%Y")

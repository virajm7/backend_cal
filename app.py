from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

app = FastAPI()

# 🔓 Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- Logic ----------
def add_numbers(a: float, b: float):
    return a + b

def subtract_numbers(a: float, b: float):
    return a - b

def multiply_numbers(a: float, b: float):
    return a * b

def divide_numbers(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero not allowed")
    return a / b

# ---------- APIs ----------
@app.get("/add")
def add(a: float, b: float):
    return {"result": add_numbers(a, b)}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": subtract_numbers(a, b)}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": multiply_numbers(a, b)}

@app.get("/divide")
def divide(a: float, b: float):
    return {"result": divide_numbers(a, b)}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 🔓 Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # allow requests from any website
    allow_credentials=True,
    allow_methods=["*"],      # allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],      # allow all headers
)

def add_numbers(a: float, b: float):
    return a + b

@app.get("/add")
def add(a: float, b: float):
    result = add_numbers(a, b)
    return {"sum": result}

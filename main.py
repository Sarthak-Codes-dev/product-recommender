from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# 🔥 ADD THIS CORS CONFIG
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    budget: int
    gaming: bool
    coding: bool

@app.post("/recommend")
def recommend(data: UserInput):
    products = [
        {"name": "ASUS TUF", "price": 75000, "use_case": ["gaming","coding"]},
        {"name": "MacBook Air", "price": 85000, "use_case": ["coding"]},
        {"name": "HP Pavilion", "price": 60000, "use_case": ["coding"]},
    ]
    return products
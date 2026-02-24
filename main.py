from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Input structure
class UserInput(BaseModel):
    budget: int
    gaming: bool
    coding: bool

# Home route
@app.get("/")
def home():
    return {"message": "Server working"}

# Recommendation route
@app.post("/recommend")
def recommend(data: UserInput):
    products = [
        {"name": "ASUS TUF", "price": 75000, "use_case": ["gaming","coding"]},
        {"name": "MacBook Air", "price": 85000, "use_case": ["coding"]},
        {"name": "HP Pavilion", "price": 60000, "use_case": ["coding"]},
    ]
    return products
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
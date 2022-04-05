from fastapi.middleware.cors import CORSMiddleware
from DIXI.auth.router import user_router
from DIXI.product.router import product_router
from DIXI.review.router import review_router

from fastapi import FastAPI


app = FastAPI()


origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)


app.include_router(product_router)
app.include_router(user_router)
app.include_router(review_router)


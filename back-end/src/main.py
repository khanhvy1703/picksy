from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import movie

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movie.router, prefix="/api/v1/movies", tags=["movies"])

@app.get("/")
def root():
    return {"message": "Picksy backend is running"}

if __name__ == "__main__":
    import uvicorn

    print("Backend is running on http://localhost:5000")
    uvicorn.run("src.main:app", host="0.0.0.0", port=5000, reload=True)
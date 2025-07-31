from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers.vehicles import router as vehicles_router
from app.routers.patrols import router as patrols_router
from app.routers import patrol_logs
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI app instance
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(vehicles_router)
app.include_router(patrols_router)
app.include_router(patrol_logs.router)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
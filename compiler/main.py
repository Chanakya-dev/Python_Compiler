from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from compiler.routes.code_executor import router as code_executor_router
import os
app = FastAPI()
print("Current working directory:", os.getcwd())
os.chdir("/app/compiler")
print("Current working directory:", os.getcwd())
# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the router
app.include_router(code_executor_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Compiler API"}




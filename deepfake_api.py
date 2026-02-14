from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import asyncio
import random

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    
    await asyncio.sleep(3) 
    
    
    confidence = random.randint(85, 99)
    is_fake = random.choice([True, False])
    
    status = "DEEPFAKE DETECTED" if is_fake else "REAL VIDEO"
    color = "#ff4444" if is_fake else "#00ff88"

    return {
        "filename": file.filename,
        "result": status,
        "confidence": f"{confidence}%",
        "color": color
    }

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8001)

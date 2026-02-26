import os
import uvicorn

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use Render's PORT, fallback to 8000 locally
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",                  # MUST be 0.0.0.0
        port=port,
        reload=False                     # No reload on prod
    )

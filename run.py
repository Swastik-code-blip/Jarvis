import uvicorn
import os

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))          # Railway sets PORT, fallback to 8000 locally
    reload = os.getenv("ENV") != "production"    # optional: reload only if not prod

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=port,
        reload=reload
    )


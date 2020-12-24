import os

import uvicorn

staging_level = os.environ.get("STAGING_LEVEL", "dev")
host0 = os.environ.get("HOST0", "0.0.0.0")
port0 = os.environ.get("PORT0", 8080)

if __name__ == "__main__":
    reload = staging_level == "dev"
    app = "async_api.app:app"
    uvicorn.run(app, host=host0, port=port0, reload=reload)

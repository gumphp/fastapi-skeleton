from bootstrap.application import create_app
from config.config import settings
import uvicorn

# 不再需要bcrypt补丁
# from app.patches import bcrypt_patch
# 仍然保留警告过滤模块以防其他警告
# from app.patches import warnings_filter

app = create_app()


@app.get("/")
async def root():
    return "welcome to fastapi skeleton"


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=settings.SERVER_HOST, port=settings.SERVER_PORT)

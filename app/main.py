from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config import Settings
from app.routes import router
from livereload import Server

settings = Settings()

def get_app() -> FastAPI:
    """Create a FastAPI app with the specified settings."""

    app = FastAPI(**settings.fastapi_kwargs)
    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
    app.include_router(router)

    return app


app = get_app()

if __name__ == "__main__":
    server = Server(app)
    server.watch('app/')  # replace with the path to your templates
    server.serve(root='.', host='0.0.0.0', port=8000)
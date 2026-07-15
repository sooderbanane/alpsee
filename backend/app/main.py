from fastapi import APIRouter, FastAPI


from app.api.v1 import health

def create_app() -> FastAPI:
    app = FastAPI(title="Alpsee", version="0.1.0")

    app.include_router(health.router, prefix="/api/v1")
    
    return app


def main():
    print("Hello from alpsee!")


if __name__ == "__main__":
    main()

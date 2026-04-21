from fastapi import FastAPI
import dotenv
from app.routers.feelings_router import router

app = FastAPI(
    title="Feelings Clasifier"
)

dotenv.load_dotenv()

app.include_router(router=router)
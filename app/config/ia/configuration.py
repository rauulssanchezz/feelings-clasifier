import os
from groq import AsyncGroq
from dotenv import load_dotenv

load_dotenv()

ia_client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
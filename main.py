from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
client=Groq(
    api_key = os.getenv("GROQ_API_KEY"))
print (client.api_key)

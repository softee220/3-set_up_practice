import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print("My API Key is: ", api_key)
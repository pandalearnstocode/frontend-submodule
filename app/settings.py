import os
from dotenv import load_dotenv

load_dotenv()

API_URL_LOCAL = os.getenv('API_URL_LOCAL')
API_URL_DOCKER = os.getenv('API_URL_DOCKER')
DEPLOYMENT = os.getenv('deployment')
if DEPLOYMENT == "docker":
    API_URL = API_URL_DOCKER
else:
    API_URL = API_URL_LOCAL
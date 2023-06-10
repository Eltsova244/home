from dotenv import load_dotenv
from flask
import os
load_dotenv()
print(os.getenv("HOGWARTS_URL"))
ab=SQLAlchemy
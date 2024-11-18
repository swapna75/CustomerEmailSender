import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  
    SECRET_KEY = os.getenv("SECRET_KEY", "your-default-secret-key") 
    GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    CELERY_BROKER_URL = os.getenv("REDIS_URL")  
    CELERY_RESULT_BACKEND = os.getenv("REDIS_URL")  
    if not SECRET_KEY:
        raise ValueError("SECRET_KEY is missing! Please set it in the .env file.")
    if not SENDGRID_API_KEY:
        raise ValueError("SENDGRID_API_KEY is missing! Please set it in the .env file.")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("DATABASE_URL is missing! Please set it in the .env file.")
    if not CELERY_BROKER_URL:
        raise ValueError("REDIS_URL is missing! Please set it in the .env file.")

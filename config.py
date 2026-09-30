import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "pocketsmart-secret-key")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-1.5-flash"
    )

    UPLOAD_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "uploads"
    )

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)



class Settings:
    PROJECT_TITLE: str = 'Jobboard'
    PROJECT_VERSION: str = '0.1.1'

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PSWRD: str = os.getenv("POSTGRES_PSWRD")
    POSTGRES_SRVR: str = os.getenv("POSTGRES_SRVR")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PSWRD}@{POSTGRES_SRVR}:{POSTGRES_PORT}/{POSTGRES_DB}" 

settings = Settings()
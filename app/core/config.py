import os
from typing import Optional, Dict, Any, List, Union
from pydantic import validator, PostgresDsn, BaseSettings , AnyHttpUrl
import secrets    
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" # secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 # 8days
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl
    # print(os.getenv("BACKEND_CORS_ORIGINS"))
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str],str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)
    # print(load_dotenv())
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")

    # POSTGRES_SERVER: str
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_DB: str
    # SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    # @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #         if isinstance(v, str):
    #             return v
    #         return PostgresDsn.build(
    #             scheme="postgresql",
    #             user=values.get("POSTGRES_USER"),
    #             password=values.get("POSTGRES_PASSWORD"),
    #             host=values.get("POSTGRES_SERVER"),
    #             path=f"/{values.get('POSTGRES_DB') or ''}",
    #         )
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/db_test")
    USERS_OPEN_REGISTRATION: bool = True
    EMAILS_ENABLED: bool = True
    # EmailStr = "test@example.com"
    # EMAIL_TEST_USER: EmailStr    # type: ignore
    # FIRST_SUPERUSER: EmailStr
    # FIRST_SUPERUSER_PASSWORD: "1234"
    class Config:
        case_sensitive = True
        env_file = ".env"
    
settings = Settings()
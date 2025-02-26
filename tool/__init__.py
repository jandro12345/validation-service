"""
Tools
"""
import logging
from os import getenv
from typing import Annotated, Any
from dotenv import load_dotenv
from fastapi import HTTPException, Header
import jwt


logging.basicConfig(level=logging.INFO)


load_dotenv()


DSN = f"""
    user={getenv("PG_USER", "0")}
    password={getenv("PG_PASS", "0")}
    host={getenv("PG_HOST", "0")}
    port={getenv("PG_PORT", "0")}
    dbname={getenv("PG_DB", "0")}
    """



async def verification_token(Token: Annotated[Any, Header()]):
    """
    verification token
    """
    try:
        token_decode = jwt.decode(Token, getenv("TOKEN"), algorithms=["HS256"])
        if not token_decode.get("authorized-transaction"):
            raise HTTPException(status_code=404, detail="Not Found")
    except jwt.InvalidTokenError as exc:
        raise HTTPException(status_code=400, detail="Invalid Token") from exc
    return Token

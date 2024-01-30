from fastapi import HTTPException, status


DATE_FORMAT = "%d/%m/%Y"
DATE_TIME_FORMAT = "%d/%m/%Y  %H:%M:%S"

CREDENTIALS_EXCEPTION = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

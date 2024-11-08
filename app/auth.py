from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
import secrets

security = HTTPBasic()

# Get credentials from environment variables
USERNAME = os.getenv("AUTH_USERNAME", "default")
PASSWORD = os.getenv("AUTH_PASSWORD", "default")

def verify_credentials(credentials: HTTPBasicCredentials = Depends(security)):
    """Verify the HTTP Basic Auth credentials."""
    is_username_correct = secrets.compare_digest(credentials.username.encode(), USERNAME.encode())
    is_password_correct = secrets.compare_digest(credentials.password.encode(), PASSWORD.encode())
    
    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
"""
Auth Service - SSO, RBAC, Multi-Tenant Authentication

Extracted from NT-AI-Engine monolith for Phase 3 Week 2
"""

from fastapi import FastAPI, HTTPException, Depends, Header
from pydantic import BaseModel
from enum import Enum
import jwt
from datetime import datetime, timedelta

app = FastAPI(title="NT-AI Auth Service")

# Configuration (from environment)
SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"

class Role(str, Enum):
    ADMIN = "admin"
    DEVELOPER = "developer"
    VIEWER = "viewer"

class AuthType(str, Enum):
    OAUTH2 = "oauth2"
    API_KEY = "api_key"

class LoginRequest(BaseModel):
    username: str
    password: str
    tenant_id: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int = 3600

@app.post("/auth/login", response_model=TokenResponse)
async def login(request: LoginRequest):
    """
    OAuth2 login flow

    TODO: Integrate with Azure AD/GitHub OAuth
    For now: Simple JWT generation
    """

    # Create JWT token
    payload = {
        "sub": request.username,
        "tenant_id": request.tenant_id,
        "role": Role.DEVELOPER.value,  # Default role
        "exp": datetime.utcnow() + timedelta(hours=1)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return TokenResponse(access_token=token)

@app.get("/auth/verify")
async def verify_token(authorization: str = Header(...)):
    """Verify JWT token"""

    try:
        # Extract token from "Bearer <token>"
        token = authorization.split(" ")[1] if " " in authorization else authorization

        # Decode and verify
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        return {
            "valid": True,
            "user": payload.get("sub"),
            "tenant_id": payload.get("tenant_id"),
            "role": payload.get("role")
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(401, "Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Invalid token")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "auth"}

"""NT-AI Python SDK - Shared utilities for all services"""

from .http_client import get_http_client
from .logging_config import get_logger
from .auth import require_auth, get_current_user

__version__ = "0.1.0"

__all__ = [
    "get_http_client",
    "get_logger",
    "require_auth",
    "get_current_user"
]

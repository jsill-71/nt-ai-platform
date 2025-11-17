# NT-AI Python SDK

**Shared utilities** for all NT-AI services

**Part of**: nt-ai-platform monorepo
**Usage**: Internal package for consistency across services

---

## Features

- HTTP client with retry logic
- Authentication helpers (JWT, OAuth2)
- Logging configuration (structured logging)
- Database utilities (connection pooling)
- Multi-tenant utilities (tenant context)

---

## Installation (within monorepo)

```python
# In any service's requirements
nt-ai-sdk @ file:../packages/sdk-python
```

---

## Usage

```python
from nt_ai_sdk import get_http_client, get_logger, require_auth

logger = get_logger(__name__)
http = get_http_client()

@require_auth(role="admin")
async def protected_endpoint():
    logger.info("Admin accessed endpoint")
    return {"status": "authorized"}
```

---

**Status**: Week 2 Task 2.2 implementation
**Progress**: Shared SDK foundation created

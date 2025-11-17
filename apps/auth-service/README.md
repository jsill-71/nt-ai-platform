# Auth Service

**Extracted from**: NT-AI-Engine monolith
**Purpose**: SSO, RBAC, multi-tenant authentication
**Status**: Week 2 implementation in progress

---

## Architecture

**FastAPI** microservice providing:
- OAuth2 authentication (Azure AD, GitHub)
- RBAC (roles: admin, developer, viewer)
- Multi-tenant isolation (tenant ID in all requests)
- JWT token management

---

## Endpoints

- POST /auth/login - OAuth2 login flow
- POST /auth/token - Exchange code for JWT
- GET /auth/verify - Validate JWT token
- POST /auth/refresh - Refresh token
- GET /auth/user - Get current user info

---

## Implementation Status

**Week 2 Task 2.1**: Auth service extraction
- Analyzing source in NT-AI-Engine
- Extracting OAuth2Connector
- Creating FastAPI endpoints
- Adding RBAC logic

**Next**: Shared SDK, PostgreSQL HA, Observability

---

**Part of**: Phase 3 Ultimate GitHub Strategy (Week 2)
**Timeline**: Continuous execution until Phase 3 complete

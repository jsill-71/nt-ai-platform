# Knowledge Graph Service

**Purpose**: Neo4j operations API for all NT-AI services
**Part of**: Phase 3 Week 3 - Platform Services
**Status**: Foundation created

---

## API Endpoints

- POST /kg/nodes - Create node
- GET /kg/nodes/{id} - Get node
- POST /kg/relationships - Create relationship
- GET /kg/query - Execute Cypher query
- GET /kg/health - Service health

---

## Features

- Connection pooling (Neo4j driver)
- Query caching (Redis)
- Multi-tenant isolation (tenant-scoped graphs)
- Health monitoring

---

**Week 3 Task 3.1**: Knowledge Graph service extraction
**Progress**: Foundation created, endpoints next
**Next**: Full API implementation

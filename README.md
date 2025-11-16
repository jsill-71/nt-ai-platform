# NT-AI Platform Services

**Platform services monorepo for NT-AI-Engine ecosystem**

Built with Turborepo + pnpm for high-performance builds.

## What This Is

Platform-as-a-service layer providing:
- **Auth Service**: SSO, RBAC, multi-tenant isolation
- **Observability Platform**: Logging, metrics, tracing
- **Data Platform**: PostgreSQL, Redis, Cosmos DB wrappers
- **Knowledge Graph Service**: Neo4j operations
- **Shared SDK**: Common utilities for all NT-AI services

## Architecture

```
nt-ai-platform/
├── apps/
│   ├── auth-service/          # SSO + RBAC
│   ├── observability/         # Grafana + Prometheus
│   └── knowledge-graph-api/   # Neo4j service
├── packages/
│   ├── sdk-python/            # Shared Python SDK
│   ├── sdk-types/             # TypeScript types
│   └── config/                # Shared configs
├── infrastructure/
│   ├── docker-compose/        # Local development
│   └── terraform/             # Azure deployment
├── turbo.json                 # Turborepo config
└── pnpm-workspace.yaml        # pnpm workspaces
```

## Quick Start

```bash
# Install dependencies
pnpm install

# Start all services
pnpm dev

# Run tests
pnpm test

# Build all
pnpm build
```

## Status

**Version**: 0.1.0 (Week 1 pilot)
**Created**: November 16, 2025
**Implementation**: Phase 3 (Ultimate GitHub Strategy)
**Timeline**: 20 weeks starting January 2026
**Budget**: $262.5K

See [Phase 3 Execution Plan](https://github.com/jsill-71/NT-AI-Engine/blob/main/PHASE3_DETAILED_EXECUTION_PLAN.md) for complete roadmap.

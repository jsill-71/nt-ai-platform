"""Knowledge Graph Service - Neo4j Operations API"""

from fastapi import FastAPI
from neo4j import AsyncGraphDatabase
import os

app = FastAPI(title="NT-AI Knowledge Graph Service")

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "trinity123")

driver = AsyncGraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

@app.post("/kg/query")
async def execute_query(cypher: str):
    """Execute Cypher query"""
    async with driver.session() as session:
        result = await session.run(cypher)
        return {"data": [dict(record) async for record in result]}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "knowledge-graph"}

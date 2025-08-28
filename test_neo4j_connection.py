#!/usr/bin/env python3

import os
from langchain_community.graphs import Neo4jGraph


# Test Neo4j connection
def test_neo4j_connection():
    # DB credentials - using the correct Bolt URL
    url = "bolt://localhost:7687"
    username = "neo4j"
    password = "your_password_here"

    print(f"Testing connection to: {url}")
    print(f"Username: {username}")

    try:
        # Create Neo4jGraph instance
        graph = Neo4jGraph(url=url, username=username, password=password)

        # Test a simple query
        result = graph.query("RETURN 1 as test")
        print("✅ Connection successful!")
        print(f"Test query result: {result}")

        return graph

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return None


if __name__ == "__main__":
    test_neo4j_connection()

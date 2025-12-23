from azure.cosmos import CosmosClient
import os

client = CosmosClient(
    os.getenv("COSMOS_DB_URI"),
    os.getenv("COSMOS_DB_KEY")
)

db = client.get_database_client(os.getenv("COSMOS_DB_NAME"))

users_container = db.get_container_client("users")
documents_container = db.get_container_client("documents")
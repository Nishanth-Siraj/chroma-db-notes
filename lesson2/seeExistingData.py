import chromadb

# client = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection(name="vehicles")

print(f"Collection retrieved: {collection.get()}")
import chromadb

# client  = chromadb.Client()
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.create_collection(name="vehicles")

collection.add(
    documents=[
       "car runs on road"
       ],
    ids=["car1"]
    )

print(f"Data is saved in the collection: {collection.get()}")
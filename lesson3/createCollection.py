import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="vehicles")

print(f"Collection retrieved: {collection.name}")

collection.add(
    documents=[
        "car runs on road",
       "plane flies in the sky",
       "boat sails on water",
       "bus is used for public transport",
    ],
    ids=["car1", "plane1", "boat1", "bus1"]
)

data = collection.get()

print("Data in collection:")
for i,doc in zip(data['ids'], data['documents']):
    print(f" - {i}: {doc}")


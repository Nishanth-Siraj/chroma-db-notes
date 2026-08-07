import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="vehicles")

collection.update(
    documents=[
        "car runs on road",
        "plane flies in the sky",
        "fish swims in water",
        "bus is used for public transport",
    ],
    ids=["car1", "plane1", "boat1", "bus1"]
)

print(f"the updated record is {collection.get()}")

record = collection.get(ids=["car1", "plane1", "boat1", "bus1"])

print("Data in collection:")
for i, doc in zip(record['ids'], record['documents']):
    print(f" - {i}: {doc}")
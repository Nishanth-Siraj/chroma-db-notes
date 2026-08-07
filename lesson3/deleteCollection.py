import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection(name="vehicles")

collection.delete(ids=["car1"])

print(f"the deleted record is {collection.get()}")
for i, doc in zip(collection.get()['ids'], collection.get()['documents']):
    print(f"data - {i}: {doc}")
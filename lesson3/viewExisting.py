import chromadb

client = chromadb.PersistentClient(path="./chroma_db")  

collection = client.get_collection(name="vehicles") 

data = collection.get()

print("Data in collection:")
for i, doc in zip(data['ids'], data['documents']):
    print(f" - {i}: {doc}")
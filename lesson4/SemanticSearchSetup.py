import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="my_collection")

collection.add(
    documents=[
        "car runs on petrol",
        "Bus carries many passengers on the road",
        "bicycle runs without petrol",
        "boat runs on water",
        "plane flies in the sky"
    ],
    ids=[
        "car",
        "bus",
        "bicycle",
        "boat",
        "plane"
    ]
)

print("Documents added to the collection successfully.")

results = collection.query(
    query_texts=["vehicle that doesnt require fuel"],
    n_results=3
)

print("Query results:")
for result in results['documents'][0]:
    print(f"{result} distance: {results['distances'][0][results['documents'][0].index(result)]}")

data = collection.get(include=["documents", "metadatas"])

print("Retrieved data from the collection:")
for doc, meta in zip(data['documents'], data['metadatas']):
    print(f"Document: {doc}, Metadata: {meta}")
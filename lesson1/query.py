import chromadb
client = chromadb.Client()

#create a collection
collection = client.create_collection(name="vehicles")

print("Collection created:", collection.name)

# Add some documents to the collection
collection.add(
    documents=[
       "car runs on road",
       "plane flies in the sky",
       "boat sails on water",
       "bus is used for public transport",
    ],
    ids=["car1", "plane1", "boat1", "bus1"]
)

# Query the collection
results = collection.query(
    query_texts=["if i have to catch a fish, what vehicle should I use?"],
    n_results=2
)

# Print the results
print("Query results:")
'''
Collection created: vehicles
Query results:
{'ids': [['boat1', 'car1']], 'embeddings': None, 'documents': [['boat sails on water', 'car runs on road']], 'uris': None, 'included': ['metadatas', 'documents', 'distances'], 'data': None, 'metadatas': [[None, None]], 'distances': [[1.3979741334915161, 1.4848012924194336]]}
'''
for i in range(len(results['documents'][0])):
    print(f"Document: {results['documents'][0][i]}, ID: {results['ids'][0][i]}, Distance: {results['distances'][0][i]}")

# else
print(results)
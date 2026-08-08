semantic search = relevance "fuel" is relevent to car or any fire based object
keyword search = find "123" data related to pk 123
when ever document added , chroma creates embeddings for document
when query asked, query converted to embedings.

vector query is made with query and data, nearer data to query embeddings considered.
answer for the comparison is the closest vectors.


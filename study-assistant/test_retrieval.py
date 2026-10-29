from sentence_transformers import SentenceTransformer
from vector_index import VectorIndex


with open("chunks.txt", "r", encoding="utf-8") as file:
    texts = file.read()
chunks = [chunk.strip()                         #removes white space
          for chunk in texts.split("\n\n")      #\n\n is paragraph break
          if chunk.strip()                      #keep this chunk if it contains text after striping
]

# print(len(chunks))        returns 10 as 10 chunks
# print(chunks[0])          returns 1st paragraph

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

index = VectorIndex()
index.add(embeddings,chunks)

print(index.vectors.shape)
print(len(index.texts))

queries = [
    "What is a database index?",
    "How can I find database records faster?",
    "Why can indexes slow down database updates?",
    "How do I retrieve users older than 18 from a database?",
    "What uniquely identifies each row in a table?",
    "How do tables reference records in other tables?",
    "How can I find an element efficiently in sorted data?",
    "How do I search through items one by one?",
    "Which data structure removes the newest item first?",
    "Which data structure processes the oldest item first?",
    "Two different keys produce the same hash value. What is this called?",
    "How does a hash table determine where to store a key?",
    "Hash collision?",
    "What is the difference between binary search and linear search?",
    "How does gradient descent update a neural network's weights?"
]

for query in queries:
    query_embeddings = model.encode(query)
    results = index.search(query_embeddings, k=3)
    print(f"\nQuery: {query}")
    for text, score in results:
        print(f"Score: {score:.4f} | {text[:80]}")
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer

from vector_index import VectorIndex
from prompt_build import build_prompt

load_dotenv()
client = genai.Client()

index = VectorIndex()

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("chunks.txt", "r", encoding="utf-8") as file:
    texts = file.read()
chunks = [chunk.strip()                     
          for chunk in texts.split("\n\n")     
          if chunk.strip()                     
]

embeddings = model.encode(chunks)
index.add(embeddings, chunks)

question = input("Ask a question: ")
question = question.strip()
if not question:
    print("No question was provided.")
    exit()
query_embedding = model.encode([question])

results = index.search(query_embedding[0], k=3)

retrieved_chunks = [text for text, score in results]

prompt = build_prompt(question, retrieved_chunks)

try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    print("\nAnswer:")
    print(response.text)

except Exception as e:
    print("An error occurred:", e)

print("\nAnswer:")
print(response.text)
import openai

openai.api_key = "YOUR_API_KEY"

def generate_embedding(text):
    response = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


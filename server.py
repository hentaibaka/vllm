from openai import OpenAI
client = OpenAI(
    base_url="http://localhost:8001/v1",
    api_key="token-abc123",
)

completion = client.chat.completions.create(
  model="IlyaGusev/saiga_llama3_8b",
  messages=[
    {"role": "user", "content": "Привет!, посоветуй книгу"}
  ]
)

print(completion.choices[0].message)

import openai

openai.api_key = "secret key"

response = openai.Image.create(prompt="a mammoth", n=1, size="1024x1024")

print(response)

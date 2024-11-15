import ollama


model = "llama3"  

response = ollama.chat(model=model, messages=[{"role": "user", "content": "when was gold discovered!"}])


print(response)

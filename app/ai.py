import ollama

# Define the model
model = "llama3"  # Or the model you want to use, replace with correct model name

# Test if the ollama package is working with the specified model
response = ollama.chat(model=model, messages=[{"role": "user", "content": "when was gold discovered!"}])

# Print the response
print(response)

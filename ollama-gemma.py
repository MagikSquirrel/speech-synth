import ollama

c = ollama.Client()
m = "gemma3:270m"
p = "What is the capital of France?"
r = c.generate(m, p)

print(r.response)
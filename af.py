with open("key.key", "rb") as f:
    data = f.read()
print("Raw key content:", data)
print("Key length:", len(data))

person = {"name": "Alice", "age": 30}

person["name"]                  # KeyError if missing
person.get("city")              # None if missing
person.get("city", "Unknown")   # custom default


person["email"] = "alice@example.com"
person.update({"age": 31, "job": "Engineer"})
person.setdefault("hobby", "reading")   # only sets if missing
del person["email"]
person.pop("hobby", None)               # safe remove


for k, v in person.items():
    print(k, v)


#merging

a = {"x": 1}
b = {"y": 2}
merged = a | b 


### LLM chat messages 

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is a dict?"},
]
messages.append({"role": "assistant", "content": "A key-value mapping."})

user_msg = [m["content"] for m in messages if m["role"] != "user"]

# print(user_msg)


### API request payload

payload = {
  "model":"gpt-4o-moni",
  "messages": messages,
  "temperature": 0.7,
  "max_tokens":256
}

defaults = {"temperature": 0.7, "max_tokens": 256}
params = {**defaults, "temperature": 0.2}

print(params)

corpus = "the cat sat on the mat".split()
vocab = {tok: i for i, tok in enumerate(sorted(set(corpus)))}
print(vocab)
no_parens = 1, 2, 3 

from_list = tuple([1, 2, 3])


#tuple is immutable but it holds the object that can be mutible like

t = (1, [2, 3])
t[1].append(4)
print(t)


t = (1, "hello", 3.14, True, None, [1, 2], {"a": 1}, (4, 5), len)

t = (1, 2, 2, 3)
t.count(2)       # 2
t.index(3)       # 3
2 in t           # True
(1, 2) + (3,)    # (1, 2, 3)
(0,) * 3         # (0, 0, 0)


distances = {
    ("Paris", "London"): 344,
    ("Paris", "Berlin"): 878,
}
distances[("Paris", "London")]    # 344

# Cache keyed by prompt + parameters
cache = {}
key = ("Hello", 0.7, 256)         # (prompt, temperature, max_tokens)
cache[key] = "model response"

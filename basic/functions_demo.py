def stats(nums):
    return min(nums), max(nums), sum(nums) / len(nums)

lo, hi, avg = stats([1, 2, 3])


def f(a, b, /, c, *, d):
    ...
# a, b: positional only | c: either | d: keyword only
f(1, 2, 3, d=4)
f(1, 2, c=3, d=4)


def total(*args):
  return sum(args)


def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)

show(model="gpt", temperature=0.7)

def call(prompt, *args, model="default", **kwargs):
    ...
    # print(prompt, args, model, kwargs)

call(12, model="x", temperature=0.5)
# Hi (1, 2) x {'temperature': 0.5}

defaults = {"temperature": 0.7, "max_tokens": 256}

def ask(prompt, **options):
    payload = {"prompt": prompt, **defaults, **options}
    return payload

ask("Hello", temperature=0.0, options=22)
# {'prompt': 'Hello', 'temperature': 0.0, 'max_tokens': 256}


#Type hints
def add(a: int, b: int) -> int:
    return a + b

def clean(text: str) -> str:
    return text.strip().lower()

def log(msg: str) -> None:
    print(msg)


# Collection as return type in python

def tokenize(text: str) -> list[str]:
  print(22)

def count_words(words: list[str]) -> dict[str, int]:
    return words.get(0), len(word.get(0))

tokenize("hi")

#function is just and object in python so we can pass it around

def apply(func, value):
  return func(value)

def multiply(a):
  return a * 3

print(apply(multiply, 2))

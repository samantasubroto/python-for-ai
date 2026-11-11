class Document:
  """A text document."""

  def __init__(self, text: str, source: str = "unknown"):
    self.text = text
    self.source = source

  def word_count(self) -> int:
    return len(self.text.split())

a = Document("AI for All", "Youtube")

# print(a.word_count())

class Model:
    registry = []                   # class attribute, shared by all instances

    def __init__(self, name):
        self.name = name            # instance attribute, one per object
        Model.registry.append(name)

Model("bert")
Model("gpt")
print(Model.registry)                     # ['bert', 'gpt']

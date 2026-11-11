text = "  Hello, World! Python for AI.  "

text.strip()                 # "Hello, World! Python for AI."
text.lower()                 # lowercase for normalization
text.upper()
text.title()
text.replace("World", "AI")
len(text)


sentence = "the quick brown fox"
tokens = sentence.split()            # ['the', 'quick', 'brown', 'fox']
" ".join(tokens)                     # back to a string
"a,b,c".split(",") 

s = "machine learning"
s[0:7]       # "machine"
s[-8:]       # "learning"
s[::-1]      # reversed

s = "Python for AI"
# print("addd".isalnum())


### prompt templates 

name = "AI"
prompt = f"""
hello world
this is 
python in the
world of
{name}
"""
# print (prompt)

from string import Template

t = Template("Translate $text to $lang.")
print(t.substitute(text="Hello", lang="French"))





stop_words = {"the", "a", "on", "is"}
words = "the cat sat on the mat".split()

[w for w in words if w not in stop_words]
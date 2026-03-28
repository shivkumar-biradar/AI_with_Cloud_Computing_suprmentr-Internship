import string

text = "Hello!!! This is @ChatGPT, 123"
cleaned = text.lower().translate(str.maketrans('', '', string.punctuation))
print(cleaned)



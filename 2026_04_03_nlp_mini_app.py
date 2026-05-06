from sklearn.feature_extraction.text import TfidfVectorizer

# sample text
text = """AI is the future. AI helps in automation. Python is widely used in AI."""

# TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform([text])

words = vectorizer.get_feature_names_out()
scores = X.toarray()[0]

# sort keywords
keywords = sorted(zip(words, scores), key=lambda x: x[1], reverse=True)

print("Top Keywords:")
for word, score in keywords[:5]:
    print(word)
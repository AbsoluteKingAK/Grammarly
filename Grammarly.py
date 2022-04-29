from textblob import TextBlob

txt = TextBlob(input("Enter A Sentence : "))

print(txt.correct())
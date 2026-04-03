from textblob import TextBlob

while True:

    text = input("Enter a sentence (or type 'exit' to quit): ").strip()

    if text.lower() == "exit":
        print("Goodbye!")
        break

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity #positive or negative
    subjectivity = analysis.sentiment.subjectivity # 0 = fact, 1 = opinion

    if polarity > 0.5:
        sentiment = "Extremely Positive"
    elif polarity > 0:
        sentiment = "Positive"
    elif polarity < -0.5:
        sentiment = "Extremely Negative"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"Sentiment: {sentiment}")
    print(f"Polarity Score: {polarity}")
    print(f"Subjectivity Score: {subjectivity}")

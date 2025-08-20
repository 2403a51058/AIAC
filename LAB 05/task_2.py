def analyze_sentiment():
    positive_words = {'awesome', 'excellent', 'good', 'great', 'fantastic', 'amazing', 'love', 'wonderful', 'happy'}
    negative_words = {'bad', 'terrible', 'awful', 'poor', 'hate', 'worst', 'sad', 'disappointing', 'boring'}

    text = input("Enter your sentence: ").lower()
    pos_count = sum(word in text for word in positive_words)
    neg_count = sum(word in text for word in negative_words)

    if pos_count > neg_count:
        sentiment = "positive"
    elif neg_count > pos_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print(f"Sentiment: {sentiment}")

if __name__ == "__main__":
    analyze_sentiment()
import pandas as pd
from textblob import TextBlob


def get_sentiment(text):
    """
    Analyzes the sentiment of a given text.

    Parameters:
        text (str): The text to analyze.

    Returns:
        str: The sentiment of the text, which can be 'Positive', 'Negative', or 'Neutral'.
    """
    if isinstance(text, str):
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            return "Positive"
        elif polarity < 0:
            return "Negative"
        else:
            return "Neutral"
    return "Neutral"  # Default sentiment for non-string inputs


def main():
    # Load the dataset
    file_path = '/Users/rohan/IdeaProjects/CMPE272-LLM-SentimentAnalysis/SentimentAnalysisTest.csv'
    df = pd.read_csv(file_path, encoding='ISO-8859-1')

    # Inspect the dataset structure
    print("Dataset Preview:")
    print(df.head())

    # Prepare the output file
    output_file = 'sentiment_analysis_output.txt'

    with open(output_file, 'w') as f:
        f.write("Sentiment Analysis Results:\n")
        f.write("=" * 30 + "\n")

        # Process each entry and write the sentiment result to the output file
        for index, row in df.iterrows():
            text = row['text']  # Assuming 'text' is the column containing the text data
            sentiment = get_sentiment(text)
            output = f"Entry {index + 1}:\nText: {text}\nSentiment: {sentiment}\n\n"
            f.write(output)
            print(output)  # Optional: Also print to the console

    print(f"Sentiment analysis results have been saved to {output_file}")

    # Optionally, save the results to a new CSV file
    df['Sentiment'] = df['text'].apply(get_sentiment)
    csv_output_file = 'sentiment_analysis_results.csv'
    df.to_csv(csv_output_file, index=False)


if __name__ == "__main__":
    main()

import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from NLP import sentimentscorer


def plot_sentiment_scores(movie_names):
    """
    This function takes each movie creates a bar char, plotting each positive, negative, and neutral sentiment score from each movie, from the NLP file
    """
    #1. intilaize an empty list for the different sentiment scores
    #2.1 for each movie in the movie names list 
        #2.2 set th escore equal to the sentiment score in the movie 
        #2.3.1 if the score of the movie is not none (which means we have a blank/error) 
            #2.3.2 then we append the scores (which appear as a dictionary in thier initial output) to the list
    #3. set the initial width of each bar to 0.2
    #4. Create a array of evenly spaced bars for each of the different movies, Chatgpt Link: https://chat.openai.com/share/fada5498-7ca2-45d9-aad8-665f7bc8a9ac
    #5-7. Make the negative bar be in th emiddle, and subtract bar width so the bars are even, as prior they were overlapping
    #8. Start the plot of the figure, with setting the size of the plot to 10 by 10
    #9-11: at the position  equal to x_, extract each score value for the score in sentiment scores depending on if it is positive/neutral/negative, set the width = 0.2, and the label equal to positive or neutral
    #12. Label the x-axis movie names
    #13. Label the y-axis sentiment score
    #14. Title the plot Sentiment Analysis of Keanue Reeves Movies  
    #15. plot the labels of hte x axis as movie names, and set the rotation to 14 due to the fact that titles are long
    #16. plot the legend 
    #17. show the plot 
    # Chatgpt Link: https://chat.openai.com/share/a712b981-0f86-494c-b43e-d1607b761398

    sentiment_scores = []
    for movie in movie_names:
        score = sentimentscorer(movie)
        if score is not None:
            sentiment_scores.append(score)

    bar_width = 0.2

    x = np.arange(len(movie_names))

    x_positive = x - bar_width
    x_negative = x
    x_neutral = x + bar_width

    plt.figure(figsize=(10, 10))
    
    plt.bar(x_positive, [score['pos'] for score in sentiment_scores], width=bar_width, label='Positive')
    plt.bar(x_negative, [score['neg'] for score in sentiment_scores], width=bar_width, label='Negative')
    plt.bar(x_neutral, [score['neu'] for score in sentiment_scores], width=bar_width, label='Neutral')

    plt.xlabel('Movie Names')
    plt.ylabel('Sentiment Score')
    plt.title('Sentiment Analysis of Keanue Reeves Movies')
    plt.xticks(x, movie_names, rotation=14)  # Set the x-axis labels

    plt.legend()

    plt.show()

def main():
    movie_names = [
        "John Wick (2014)",
        "John Wick: Chapter 2 (2017)",
        "John Wick: Chapter 3 - Parabellum (2019)",
        "John Wick: Chapter 4 (2023)",
        "The Matrix",
        "The Matrix: Resurrection"
    ]
    
    plot_sentiment_scores(movie_names)

if __name__ == "__main__":
    main()
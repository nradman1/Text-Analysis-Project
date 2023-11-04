from project import cleanreviewslist
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentimentscorer(moviename):
    """"
    This takes all of the reviews of a movie, converts them into a singular list, and outputs a score of the sentiments
    """
    #1. set clean review to the initial function that cleaned the reviews list 
    #2 intialize an empty list - as for this function, we want all of the reviews to be in a singular string
    #3.1 for each review in the cleaned list
        #3.2.1 for each word in the review
            #3.2.2 append the word to the list
    #4. make the sentence (string) equal to each word jointed by a space
    #5. the sentiment score is equal to the sentiment intensity analyze, which pulls the polarity scores of the sentence
    cleanedreview1 = cleanreviewslist(moviename, nostopwords=True)
    cleanedreview1no = []
    
    for review in cleanedreview1:
        for word in review:
            cleanedreview1no.append(word)
    sentence = ' '.join(cleanedreview1no)
    
    score = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return score

def main():
    """
    Test code
    """
    print(sentimentscorer("John Wick (2014)"))
    print(sentimentscorer("John Wick: Chapter 2 (2017)"))
    print(sentimentscorer("John Wick: Chapter 3 - Parabellum (2019)"))
    print(sentimentscorer("John Wick: Chapter 4 (2023)"))
    print(sentimentscorer("The Matrix"))
    print(sentimentscorer("The Matrix: Ressurecction"))

if __name__ == "__main__":
    main()
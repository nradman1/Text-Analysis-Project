from project import cleanreviewslist
from thefuzz import fuzz

def review_to_string(nameofmovie):
    """
    This function returns all of the reviews for one movie in a single sentence string
    """
    #1. set the variable equal to the review function we made in project.py
    #2. intialize an empy list called cleanedreview1no - we are using this to make all of the reviews for a movie in one list instead of having each review be a sublist in a larger list
    #3.1 for each of the reviews in the cleaned review list
        #3.2 for each of the words in each review
        #3.3 append each word to the empty list
    #4. join each of the words in the list with spaces to the variable sentence1 
    cleanedreview1 = cleanreviewslist(nameofmovie, nostopwords=True)
    cleanedreview1no = []
    
    for review in cleanedreview1:
        for word in review:
            cleanedreview1no.append(word)
    sentence1 = ' '.join(cleanedreview1no)

    return sentence1 

def fuzzratio(movie1, movie2):
    """
    Calculates the similarity ratio between two strings by comparing substrings or partial matches
    """
    sentence1 = review_to_string(movie1)
    sentence2 = review_to_string(movie2)
    return fuzz.ratio(sentence1, sentence2)


def partialratio(movie1, movie2):
    """
    Calculates the similarity ration between two strings by comparing entire strings
    """
    sentence1 = review_to_string(movie1)
    sentence2 = review_to_string(movie2)
    return fuzz.partial_ratio(sentence1, sentence2)


def tokensortratio(movie1, movie2):
    """
    calculate the similarity ratio between two strings after tokenizing, sorting, and comparing them 
    """
    sentence1 = review_to_string(movie1)
    sentence2 = review_to_string(movie2)
    return fuzz.token_sort_ratio(sentence1, sentence2)


def main():
    """
    test code goes here 
    """
    print(fuzzratio("John Wick (2014)","John Wick: Chapter 2 (2017)"))
    print(partialratio("John Wick (2014)","John Wick: Chapter 2 (2017)"))
    print(tokensortratio("John Wick (2014)","John Wick: Chapter 2 (2017)"))

    print(fuzzratio("John Wick (2014)","John Wick: Chapter 3 - Parabellum (2019)"))
    print(partialratio("John Wick (2014)","John Wick: Chapter 3 - Parabellum (2019)"))
    print(tokensortratio("John Wick (2014)","John Wick: Chapter 3 - Parabellum (2019)"))

    
    print(fuzzratio("John Wick (2014)","John Wick: Chapter 4 (2023)"))
    print(partialratio("John Wick (2014)","John Wick: Chapter 4 (2023)"))
    print(tokensortratio("John Wick (2014)","John Wick: Chapter 4 (2023)"))

    
    print(fuzzratio("John Wick (2014)","The Matrix"))
    print(partialratio("John Wick (2014)","The Matrix"))
    print(tokensortratio("John Wick (2014)","The Matrix"))

    print(fuzzratio("John Wick (2014)","The Matrix: Resurrection"))
    print(partialratio("John Wick (2014)","The Matrix: Resurrection"))
    print(tokensortratio("John Wick (2014)","The Matrix: Resurrection"))

          
if __name__ == "__main__":
    main()
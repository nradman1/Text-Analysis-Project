from imdb import Cinemagoer
import nltk
import string
from nltk.corpus import stopwords    #I used this website to learn more about implementing stopwords into my cleaning function (https://pythonspot.com/nltk-stop-words/) 

# create an instance of the Cinemagoer class
ia = Cinemagoer()

def reviewslist(nameofmovie):
    """
    Given the same of a movie, search for the movie's ID in cinemagoer and create a list of all of these reviews for this movie 
    """
    #1. search the cinemagoer library for the movie with a title matching name of movie, select the first result
    #2. set the movie ID to the id of the movie we just searched up 
    #3. Use the get movie reviews function in order to get reviews for the id of the movie we selected
    #4. intialize an empty list for the reviews
    #5.1 for each review, iterate through all of the data stored in the reviews
        #5.2 make a paragraph equal to the content of each review
        #5.3 add each review to the list of reviews
    #6. return the list of reviews 
    movie = ia.search_movie(nameofmovie)[0]
    id = movie.movieID

    reviews = ia.get_movie_reviews(id)
    listofreviews = []
    for review in range(len(reviews['data']['reviews'][0])):
        paragraph = reviews['data']['reviews'][review]['content']
        listofreviews.append(paragraph)

    return listofreviews

def cleanreviewslist(nameofmovie, nostopwords=True):
    """
    This function takes the list of reviews, and cleans it so it excludes stop words, as well as makes sure the words are strippable, so they are ready for the 
    """
    #1. make stop words a set, equal to all the english stop words
    #2. make strippables set to the string punctuation and whitespace
    #3. initalize a cleaned review list 
    #4. make the initial list euqal to the list of reviews from the function we just created
    #5.1 for all of the text in the inital list
        #5.2 replace the dashes with spaces, and replace the character of the em dash with spaces. There was an issue with periods and commas still showing up as words, even while using trippables, so we utilized a replace for these two functions as well. 
        #5.3 split the text into words 
        #5.4 intialize an empty list for cleaned words
        #5.5.1 for all of the words that have been split up and cleaned from the dashes
            #5.5.2 make the words stripped of the strppables and all lower case 
            #5.5.3.1 if the parameter is equal to  no stop words
                #5.5.3.2 if the words are not in the stop words list
                    #5.5.3.3 append the word to clean words
                #5.5.3.4 else append the word to the cleaned words 
        #5.5.2 append all of the words to the cleaned words list 

    stop_words = set(stopwords.words("english"))
    strippables = string.punctuation and string.whitespace
    
    cleanedreview = []
    startlist = reviewslist(nameofmovie)
    for text in startlist:
        text = text.replace('-', ' ').replace(chr(8212), ' ').replace('.',' ').replace(',',' ')
        words = text.split()
        cleanedwords = []

        for word in words:
            word = word.strip(strippables).lower()

            if nostopwords:
                if word not in stop_words:
                    cleanedwords.append(word)
            else:
                cleanedwords.append(word)

        cleanedreview.append(cleanedwords)
    
    return cleanedreview

def main():
    """
    Test code
    """
    print(cleanreviewslist("John Wick (2014)",nostopwords=True))
    print(cleanreviewslist("John Wick: Chapter 2 (2017)",nostopwords=True))
    print(cleanreviewslist("John Wick: Chapter 3 - Parabellum (2019)",nostopwords=True))
    print(cleanreviewslist("John Wick: Chapter 4 (2023)",nostopwords=True))
    print(cleanreviewslist("The Matrix",nostopwords=True))
    print(cleanreviewslist("The Matrix: Ressurecction",nostopwords=True))
    
if __name__ == "__main__":
    main()
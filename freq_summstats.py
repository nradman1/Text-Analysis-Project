#After cleaning the reviews from punctuation and stopwords, I want to find the 10 most common words used thought all o the reviews for each movie
from project import cleanreviewslist

def get_most_common_words (nameofmovie, number=10):
    """
    This function finds the n number of most common words from all of the reviews about a movie 
    """
    #1. Initialize the wordcount as an empty dictionary
    #2. Use the clean review list function in order to get a review list without strippables, stopwords, etc...
    #3.1 for each review in the list
     #3.2.1 for each word in the review
        #3.2.3 if the word is in the dictoinary alread
            #3.2.3.1 add 1 to the value of the word
        #3.2.4 else
            #3.3.4.1 set the inital value of the word to 1, since it is the first time it appears
    #4. sort each of the words based on their values, returning the second element of x, which is the frequency, sort in reverse order from largest to smallest
    #5. set the commonwords equal to the sortedwords, cut off my the number of words inserted in the parameter
    #6.1 for the words and their frequency in the sorted commonwords dictionary
        #6.2 print word:frequency
    wordcount = {}

    cleanedreview = cleanreviewslist(nameofmovie, nostopwords=True)

    for review in cleanedreview:
        for word in review:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
    
    sortedwords = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    commonwords = sortedwords[:number]

    for word, frequency in commonwords:
        print(f'{word}:{frequency}')


def get_unique_words(movie1, movie2):
    """
    This function returns list unique words for movie 1 and movie 2 
    """
    #1.make the first cleaned review equal to us calling the function cleanreviewslist from project.py for movie 1
    #2.the same as above but for the second movie

    #3. intilaize an empty list for movie 1 - this will be so we can turn the list with sublists of different reviews, to one list of words that appear in the reviews for the movie 
    #4.1 for each review in the cleaned reviews
       #4.2.1 for each word in the review
        #4.2.2 append the word to the cleaned reviews list
    #5-6. repeat the same as above but for movie 2
    #7. initalize an empty list called unique words
    #8.1 for each word in the list for movie 1
        #8.2.1 if the word in list for movie 1 is not in the word in list for movie 2
            #8.2.2 append the word to the unique words list 
    #9. return unique words

    cleanedreview1 = cleanreviewslist(movie1, nostopwords=True)
    cleanedreview2 = cleanreviewslist(movie2, nostopwords=True)

    cleanedreview1no = []
    for review in cleanedreview1:
        for word in review:
            cleanedreview1no.append(word)

    cleanedreview2no = []
    for review in cleanedreview2:
        for word in review:
            cleanedreview2no.append(word)

    unique_words = []
    for word in cleanedreview1no:
        if word not in cleanedreview2no:
            unique_words.append(word)

    return unique_words

def main():
    """
    test code goes here 
    """
    print(get_most_common_words("John Wick (2014)",number=10))
    print(get_most_common_words("John Wick Chapter 2 (2017)",number=10))
    print(get_most_common_words("John Wick: Chapter 3 - Parabellum (2019)",number=10))
    print(get_most_common_words("John Wick Chapter 4 (2023)",number=10))
    print(get_most_common_words("The Matrix",number=10))
    print(get_most_common_words("The Matrix: Resurrection",number=10))
    
    print(get_unique_words("John Wick (2014)","John Wick: Chapter 2 (2017)"))
    print(get_unique_words("John Wick (2014)","The Matrix"))
    print(get_unique_words("The Matrix","The Matrix: Resurrection"))


if __name__ == "__main__":
    main()
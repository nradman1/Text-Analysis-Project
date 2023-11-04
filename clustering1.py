import numpy as np
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
from similarity import fuzzratio
from similarity import partialratio
from similarity import tokensortratio

def plot_similarity_scatter(movie_names):
    plt.figure(figsize=(20, 10))
    
    for i in range(len(movie_names)):
        for j in range(i + 1, len(movie_names)):
            movie1 = movie_names[i]
            movie2 = movie_names[j]
            similarity_fuzz_ratio = fuzzratio(movie1, movie2)
            similarity_token_sort_ratio = tokensortratio(movie1, movie2)
            
            plt.scatter(similarity_fuzz_ratio, similarity_token_sort_ratio, label=f"{movie1} vs. {movie2}")

    plt.xlabel('fuzz.ratio')
    plt.ylabel('fuzz.token_sort_ratio')
    plt.title('Similarity Comparison for Movie Pairs')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


    plt.show()

if __name__ == "__main__":
    movie_names = [
        "John Wick (2014)",
        "John Wick: Chapter 2 (2017)",
        "John Wick: Chapter 3 - Parabellum (2019)",
        "John Wick: Chapter 4 (2023)",
        "The Matrix",
        "The Matrix: Resurrection"
    ]
    plot_similarity_scatter(movie_names)
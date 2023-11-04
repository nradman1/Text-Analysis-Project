# Text-Analysis-Project
 ## 1. Project Overview
The data source employed in this research project comprises IMDb movie reviews, a repository of movie critiques contributed by a diverse group of users. The principal focus of my analysis centers on the movie series, John Wick, encompassing installments 1, 2, 3, and 4. Furthermore, my study extends to the examination of other cinematic works featuring Keanu Reeves, the original Matrix film and it’s recent continuation, the Matrix Resurrections.  

I intend to employ sentiment analysis text similarity analysis techniques and coupled visualization form clustering with to achieve a comprehensive understanding of the prevailing sentiments and perceptual similarities surrounding these films. 

This endeavor aims to discern whether there are commonalities or distinctions in sentiment when of the John Wick series as well as The Matrix series. My objective is to discern the prevailing sentiments and, potentially, the rationale behind the decision to create sequels for certain films featuring Keanu Reeves. This research aspires to unveil whether there are consistent sentiment patterns in movies where Keanu Reeves assumes a lead role, or if there is a recurring sentiment associated with his participation in films that were deemed sequel-worthy, or that became multi-film series. 

 ## 2. Implementation
The structure I wanted to create for my code entailed an initial step of importing and cleaning the data in “projcet.py,” followed by an analysis of the data in “freq_summstats.py,” “similarity.py” and “NLP.py.” Afterwards I wanted to do visualization in “clutering1” and “clustering,”, based on the analyses from the previous steps. In the initial “project.py” bringing in the data was where I had to make my first decision. I needed to decide how I wanted to store the data; I selected to store each review as its own list of words within a larger list, rather than consolidating all reviews into a single list or treating them as individual words. This decision was motivated by the intent to preserve the reviews' integrity. An issue that I had with the file coming up was that the stripping of periods and commas from the strippables did not work. I am still unsure as to why, but I decided to bypass this by doing .replace() both commas and periods with spaces instead, which worked as a fixed, however, I was still wondering why strippables did not work properly, but that was my reason for using the replace function. 

Another key decision was made when calculating the most common words. Instead of focusing on individual reviews, I sought to identify the most common word in each movie, as a single review might not offer comprehensive insights into a film. To achieve this, I iterated through each review in "cleaned_review" and then through each word within each review, ensuring an exhaustive examination of all movies. 

For the "get_unique_words" function, aimed at identifying unique words between reviews, I restructured the lists to isolate words. This transformation allowed a more direct comparison between all reviews and all reviews for different movies, with all words for a single movie consolidated into a list. 

The main difficulties that I faced with this project was with the clustering and visualization aspect, as I had no experience prior to this with making graphs/charts on python. As recommended, I utilized matplotlib.pyplot and numpy as np. I went on the Matplotlib website and looked up examples of the scatterplot (link) as well as bar chart (link:https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-p ) to see how they worked, which reminded me of turtle. The first thing I wanted to do was graph the text similarity as scatter plot. I wanted to plot each combination of the fuzz ratio and the token sort ratio. To do this, I iterated using two for loops, one for the first movie in the pair i, and one for the second in the pair, which is i + 1, for the amount of movies that are left. I then utilized the fuzz and token short ratios implemented from earlier. One issue that I had here is the legend was extremely large and covering half the graph, so I utilized chatgpt, however, it gave me a unsatisfactory answer, as it only showed me the different options for loc. So, I instead utilized matplotlib.pyplot.legend — Matplotlib 3.8.1 documentation which showed me bbox_to_anchor, that allows you to move the legend to the right outside of the chart.  
The main difficulties that I faced with this project was with the clustering and visualization aspect, as I had no experience prior to this with making graphs/charts on python. As recommended, I utilized matplotlib.pyplot and numpy as np. I went on the Matplotlib website and looked up examples of the scatterplot (link:https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_demo2.html#sphx-glr-gallery-lines-bars-and-markers-scatter-demo2-p  ) as well as bar chart (link:https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html#sphx-glr-gallery-lines-bars-and-markers-bar-colors-py ) to see how they worked, which reminded me of turtle. The first thing I wanted to do was graph the text similarity as scatter plot. I wanted to plot each combination of the fuzz ratio and the token sort ratio. To do this, I iterated using two for loops, one for the first movie in the pair i, and one for the second in the pair, which is i + 1, for the amount of movies that are left. I then utilized the fuzz and token short ratios implemented from earlier. One issue that I had here is the legend was extremely large and covering half the graph, so I utilized chatgpt, however, it gave me a unsatisfactory answer, as it only showed me the different options for loc. So, I instead utilized matplotlib.pyplot.legend — Matplotlib 3.8.1 documentation which showed me bbox_to_anchor, that allows you to move the legend to the right outside of the chart.  
The main difficulties that I faced with this project was with the clustering and visualization aspect, as I had no experience prior to this with making graphs/charts on python. As recommended, I utilized matplotlib.pyplot and numpy as np. I went on the Matplotlib website and looked up examples of the scatterplot (link: ) as well as bar chart (link: ) to see how they worked, which reminded me of turtle. The first thing I wanted to do was graph the text similarity as scatter plot. I wanted to plot each combination of the fuzz ratio and the token sort ratio. To do this, I iterated using two for loops, one for the first movie in the pair i, and one for the second in the pair, which is i + 1, for the amount of movies that are left. I then utilized the fuzz and token short ratios implemented from earlier. One issue that I had here is the legend was extremely large and covering half the graph, so I utilized chatgpt, however, it gave me a unsatisfactory answer, as it only showed me the different options for loc. So, I instead utilized link: (https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html) documentation which showed me bbox_to_anchor, that allows you to move the legend to the right outside of the chart.  

I was also interested in how I could run a list of multiple movies through the parameters at once, so I asked chatgpt again if there was a way to do this, and this was the result:  
<!-- ![gpt](images/gpt.png) -->
<img src="images/gpt.png" width="400" alt="text clustering" style="display:block; margin:10px auto;"/>

This was a lot simpler than I initially thought, because I was able to iterate through all of the different movies as 2 parameters, utilizing both for I and for j in the range. I implemented this method in both the scatterplot and the bar chart, to get a comprehensive comparison of all the movies.  

I also had issues while setting up the bar chart. The first issue I had was getting the bars to not be placed on top of each other. I asked chatgpt how to get the bars to be evenly spaced out, and instead of using matplotlib, it suggested I use Numpy, link. To fix this, rather than have the bar’s width inside of the function and just as 0.2, I set it up so the negative would be in the middle, and subtract bar width from it and add it for positive and neutral, that way they did not overlap. I also used numpy to arrange it to get the position for each bar. However, after fixing this is still not done as the axis was messed up. I then looked at the Chart example and realized you could tilt it. 

Overall, there was a lot of different decisions to be made in order to get the correct results, which I will discuss subsequently.  

 ## 3. Results
#### Common Words
<!-- ![common words](images/commonwords1.png) -->
<img src="images/commonwords1.png" width="400" alt="text clustering" style="display:block; margin:10px auto;"/>
When analyzing the top words for each of the John Wick films, we can find some interesting insights. While the most common words all include the title of the film ‘John Wick’ in many of the films, which makes sense as it is the movie title, there are some interesting differences. For example, all reviews mention action, with the first one having it as the very first word, which shows how this is the focus of the film, and what resonated about the first one. Additionally, what is interesting is that the reviews for Chapter 2, 3, and 4 all say first in it, which probably all compare it to how great the first one is. Another interesting thing is Keanu reeves is mentioned in the reviews for chapter 1 and chapter 4, which shows maybe his prominence in acting stuck out in these two films. Lastly, it is interesting that the third one is the only one which mentions world, as he does travel the world in this film, as well as the only one that mentions fight, as a lot of fighting occurs in all of the films.  Also, the last film had ‘dumb’ being one of the top 10 words, showing its weakness in the series.

<!-- ![gpt](images/commonwrods2.png) -->
<img src="images/commonwrods2.png" width="400" alt="text clustering" style="display:block; margin:10px auto;"/>
Next, to compare the matrix movies, it also contained action in the most common words for both the films, shows reeve’s prominence as an actor in this space. Lastly, the last Matrix remake had “blah” in the most common words, which I thought was funny, as well as a good descriptor of the movie.

#### Unique Words
Next, we want to see the unique words in all of the reviews for the different movies to see if this could provide a difference analysis for both John Wick, the Matrix, and the sequel films to each of them, as well as between John Wick and the Matrix. There were many words unique to the first film, which include puppy, confusion, melodramatic, fantastic, soapy, and unstoppable. All of this makes sense, considering what occurs with his dog in the first movie, as well as the fast pace. When looking at the unique words between John Wick and the Matrix, there were significantly more – with John Wick speaking of the dog, car, and Russian (all very specific to the movie) as well as stunts, chaos, bloodshed, and violence, which I was surprised were not included in reviews about the Matrix. Lastly, words unique to the Matrix film vs. It's sequel were mentions of dystopia, terrifying, suspenseful, psychological, metallic, killing, and many more, but I was also surprised these were not included.

#### Text Analysis
<!-- ![Similarity](images/similarity.png) -->
<img src="images/similarity.png" width="400" alt="text clustering" style="display:block; margin:10px auto;"/>
We first analyzed the text similarity and created a plot of the fuzz ratio to the fuzz token to short ratio. This helped us visualize the similarity between each movie review comparison. It makes sense this shows a positive trend line due to the fact the token sort ratio tokenizes, sorts, and compares them. It was interesting that the most similar reviews by far were John Wick 1 and John Wick Chapter 2, but John Wick 1 and John Wick Chapter 3 were the least similar reviews. This was interesting and it showed even within the same series, there were big disparities between the movies. One could conclude John Wick 1 and 2 are more similar than the third film in the series, which had a different pace. I also found it interesting that John wick and the Matrix had the second most similarity in terms of their reviews.  found this very interesting as it the movies who are not in the same series at all. It shows how though, movies that both started off very popular Keanu Reeves series had very similar language utilized in their writing.

#### NLP Analysis
<!-- ![gpt](images/NLP.png) -->
<img src="images/NLP.png" width="400" alt="text clustering" style="display:block; margin:10px auto;"/>

Afterwards, we analyzed the Natural Language Processing data by creating a bar chat and plotting all the results of the Sentiment Scorer. What I found interesting about this one is John Wick 1 had the second most negative sentiment; it had 3 movies made afterwards. However, I think this could also be a result of the fact that the movie is particularly violent, and people were not used to it yet. Additionally, I believe people would not watch more of the films if they did not like it, contributing to the negative sentiment. I thought it was interesting that a film like the Matrix, which had the least negative sentiment had the sequel with the most negative and least positive sentiment overall, as well as the least neutral.>

 ## 4. Reflection
 What went well throughout the project was the data collection as well as the data analysis. The data proved to give me a good amount of data that I was able to use for all of the analysis, and I was able to get some interesting results. In addition, I think what went well was my utilization of examples from the matplot documentation website and Chatgpt to get well-formatted charts at the end. I learned a lot about data visualization within python which I did not know much about before, which allowed me to expand upon some skills we learned using turtle. I also learned a lot about making sure data is formatted correctly, as well as running lists as parameters through data sets, which is super helpful, as I now know the power of the for loop and iterations. Beforehand, I wish I knew more about different strategies to fix data visualizations, as I had a lot of trouble with the legend or the bars from the chart covering up other aspects of the chart.  
 I think that I could improve the process of cleaning the data more at the beginning, while I initially wanted to create a list of lists of reviews, I could have complied all of the words together immediately, instead of keeping it as a list in list format. I think the project was appropriately scoped, as I initially started off with trying to include even more Keanu Reeve’s movies (Point Break and the Devil’s Advocate) but I pared it back to just movies with series, to not have an overwhelming amount of data. I also had a good testing plan in that I was able to run my data multiple times without having any issues with it breaking or recursion, as well as could compare the different reviews and movies to each other to see if it was pulling properly.


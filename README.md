# ADM_HW3
Topics: Data Mining, Web Scraping, Algorithms for search engines.

# Homework 3 - Which book would you recomend?

*************************
### Goal
In this third HM I have dedicated myself to the construction of several search engines, based on Data Mining techniques. They have been built over the "best books ever" list of [Googlereads](https://www.goodreads.com/) in order to return the most coherent books based on the established search criteria.

### Get data to analyze
Not having an already structured dataset to work on, it was built from scratch through web scraping techniques and algorithms. Around 30k books have been scraped from Googlereads, and each one has been stored in a dataset containing the following columns:

1. Title (to save as bookTitle)
2. Series (to save as bookSeries)
3. Author(s), the first box in the picture below (to save as bookAuthors)
4. Ratings, average stars (to save as ratingValue)
5. Number of givent ratings (to save as ratingCount)
6. Number of reviews (to save as reviewCount)
7. The entire plot (to save as Plot)
8. Number of pages (to save as NumberofPages)
9. Published (Publishing Date)
10. Characters
11. Setting
12. Url

This dataset, stored in a .tsv file, is the starting point to the creating of our search engines.

## Files descriptions
The directory of this homework consists of several files:

1 `collector.ipynb`
> This Jupyter notebook file contains all the functions and  the descriptive process to collect your data from the html page (from which you get the urls), to save the urls in a .txt file and download in local the pages of different books.

  1.1 `lista.txt`
  > It is a .txt file in which each row is a link containing book's web page url.

2 `parser.ipynb`
> This Jupyter notebook file is the core of the Data Scraping process. It contains the functions and the descriptive process that let us to build the dataset. The functions of this file store the dataset in a .tsv file.

3 `articles.tsv`
> This is the final dataset that we have after the scraping process. It's a dataset composed by almost 30k rows/books and twelve columns.




**********************
*Homework made by:*
Tommaso Berritto

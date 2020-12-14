from bs4 import BeautifulSoup
import string
import requests
from selenium import webdriver
import spacy
import os
import pandas as pd
import re
from itertools import islice
import numpy as np
from nltk.tokenize import word_tokenize 
import nltk 
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
import csv
nltk.download('stopwords')
nltk.download('punkt')
import heapq 
import csv
from collections import defaultdict




#In this function we pre-process the data, in particular all the plots, thanks to the NLKT Python's library
def pre_processing (lista):
    vocabulary = "".join(lista)
    vocabulary = vocabulary.lower()
    vocabulary_p = "".join([char for char in vocabulary if char not in string.punctuation])
    vocabulary_words = word_tokenize(vocabulary_p)
    stop_vocabulary_words = stopwords.words('english')

    filtered_words = [word for word in vocabulary_words if word not in stop_vocabulary_words]
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in filtered_words]
    
    return stemmed



# This function creates a vocabulary of word in our corpus and maps with a number each one
def create_vocabulary (descriptions):
    
    vocabulary_pp = pre_processing(descriptions)
    
    d = dict()
    i = 0
    for word in vocabulary_pp:
        if word not in d:
            d[word] = i
            i += 1
    
    return d



# it's a function that return us a list of plots in which each i element is the i-th book's plot pre-processed
def take_plots_pp ( plot_list):

    plot_list_pp = []
    for i in range(0 , len(plot_list)):
        text = plot_list[i]
        result = pre_processing(text)
        plot_list_pp.append(result)


    return plot_list_pp



# Let's map each word in Plots with the respective number that we find in vocabulary
def maps_plot_by_number(plot_list_ , d):
    for plot in plot_list_ :
        for i in range(0,len(plot)):
            word = plot[i]
            #print(word)
            if word in d :
                number = d[word]
                plot[i] = number
                #print(plot[i])

    return plot_list_


#Let's compute our inverted index
def inverted_index(corpus,vocabulary):

    inv_index = defaultdict(list)
    vocabolario = vocabulary
    for word_num in vocabolario :
        for i in range(0,len(corpus)):
            if word_num in corpus[i] :
                inv_index[word_num].append(i)

    return inv_index

def calculate_N(plot_list_pp,words_as_number):
    
    corpus = plot_list_pp
    
    vocabolario = words_as_number

    N_list = []
    for word_num in vocabolario:
        N = 0
        for i in range(0,len(corpus)):
            if word_num in corpus[i]:
                N  = N + 1
        N_list.append(N)

    if len(N_list) == len(vocabolario) :
        
        return N_list
    
    else:
        
        return("problem")
       



#Let's calculate the inverted index with tfidf
def inverted_index_tfidf(plot_list_pp,words_as_number,N_list):
    corpus = plot_list_pp
    n = len(corpus)
    inv_index2 = defaultdict(list)
    vocabolario = words_as_number


    j = 0
    for word_num in vocabolario :

        N = N_list[j] #numbers of document that contain word_num


        for i in range(0,len(corpus)):
            if word_num in corpus[i] :

                #inv_index[word_num].append(i)
                tf = corpus[i].count(word_num)
                tfidf = tf * np.log(n/N)
                #inv_index[word_num].append(tfidf)
                inv_index2[word_num].append((i , tfidf))

        j = j + 1
    
    return inv_index2




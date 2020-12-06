from collections import Counter
import numpy as np
import heapq

def search_engine1(query , d , inv_index):
    
    repetitions = len(query)
    all_documents = np.array([],int)
    
    #For each word of the query, we take the corrispective number and take from inverted index the documents that contain it
    for word in query:
        if word in d:
            number_value = d[word]
            number_value = str(number_value)
            documents = inv_index[number_value]
            documents = np.array(documents)
            all_documents = np.append(all_documents,documents)
            
    #We consider the list of documents as one-d array 
    documents_1d = all_documents.flatten()
    res = Counter(documents_1d)
    
    #we take only the documents that have repetitions == len(query). Those will be our books!
    final_list = np.array([])
    for key, value in res.items():  
        if value == repetitions:
            final_list = np.append(final_list,key) 
    
    #it's a list with the id-books that contains all the query words
    return final_list

#-----------------------------------------------------------------------------------------------------

def search_engine2(query, d , inv_index,inv_index2):
    
    #As starting point we pick the result of first search engine
    final_list = search_engine1(query , d , inv_index)        
    

    q = np.ones(len(query))
    scores =  np.array([])

    for n in final_list :
        lista_tfidf_n = np.array([])

        for word in query:
            if word in d:
                number_value = d[word]
                number_value = str(number_value)
                #for each word happens--> term = (document1, tfIdf_{term,document1})
                document = inv_index2[number_value]
                document = np.array(document)

                for pair in document:
                    if pair[0] == n:
                        tfidf = pair[1] 
                        lista_tfidf_n = np.append(lista_tfidf_n, tfidf)

        #Let's calculate the score for the n-th document and add it to an array
        score =  np.dot(q, lista_tfidf_n)/(np.linalg.norm(q)*np.linalg.norm(lista_tfidf_n))
        scores = np.append(scores, score)


    docu_scores = list(zip(final_list,scores))


    #Let's take the top-k values using an optimized heap data structure
    heapq.heapify(docu_scores)
    top_k = (heapq.nlargest(3, docu_scores,key = lambda x: x[1] ))
    return top_k



#------------------------------------------------------------------------------------------ 

def search_engine3 (characters_list , rating_list, x, final_list) :


    a = range(0,20)
    b = range(20,80)
    c = range(80,300)
    f = range(300,100000000)

    if x == 2:
        numbers_of_ch = []
        for oggetto in characters_list :
            l = len(oggetto)
            if l in a:
                score_character = 1
                numbers_of_ch.append(score_character)
            if l in b:
                score_character = 2
                numbers_of_ch.append(score_character)
            if l in c:
                score_character = 3
                numbers_of_ch.append(score_character)
            if l in f:
                score_character = 4            
                numbers_of_ch.append(score_character)
    elif x == 1  :
        numbers_of_ch = []
        for oggetto in characters_list :
            l = len(oggetto)
            if l in a:
                score_character = 4
                numbers_of_ch.append(score_character)
            if l in b:
                score_character = 3
                numbers_of_ch.append(score_character)
            if l in c:
                score_character = 2
                numbers_of_ch.append(score_character)
            if l in f:
                score_character = 1            
                numbers_of_ch.append(score_character)



    scores = []
    for i in range (0, len(rating_list)) :
        score = numbers_of_ch[i] * rating_list[i]
        scores.append(score)

    docum_scores = list(zip(final_list, scores))
    
    #Let's take the top-k values using an optimized heap data structure
    heapq.heapify(docum_scores)
    top_k = (heapq.nlargest(3, docum_scores, key = lambda x: x[1] ))
    return top_k
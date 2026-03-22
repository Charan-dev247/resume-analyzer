from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
import re



def preprocess(text):
   text = text.lower()
   text = re.sub(r'[^a-zA-Z ]','',text)
   
   words = text.split()
  
   
   return " ".join(words)
   
def calculate_similarity(resume,job_desc):
    resume = preprocess(resume)
    job_desc = preprocess(job_desc)
    
    
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume,job_desc])
    
    score = cosine_similarity(vectors[0:1] , vectors[1:2])
    
    return round(score[0][0] * 100 , 2)




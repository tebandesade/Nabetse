import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities
import sys
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


pags = [] 
file_ = '../data/acuerdofinal.txt'
# pagina se dive por acuerdo fina o pagina 

with open(file_) as arch:
	for line in arch:
		texto = line.strip()
		if not re.match(r'^\s*$', texto):
			print ('test %%%: ', texto)
			pags.append(texto)
no_features =1000
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(pags)

tfidf_feature_names = tfidf_vectorizer.get_feature_names()

print (tfidf_feature_names)

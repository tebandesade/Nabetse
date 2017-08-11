import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#from gensim import corpora, models, similarities
import sys
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import codecs
from sklearn.decomposition import NMF, LatentDirichletAllocation

pags = [] 
file_ = '../data/acuerdofinal.txt'
# pagina se dive por acuerdo fina o pagina 

with codecs.open(file_,"r","utf-8") as arch:
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
print (len(tfidf_feature_names))



tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')

tf = tf_vectorizer.fit_transform(pags) 
tf_feature_names = tf_vectorizer.get_feature_names()

print (tf_feature_names)

no_topics = 20

# Run NMF
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)


print('$$$$$')
# Run LDA
lda = LatentDirichletAllocation(n_topics=no_topics, max_iter=5, learning_method='online', learning_offset=50.,random_state=0).fit(tf)


def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])

no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)
display_topics(lda, tf_feature_names, no_top_words)

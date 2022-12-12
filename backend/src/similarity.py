import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from difflib import SequenceMatcher

#with open(r'C:\Users\Kaio Dias\Desktop\VSCode\EngSoft\texto1.txt', encoding=  "UTF-8") as arq1:
#    t1 = arq1.read()
#
#with open(r'C:\Users\Kaio Dias\Desktop\VSCode\EngSoft\texto2.txt' , encoding=  "UTF-8") as arq2:
#    t2 = arq2.read()

textoBase = "Suponha que esse seja seu texto principal"
textoComparado = "Suponha que esse seja o texto a ser comparado"

#Num NGrams
n = 3

#Instaciar o contador
count = CountVectorizer(analyzer='word', ngram_range=(n, n))

#Cria o dicionário
vocab2Init = count.fit([textoComparado, textoBase]).vocabulary_
similarity = SequenceMatcher(None, textoBase, textoComparado).ratio()

accuracy_score = ()

print(vocab2Init)
print(f" Os textos apresentam similaridade de {round(similarity * 100)}% ")
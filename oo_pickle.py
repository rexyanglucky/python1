#coding=utf8
#pickle 腌制
import pickle
lista=["mingyue","jishi","you"]
dumplista=pickle.dumps(lista)
print dumplista
listc=pickle.loads(dumplista)
print listc
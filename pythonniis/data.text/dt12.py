#write a list in file in binary format
import pickle
numbers=[10,20,30,40,50]
f=open("xyz.data","wb")
pickle.dump(numbers,f)
f.close()
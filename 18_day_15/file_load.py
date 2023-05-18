import pickle

with open("dummy3","rb") as f:
    cnt = pickle.load(f)
    print(cnt)

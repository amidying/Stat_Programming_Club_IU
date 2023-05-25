import pickle

# content = "This is to be pickled"

# with open("pickling2","wb") as f:
#     pickle.dump(content,f)

with open("pickling2","rb") as f:
    print(pickle.load(f))
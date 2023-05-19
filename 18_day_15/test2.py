import pickle

model = "somehting in logistic"

# with open("logistic","wb") as f:
#     pickle.dump(model,f)

with open("logistic","rb") as f:
    content = pickle.load(f)
    print(content)
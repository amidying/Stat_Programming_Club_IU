

text = input("Enter your text: ")
word = input("Enter word to remove: ")

def removeWord(sentence,word):
    sentence = sentence.replace(word,"")
    sentence.strip()
    return sentence
    

print(removeWord(text,word))
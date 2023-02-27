
# def reverse(s):
#     str = ""
#     for i in s:
#         str = i + str
#     return str
#! ei problem e jader somossa skip korteparo
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

text = input("Enter your text: ")

newtext = reverse(text)

print(text == newtext)

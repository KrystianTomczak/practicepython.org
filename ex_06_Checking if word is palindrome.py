import string
word = input("Uer input: ")
translator = str.maketrans("", "", string.punctuation)
word = word.translate(translator)
lst = list()
for i in word:
    if i.startswith(" ") : continue
    i = i.lower()
    lst.append(i)

def rev_slice(lst):
    lst_back = lst[::-1]
    return lst_back

def check():
    if lst == rev_slice(lst):
        return ("Your word is Palindrome.")
    else:
        return ("Unfortunately Your word is not palindrome.")

print(check())
print(lst)
print(rev_slice(lst))
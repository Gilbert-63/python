print("hellow python")
name=input("enter new text")
charac=len(name)
print (charac)
a = name.replace(" ","")
words = []
for i in range (5):
 word = input (f"enter word {i + 1}:")
 words.append(word)
print("length of words entered:")
for word in words:
 print (f" The word '{word}' has {len(word)} characters")
word = input("enter aword")
a=word.replace("A","K")
b=a.replace("I","J")
c=b.replace("O","P")
d=c.replace("E","T")
e=d.replace("U","F")
print(e)
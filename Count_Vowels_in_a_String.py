a=input("Enter word or sentence: ")
count=0
for i in range(len(a)):
    if a[i] in ["a", "i", "e", "o", "u", "A","E","I","O","U"]:
        count=count+1
        i=i+1
print(count)
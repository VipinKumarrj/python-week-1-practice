num=int(input("Enter Number: "))
i=2
while i<num:
    if num%i==0:
        print("It is not Prime number ")
        break
    i=i+1
else:
    print("It is Prime number ")
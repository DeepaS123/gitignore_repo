name =  str(input("Enter a Name: "))
index = 0
for char in name:
    print("character ",char," has +ve index of ",index,"and -ve index of ", index - len(name))
    index +=1
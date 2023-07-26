#Assignment No : 8

print("--MENU--")
print("1.String Swap Case")
print("2.String Length")
print("3.String Uppercase")
print("4.String Lowercase")
print("5.String Indexing")
print("6.String Slicing")
print("7.Exit")

while(True):
        i = int(input("Enter your choice : "))
        if i ==1:
                s1 = input("Enter String ")
                print("String Swap Case",s1.swapcase())
        elif i == 2:
                s1 = input("Enter String to find its length ")
                print("Length of string is ",len(s1))
        elif i == 3:
                s1 = input("Enter String in lowercase")
                print("Upper case string ",s1.upper())
        elif i == 4:
                s1 = input("Enter String in Uppercase")
                print("Lower case string ",s1.lower())
        elif i == 5:
                s1 = input("Enter string for indexing")
                pos = int(input("Enter position to extract"))
                print("Character at position ", pos,"is",s1[pos])
        elif i == 6:
                s1 = input("Enter String for slicing")
                start = int(input("Enter starting position to extract"))
                end = int(input("Enter ending position for extract"))
                print("Sliced String is ",s1[start:end])
        elif i == 7:
                break
        else:
                print("Invalid Choice")
        
                           

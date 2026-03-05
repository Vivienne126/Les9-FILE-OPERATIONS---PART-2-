with open("1.txt" , "w") as file:
    file.write("Hello!!!  , How are you \n I am good")
file.close() 

with open("1.txt" , "r") as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)

file.close()


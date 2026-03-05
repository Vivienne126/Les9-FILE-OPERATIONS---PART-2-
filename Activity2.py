# new_file=open("New.txt" , "x")
# new_file.close()

#Check if a file exists
import os
if os.path.exists("New.txt"):
    os.remove("New.txt")

else:
    print("The file does not exist")

my_file=open("new.txt" , "w")
my_file.write("Apple , Banana , Mango")
my_file.close()


# os.remove("1.txt")

os.rmdir("my_folder")
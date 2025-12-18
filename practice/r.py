f= open(r"C:\Users\Sanskriti\Desktop\AIML\day7\sample.txt", "r+") #file object we can think of it as a file object
#here i've added r before the path

f.write("123")
print(f.read())

f.close()

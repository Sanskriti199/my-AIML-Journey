f= open(r"C:\Users\Sanskriti\Desktop\AIML\day7\sample.txt", "r") #file object we can think of it as a file object
#here i've added r before the path
'''data=f.read()'''
data=f.readline()
print(data)

data=f.readline()
print(data)

f.close()

# when we are reading line by line
#the pointer is moving frrom the start to the end of the line

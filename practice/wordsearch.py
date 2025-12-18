data =True
line=1
word="python"

with open(r"C:\Users\Sanskriti\Desktop\AIML\day7\sample.txt", "r") as f:
    while data:
        data=f.readline()
        if(word in data):
            print(f"{word} found in {line}")
            break
        print(data) 
        line+=1
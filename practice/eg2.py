username=input("enter a username:")
password=input("enter a password:")

if (username=="admin" and password=="pass"):
    print("login successful")
elif (username!="admin"):
    print("enter correct username")
elif (password!="pass"):
    print("enter correct password")
else:
    print("enter correct details")
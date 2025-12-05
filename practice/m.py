color=input("enter a color:")

match color:
    case "Green":
        print("go")
    case "yellow":
        print("look")
    case "red":
        print("stop")
    case _:
        print("default")
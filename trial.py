import pyshorteners as sh


link = input("This is a link shortner(just add the link)")
website = input("This is link for : ")
store_or_not = input("Do you want ot store it [y/n]: ")
shortner = sh.Shortener()
x = (shortner.tinyurl.short(link))

print(x)


def TextFile():
    file = open("C:\\Users\\aaran\\OneDrive\\Desktop\\link.txt" , "a")

    file.write(x)
    file.write(f"({website})")
    file.write(''"\n")
    file.close()

    file = open("C:\\Users\\aaran\\OneDrive\\Desktop\\link.txt", "r")
    file.read()
if store_or_not == "y":
    TextFile()
    pass
else:
    print("Ok No problem ")
    pass





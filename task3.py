def main():
    myfile = open ("names.txt", "r")
    names = myfile.readlines()
    names.sort()
    print(names)
    myfile.close()
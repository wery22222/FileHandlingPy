def main():
    while True:
        myfile = open ("variable.txt", "a")
        name = input("name")
        if name == "quit":
            break
        age = input("score")
        myfile.write(f"{name}, {age} \n")
        myfile.close()
main()
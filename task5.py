def main():
    myfile = open ("variable.txt", "a")
    name = input("name")
    age = input("age")
    myfile.write(f"{name}, {age} \n")
    myfile.close()
main()
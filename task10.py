def main():
    list_of_subjects = open("subjects.txt", "r").readlines()
    list_of_subjects.sort()
    print(list_of_subjects)
    open("subjects.txt", "w").write("")
    for i in list_of_subjects:
        open("subjects.txt", "a").write(i)


main()
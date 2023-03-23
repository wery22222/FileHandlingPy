def main():
    myfile = open ("variable.txt", "w")
    score = input("score")
    myfile.write(score)
    myfile.write('\n')
    myfile.close()
main()
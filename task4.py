def main():
    myfile = open ("variable.txt", "a")
    highscore = int(input("score"))
    myfile.writestr(highscore)
    myfile.write('\n')
    myfile.close()
main()
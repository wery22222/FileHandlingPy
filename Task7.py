def main():
    scores = []
    text_file = open("scores.txt", "r")
    for i in text_file:
        scores.append(int(i.strip()))
    text_file.close()
    scores.sort(reverse=True)
    print(scores)
main()
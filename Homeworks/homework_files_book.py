with open("homework.txt", "r", encoding="UTF8") as file:
    data = file.read().split(" ")
    data = [(item.replace(",", "").replace(".", "").replace("!", "").replace("?", "").lower()) for item in data]
    data2 = set(data)
    print("Number of words in data file is:", len(data))
    print("Number of unique words in data file is:", len(data2))
    # with open("homework_files_book_result.txt", "w", encoding="UTF8") as file:
    #        data3 = ("The number of words in data file is:", len(data), "The number  of unique words in data file is:", len(data2))
    #        file.write(str(data3))
    with open("homework_files_book_result.txt", "w", encoding="UTF8") as file:
        file.write("There are " + str(len(data)) + " words in text file.\n")
        file.write("There are " + str(len(set(data))) + " unique words in text file.")

# I had to use .lower as well, because he might count same words twice








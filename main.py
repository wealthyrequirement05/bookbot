with open("C:\\Users\\Astro Bullivant\\PycharmProjects\\For GitHub\\bookbot\\bookbot\\books\\frankenstein.txt", "r") as f:
    file_contents = f.read()
    word_list = file_contents.split()
    num_words = len(word_list)

    file_contents_lower_string = file_contents.lower()
    file_contents_lower = []
    file_contents_lower[:] = file_contents_lower_string
    counts = []
    char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'
                 , 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #letter_count = {character: file_contents_lower.count(character) for character in file_contents_lower}
    letter_count = {}
    for char in char_list:
        letter_count[char] = file_contents_lower.count(char)
        counts.append(file_contents_lower.count(char))
    #print(letter_count)
    letter_count_list = list(letter_count.items())
    #print(letter_count_list)
    #sorted_letter_count_list = letter_count_list.sort()
    sorted_letters = []
    counts.sort(reverse=True)
    sorted_list = []

    sorted_letter_count_list = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    sorted_letter_count = dict(sorted_letter_count_list)

    #print(sorted_letter_count_list)

    print("--- Begin report of books/frankenstein.txt ---")
    print(str(num_words) + " words found in the document")
    print(" ")

    for i in sorted_letter_count_list:
        print("The " + i[0] + " character was found " + str(i[1]) +" times")
    print("--- End report ---")
    #print(letter_count_list.sort())
    #for char_count in sorted_letter_count_list:
    #    print(char_count)
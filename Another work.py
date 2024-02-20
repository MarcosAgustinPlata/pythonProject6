file_name = "4-file.txt"

try:

    with open(file_name, 'r') as fd:
        print("Here are the contents of the file:\n")


        for line in fd:
            print(line, end='')


    print("\nHere are the 3 letter words:")
    with open(file_name, 'r') as fd:
        for line in fd:
            words = line.split()  # Dividir la línea en palabras basándose en espacios.
            for word in words:
                if len(word) == 3:
                    print(word)

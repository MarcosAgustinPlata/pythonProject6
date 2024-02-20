file_name = "x-file.txt"

fd = open(file_name, "w")

while True:
    line = input("Ingrese una línea de texto (deje en blanco para terminar): ")
    if line:

        fd.write(line + "\n")
    else:

        break

fd.close()



def main():
    f = open("program.txt", "r")
    contents = f.read()
    for index in contents:
        if (index == " "):
            print("espacio")
        if (index == "\n"):
            print("espacio doble")
        if index.isdigit():
            index = int(index)

        print(type(index), " - ", index)


if __name__ == '__main__':
    main()

def main():
    # transition_table = [["1", "2", "3"],
    #                     [-5, 8, 9]]

    list = [{"letra": 1, "digit": 3, " ": 0, "/n": 0},
            {"letra": 1, "digit": 1, "other": 2, " ": 2, "/n": 2},
            {"letra": 3, "digit": 3, "other": 3},
            {"letra": 3, "digit": 3, "other": 3}]
    list_tokens = []

    f = open("program.txt", "r")
    text = f.read()
    state = 0
    index = 0
    token = ""
    error_token = 2
    while index <= len(text):
        if state != 2 and state != 3:
            if (text[index] == " "):
                print("espacio")
            if (text[index] == "\n"):
                print("espacio doble")
            if text[index].isalpha():
                state = list[state]["letra"]
                print("letra ", state, " - ", text[index])
                token += text[index]
            elif text[index].isdigit():
                state = list[state]["digit"]
                print("digit ", state, " - ", text[index])
                token += text[index]
            else:
                state = list[state][text[index]]
                print("other ", state, " - ", text[index])
        elif state == 2:
            print("AÑADIDO A LA LISTA - ", token)
            list_tokens.append(token)
            token = ""
            state = 0
            if index != len(text):
                index = index - 1
        elif state == 3:
            print("Error - ", token)
            index = len(text)+1
        print("----------", index)
        index += 1


if __name__ == '__main__':
    main()

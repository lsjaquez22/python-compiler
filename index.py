def main():

    transition_table = [{"letra": 1, "digit": 3, " ": 0, "\n": 0},
                        {"letra": 1, "digit": 1, " ": 2, "\n": 2},
                        {},
                        {}]
    list_tokens = []

    f = open("program.txt", "r")
    text = f.read()
    state = 0
    index = 0
    token = ""
    error_token = ""
    while index <= len(text):
        if state != 2 and state != 3:
            if (text[index] == " "):
                print("espacio")
            if (text[index] == "\n"):
                print("espacio doble")
            if text[index].isalpha():
                state = transition_table[state]["letra"]
                print("letra ", state, " - ", text[index])
                token += text[index]
            elif text[index].isdigit():
                state = transition_table[state]["digit"]
                print("digit ", state, " - ", text[index])
                token += text[index]
            else:
                state = transition_table[state][text[index]]
                print("other ", state, " - ", text[index])
        elif state == 2:
            print("AÑADIDO A LA LISTA de TOKENS - ", token)
            print("STATE = 0")
            list_tokens.append(token)
            token = ""
            state = 0
            if index != len(text):
                index = index - 1
        elif state == 3:
            error_token += token
            while text[index] != " " and text[index] != "\n":
                error_token += text[index]
                index += 1
            print("Error - Invalid Token", error_token)
            index = len(text)+1
        print("----------", index)
        index += 1


if __name__ == '__main__':
    main()

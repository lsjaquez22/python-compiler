def main():

    transition_table = [{"letra": 1, "digit": 2, " ": 3, "\n": 3, ";": 3},
                        {"letra": 1, "digit": 1, " ": 3, "\n": 3, ";": 3},
                        {"letra": 4, "digit": 2, " ": 3, "\n": 3, ";": 3},
                        {},
                        {}]
    list_tokens = []

    f = open("program.txt", "r")
    text = f.read()
    text += " "
    state = 0
    index = 0
    token = ""
    error_token = ""
    while index < len(text):
        if state != 3 and state != 4:
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

        if state == 3:
            if token != "":
                print("AÑADIDO A LA LISTA de TOKENS - ",
                      token, " - ", len(token))
                print("STATE = 0")
                list_tokens.append(token)
            if text[index] != " " and text[index] != "\n":
                print("DELIMITER ", state, " - ", text[index])
                list_tokens.append(text[index])
            token = ""
            state = 0

        if state == 4:
            error_token += token
            while text[index] != " " and text[index] != "\n":
                error_token += text[index]
                index += 1
            print("Error - Invalid Token", error_token)
            index = len(text)+1
        print("----------", index)
        index += 1
    print(list_tokens)


if __name__ == '__main__':
    main()

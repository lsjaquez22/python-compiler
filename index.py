def main():

    transition_table = [{"letra": 1, "digit": 2, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 1, "digit": 4, " ": 3,
                            "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 4, "digit": 2, " ": 3,
                            "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {},
                        {},
                        {}]
    list_tokens = []

    reserved_words = ["if", "else", "int", "return",
                      "void", "while", "input", "output"]

    f = open("program.txt", "r")
    text = f.read()
    text += " "
    state = 0
    index = 0
    token = ""
    delimitador = ""
    error_token = ""
    print(len(text))
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
                if token in reserved_words:
                    print("PALABRA RESERVADA ENCONTRADA")
                print("AÑADIDO A LA LISTA de TOKENS - ",
                      token, " - ", len(token))
                print("STATE = 0")
                list_tokens.append(token)
            delimitador = text[index]
            if delimitador != " " and delimitador != "\n" and delimitador != "!":
                if delimitador == "<" and text[index + 1] == "=":
                    delimitador += "="
                    index += 1
                if delimitador == ">" and text[index + 1] == "=":
                    delimitador += "="
                    index += 1
                if delimitador == "=" and text[index + 1] == "=":
                    delimitador += "="
                    index += 1
                if delimitador == "/" and text[index + 1] == "*":
                    # print("FOUND COMMENT ", delimitador,
                    #       " - ", text[index + 1])
                    delimitador += "*"
                    index += 3
                    found = False

                    while index < len(text) and found == False:
                        if text[index] == "/":
                            if text[index - 1] == "*":
                                print("Valor - ", text[index],
                                      " - ", text[index - 1])
                                found = True
                                index -= 1
                        else:
                            print("Valor - ", text[index], " - ", index)

                        index += 1
                print("DELIMITER ", state, " - ", delimitador)
                list_tokens.append(delimitador)

            token = ""
            state = 0
            if delimitador == "!" and text[index + 1] == "=":
                delimitador += "="
                index += 1
                print("DELIMITER ", state, " - ", delimitador)
                list_tokens.append(delimitador)
            elif delimitador == "!" and delimitador != "=":
                state = 5

        if state == 4:
            error_token += token
            while text[index+1] != " " and text[index+1] != "\n":
                error_token += text[index+1]
                index += 1
            print("------- Error ------- Invalid Token", error_token)
            index = len(text) + 1
        if state == 5:
            delimitador = text[index]
            while text[index+1] != " " and text[index+1] != "\n":
                delimitador += text[index+1]
                index += 1
            print("------- Error ------- Delimitador Invalido", delimitador)
            index = len(text) + 1
        print("----------", index)
        index += 1
    print(list_tokens)


if __name__ == '__main__':
    main()

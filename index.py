def main():

    transition_table = [{"letra": 1, "digit": 2, " ": 11, "\n": 11, ";": 11, ",": 11, "+": 11, "-": 11, "*": 11, "/": 4, "<": 14, ">": 16, "=": 8, "(": 11, ")": 11, "{": 11, "}": 11, "[": 11, "]": 11, "!": 12},
                        {"letra": 1, "digit": 7, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                            "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 7, "digit": 2, " ": 3,
                            "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {},
                        {"letra": 10, "digit": 10, " ": 10, "\n": 10, ";": 10, ",": 10, "+": 10, "-": 10, "*": 5, "/": 10,
                            "<": 10, ">": 10, "=": 10, "(": 10, ")": 10, "{": 10, "}": 10, "[": 10, "]": 10, "!": 10},
                        {"letra": 5, "digit": 5, " ": 5, "\n": 5, ";": 5, ",": 5, "+": 5, "-": 5, "*": 6, "/": 5,
                            "<": 5, ">": 5, "=": 5, "(": 5, ")": 5, "{": 5, "}": 5, "[": 5, "]": 5, "!": 5},
                        {"letra": 6, "digit": 6, " ": 6, "\n": 6, ";": 6, ",": 6, "+": 6, "-": 6, "*": 6,
                            "/": 18, "<": 6, ">": 6, "=": 6, "(": 6, ")": 6, "{": 6, "}": 6, "[": 6, "]": 6, "!": 6},
                        {},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                            "<": 3, ">": 3, "=": 9, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                         "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {},
                        {},
                        {"letra": 7, "digit": 7, " ": 7, "\n": 7, ";": 7, ",": 7, "+": 7, "-": 7, "*": 7, "/": 7,
                            "<": 7, ">": 7, "=": 13, "(": 7, ")": 7, "{": 7, "}": 7, "[": 7, "]": 7, "!": 7},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                         "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                            "<": 3, ">": 3, "=": 15, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                         "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                            "<": 3, ">": 3, "=": 17, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 3,
                         "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3}]
    list_tokens = []

    reserved_words = ["if", "else", "int", "return",
                      "void", "while", "input", "output"]

    data = {"status": 0, "message": "se leyeron los tokens de forma correcta"}

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
        if state != 3 and state != 7:

            if text[index].isalpha():
                state = transition_table[state]["letra"]
                print("letra ", state, " - ", text[index])
                token += text[index]
            elif text[index].isdigit():
                state = transition_table[state]["digit"]
                print("digit ", state, " - ", text[index])
                token += text[index]
            else:
                print("other ", state, " - ", text[index])
                state = transition_table[state][text[index]]
                token += text[index]

        if state == 3:
            token = token[:-1]
            index = index-1
            print("TOKEN ENCONTRADO - ", token)
            if token.isalpha():
                if token in reserved_words:
                    print("Palabra reservada encontrada")
                    new_token = {"tipo": token, "value": None}
                    list_tokens.append(new_token)
                else:
                    new_token = {"tipo": "identifier", "value": token}
                    list_tokens.append(new_token)
            elif token != " " and token != "\n":
                if token.isdigit():
                    new_token = {"tipo": "number", "value": token}
                    list_tokens.append(new_token)
                else:
                    new_token = {"tipo": "symbol", "value": token}
                    list_tokens.append(new_token)
            token = ""
            state = 0
        if state == 10:
            token = token[:-1]
            print("TOKEN ENCONTRADO 10 - ", token)
            if token != " " and token != "\n":
                new_token = {"tipo": "symbol", "value": token}
                list_tokens.append(new_token)
            token = ""
            state = 0
            index = index-1
        if state == 11:
            print("TOKEN ENCONTRADO 11 - ", token)
            if token != " " and token != "\n":
                new_token = {"tipo": "symbol", "value": token}
                list_tokens.append(new_token)
            token = ""
            state = 0

        if state == 7:
            data["status"] = 1
            data["message"] = ("token incorrecto - --- ", token)
            print("--------ERROR------ token incorrecto ---- ", token)
            index = len(text)

        if state == 18:
            print("Comentario encontrado")
            token = ""
            state = 0
        print("----------", index, "----------", state)
        index += 1
    if state == 5 or state == 6:
        data["status"] = 2
        data["message"] = "Commentario sin cerradura ----"
        print("--------ERROR------ Commentario sin cerradura ---- ")

    for element in list_tokens:
        print(element)


if __name__ == '__main__':
    main()

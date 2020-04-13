def main():

    transition_table = [{"letra": 1, "digit": 2, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 6, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 1, "digit": 4, " ": 3,
                            "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 6, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {"letra": 4, "digit": 2, " ": 3,
                            "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 6, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {},
                        {},
                        {},
                        {"letra": 3, "digit": 3, " ": 3, "\n": 3, ";": 3, ",": 3, "+": 3, "-": 3, "*": 3, "/": 6, "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3}]
    list_tokens = []

    symbol_table_identifiers = []
    symbol_table_numbers = []
    reserved_words = ["if", "else", "int", "return",
                      "void", "while", "input", "output"]

    data = {"status": 0, "message": "Tokens Generados Correctamente"}

    f = open("program.txt", "r")
    text = f.read()
    text += " "
    state = 0
    index = 0
    token = ""
    delimitador = ""
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

        if state == 6:
            delimitador = text[index]
            if delimitador == "/" and text[index + 1] != "*":
                new_token = {"tipo": "delimitador", "value": delimitador}
                list_tokens.append(new_token)
                index += 1
                state = 3
            elif delimitador == "/" and text[index + 1] == "*":
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
                        print("Valor Comment/Index - ",
                              text[index], " - ", index)

                    index += 1
                if found == False:
                    state = 7
                elif found == True:
                    index += 1
                    state = 3

        if state == 3:
            if token != "":

                if token in reserved_words:
                    print("PALABRA RESERVADA ENCONTRADA - ", token)
                    new_token = {"tipo": token, "value": None}
                    list_tokens.append(new_token)
                else:
                    print("AÑADIDO A LA LISTA de TOKENS - ",
                          token, " - ", len(token))
                    if token.isalpha():
                        symbol_table_identifiers.append({"lexema": token})
                        new_token = {"tipo": "identifier",
                                     "value": len(symbol_table_identifiers)-1}
                    elif token.isdigit():
                        symbol_table_numbers.append({"lexema": token})
                        new_token = {"tipo": "number", "value": len(
                            symbol_table_numbers)-1}
                    list_tokens.append(new_token)
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
                print("DELIMITER ", state, " - ", delimitador)
                new_token = {"tipo": "delimitador", "value": delimitador}
                list_tokens.append(new_token)

            token = ""
            state = 0
            if delimitador == "!" and text[index + 1] == "=":
                delimitador += "="
                index += 1
                print("DELIMITER ", state, " - ", delimitador)
                new_token = {"tipo": "delimitador", "value": delimitador}
                list_tokens.append(new_token)
            elif delimitador == "!" and delimitador != "=":
                state = 5

        if state == 4:
            error_token += token
            while text[index+1] != " " and text[index+1] != "\n":
                error_token += text[index+1]
                index += 1
            data["status"] = 1
            data["message"] = "------- Error ------- Invalid Token", error_token
            # print("------- Error ------- Invalid Token", error_token)
            index = len(text) + 1

        if state == 5:
            delimitador = text[index]
            while text[index+1] != " " and text[index+1] != "\n":
                delimitador += text[index+1]
                index += 1
            data["status"] = 2
            data["message"] = "------- Error ------- Caracter espacial Invalido", delimitador
            # print("------- Error ------- Caracter espacial Invalido", delimitador)
            index = len(text) + 1

        if state == 7:
            data["status"] = 3
            data["message"] = "------- Error ------- No se encontro cerraduda de Comentario", delimitador
            # print(
            #     "------- Error ------- No se encontro cerraduda de Comentario", delimitador)
            index = len(text) + 1

        print("----------", index)
        index += 1

    if (data["status"] == 0):
        data["list_tokens"] = list_tokens
        data["list_identifiers"] = symbol_table_identifiers
        data["list_numbers"] = symbol_table_numbers
        print("\n")
        print("Status - ", data["status"])
        print("\n")
        print("Mensaje - ", data["message"])
        print("\n")
        print("LISTA DE TOKENS")
        for element in data["list_tokens"]:
            print(element)
        print("\n")
        print("LISTA DE IDENTIFICADORES")
        for element in data["list_identifiers"]:
            print(element)
        print("\n")
        print("LISTA DE NUMEROS")
        for element in data["list_numbers"]:
            print(element)
        print("\n")
    else:
        print("\n")
        print("Status - ", data["status"])
        print("\n")
        print("Mensaje - ", data["message"])
        print("\n")
    data


if __name__ == '__main__':
    main()

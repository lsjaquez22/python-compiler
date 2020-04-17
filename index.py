# los comentarios que inicien con dev, serviran para el desarrollador
# muestran el flujo que sigue el programa al ir leyendo cada caracter


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
                         "<": 3, ">": 3, "=": 3, "(": 3, ")": 3, "{": 3, "}": 3, "[": 3, "]": 3, "!": 3},
                        {}]
    list_tokens = []

    symbol_table_identifiers = []
    symbol_table_numbers = []
    reserved_words = ["if", "else", "int", "return",
                      "void", "while", "input", "output"]

    # El objeto que se regresara al final de la funcion
    # Se le agregaran propiedades en caso de seguir con status 0
    data = {"status": 0, "message": "se leyeron los tokens de forma correcta"}
    symbol_table_identifiers = []
    symbol_table_numbers = []

    # Path del archivo fuente para leer
    f = open("program.txt", "r")
    text = f.read()
    # Se le agrega un espacio al final del codigo para tener un ultimo delimitador
    text += " "
    # estado en el que va a empezar a buscar dentro de la tabla de transiciones - tabla[0]
    state = 0
    # posicion del caracter que va leyendo dentro del archivo fuente
    index = 0
    # Token al cual se le va a ir agregando los caracteres encontrados
    token = ""

    # ciclo que recorre todo el archivo
    # va hasta len-1 para no caer en out of range
    while index < len(text):

        # estados de error o aceptacion
        # entra cuando el estado es diferenete a alguno de estos
        if state != 3 and state != 7 and state != 10 and state != 11 and state != 18:

            # entra cuando el caracter leido es una letra
            if text[index].isalpha():
                state = transition_table[state]["letra"]
                # dev print("letra ", state, " - ", text[index])
                token += text[index]
            # entra cuando el caracter leido es un numero
            elif text[index].isdigit():
                state = transition_table[state]["digit"]
                # dev print("digit ", state, " - ", text[index])
                token += text[index]
            # entra cuando el caracter leido es un simbolo
            else:
                # dev print("other ", state, " - ", text[index])
                state = transition_table[state][text[index]]
                token += text[index]

        # primer estado de aceptacion, encontro un token de palabra, numero o de mas de 2 simbolos
        if state == 3:
            # se elimia el ultimo elemento del token ya que este marco el final del token y no pertenece
            token = token[:-1]
            # se regresa una posicion para leer el token eliminado
            index = index-1
            # dev print("TOKEN ENCONTRADO - ", token)
            # entra cuando el token es una palara
            if token.isalpha():
                # revisa si el token es igual a alguna palabra reservada
                if token in reserved_words:
                    # la palabra reservada se agrega unicamente a la lista de token y no a las tablas de simbolos
                    # dev print("Palabra reservada encontrada")
                    new_token = {"tipo": token, "value": None}
                    list_tokens.append(new_token)
                else:
                    # significa que el token no es palabra resevada
                    # variable para verificar si el token ya fue añadido a la tabla de simbolos anteriormente
                    found = False
                    # variable para recorrer la lista de tabla de simbolos, sirve como referencia a las posiciones 0,1,...
                    pos = 0
                    # variable para guardar posicion del token si existe en la tabla de simbolos
                    index_found_element = 0
                    for element in symbol_table_identifiers:
                        # compara las palabras en la tabla con el token encontrado
                        if element["lexema"] == token:
                            # al encontrado guardamos su posicion en la variable
                            index_found_element = pos
                            # cambiamos nuestra bandera de que si lo encontramos
                            found = True
                        # se va recorriendo el arreglo
                        pos += 1
                    if found == False:
                        # si no existe el token en la tabla se agrega como nuevo token a la lista y a su respectiva tabla
                        symbol_table_identifiers.append({"lexema": token})
                        new_token = {"tipo": "identifier",
                                     "value": len(symbol_table_identifiers)-1}
                        list_tokens.append(new_token)
                    else:
                        # si fue encontrado en la tabla se crea el token y se hace referencia a la posicion en la tabla donde esta guardado
                        new_token = {"tipo": "identifier",
                                     "value": index_found_element}
                        list_tokens.append(new_token)
            # los espacios y los saltos de linea son ignorados
            elif token != " " and token != "\n":
                # si el token es un numero se crea el token y se agrega a su tabla y a la lista
                if token.isdigit():
                    symbol_table_numbers.append({"lexema": token})
                    new_token = {"tipo": "number",
                                 "value": len(symbol_table_numbers)-1}
                    list_tokens.append(new_token)
                else:
                    # si el token es un simbolo se agrega unicamente a la lista de tokens
                    new_token = {"tipo": "symbol", "value": token}
                    list_tokens.append(new_token)
            # al encontrar un toke, su variable se vacia
            token = ""
            # el estado vuelvo a 0 para volver a identificar un nuevo token
            state = 0

        # estado para validar simbolos de 2 o mas caracteres
        if state == 10:
            token = token[:-1]
            # dev print("TOKEN ENCONTRADO 10 - ", token)
            if token != " " and token != "\n":
                new_token = {"tipo": "symbol", "value": token}
                list_tokens.append(new_token)
            token = ""
            state = 0
            index = index - 1

        # estado para validar simbolos de un solo caracter
        if state == 11:
            # aqui no se borra el ultimo caracter del token ni se regresa una posicion
            # esto es porque el token funciona como su mismo delimitador
            # dev print("TOKEN ENCONTRADO 11 - ", token)
            if token != " " and token != "\n":
                new_token = {"tipo": "symbol", "value": token}
                list_tokens.append(new_token)
            token = ""
            state = 0

        # estado de error al encontrar algun token invalido
        if state == 7:
            # se cambia el status del porgrama a 1, que significa error
            data["status"] = 1
            # mensaje que explique el error detectado
            data["message"] = ("token incorrecto ---- ", token)
            # se incremente index hasta el final del archivo para terminar con el ciclo
            index = len(text)

        # estado para detectar los comentario
        if state == 18:
            # dev print("Comentario encontrado")
            token = ""
            state = 0
        # dev print("----------", index, "----------", state)

        # aumento para leer el sigueinte caracter en el archivo
        index += 1

    # verifica si al terminar de leer el archivo no se quedo buscando el simbolo de cierre del comentario
    if state == 5 or state == 6:
        # cambia a estatus 2, que significa que un comentario no tiene cerradura
        data["status"] = 2
        data["message"] = "Commentario sin cerradura ----"

    if (data["status"] == 0):
        # al terminar de forma correcta, se agregan las tablas y la lista  la variable data
        data["list_tokens"] = list_tokens
        data["list_identifiers"] = symbol_table_identifiers
        data["list_numbers"] = symbol_table_numbers
        print("\n")
        print("Status - ", data["status"])
        print("\n")
        print("Message - ", data["message"])
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


if __name__ == '__main__':
    main()

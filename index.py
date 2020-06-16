# los comentarios que inicien con dev, serviran para el desarrollador
# muestran el flujo que sigue el programa al ir leyendo cada caracter


def analizados_lexico():

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
    f = open("program_2.txt", "r")
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

        if state == 5:
            # Estado para manejar los comentarios
            index += 1
            # Se va leyendo hasta que se encuentra el simbolo de cierre del comentario
            while text[index] != "/" or text[index - 1] != "*":
                # en caso de que se lea todo el archivo sin encontrar el simbolo
                # se hace un break para salir del while
                if index == len(text) - 1:
                    break
                # se recorre el index para leer el siguiente caracter
                index += 1
            # si encontro el simbolo de cierre
            # se borra el token y se reinicia el valor del state = 0
            if index != len(text) - 1:
                token = ""
                state = 0

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
        # agregar symbolo de final de programa $
        list_tokens.append({"tipo": "$", "value": None})
        # al terminar de forma correcta, se agregan las tablas y la lista  la variable data
        data["list_tokens"] = list_tokens
        data["list_identifiers"] = symbol_table_identifiers
        data["list_numbers"] = symbol_table_numbers

    return data


def analizados_sintactico(list_tokens):

    global index
    global current_token
    index = 0
    current_token = list_tokens[index]

    def declaration_list():
        if (current_token["tipo"] == "int"):
            print("declaration_list  -  igual int")
            match_tipo("int")
            match_tipo("identifier")
            declaration()
            declaration_list_prime()

        elif (current_token["tipo"] == "void"):
            print("declaration_list  -  igual void")
            match_tipo("void")
            match_tipo("identifier")
            match_value("(")
            params_list()
            match_value(")")
            compound_stmt_void()
            declaration_list_prime()

        else:
            print("-----ERROR_DECLARATION_LIST--------")
            return

    def declaration_list_prime():
        if (current_token["tipo"] == "int"):
            print("declaration_list_prime  -  igual int")
            match_tipo("int")
            match_tipo("identifier")
            declaration()
            declaration_list_prime()

        elif (current_token["tipo"] == "void"):
            print("declaration_list_prime  -  igual void")
            match_tipo("void")
            match_tipo("identifier")
            match_value("(")
            params_list()
            match_value(")")
            compound_stmt_void()
            declaration_list_prime()

        elif (current_token["tipo"] == "$"):
            print("-----FIN_PROGRAMA--------")
            return

        else:
            print("-----ERROR_DECLARATION_LIST_PRIME--------")
            return

    def declaration():
        if (current_token["value"] == "("):
            print("declaration  -  igual (")
            match_value("(")
            params_list()
            match_value(")")
            compound_stmt_int_return()
        else:
            var_array_declaration()
            match_value(";")

    def var_array_declaration():
        if (current_token["value"] == "["):
            print("var_array_declaration  -  igual [")
            match_value("[")
            match_tipo("number")
            match_value("]")
        elif (current_token["value"] == ";"):
            return
        else:
            print("-----ERROR_VAR_ARRAY_DECLARATION--------")
            return

    def params_list():
        if (current_token["tipo"] == "int"):
            print("params_list  -  igual int")
            match_tipo("int")
            match_tipo("identifier")
            param_array()
            params_list_prime()
        elif (current_token["tipo"] == "void"):
            print("params_list  -  igual void")
            match_tipo("void")
        else:
            print("-----ERROR_PARAMS_LIST--------")
            return

    def params_list_prime():
        if (current_token["value"] == ","):
            print("params_list_prime  -  igual ,")
            match_value(",")
            match_tipo("int")
            match_tipo("identifier")
            param_array()
            params_list_prime()
        elif (current_token["value"] == ")"):
            return
        else:
            print("-----ERROR params_list_prime--------")
            return

    def param_array():
        if (current_token["value"] == "["):
            print("param_array  -  igual ,")
            match_value("[")
            match_value("]")
        elif (current_token["value"] == "," or current_token["value"] == ")"):
            return
        else:
            print("-----ERROR param_array--------")
            return

    def compound_stmt_void():
        if (current_token["value"] == "{"):
            print("compound_stmt_void  -  igual {")
            match_value("{")
            local_declarations()
            statement_list_void()
            match_value("}")
        else:
            print("-----ERROR compound_stmt_void--------")
            return

    def compound_stmt_int_return():
        if (current_token["value"] == "{"):
            print("compound_stmt_int_return  -  igual {")
            match_value("{")
            local_declarations()
            statement_list_int()
            return_stmt_int()
            match_value("}")
        else:
            print("-----ERROR compound_stmt_int_return--------")
            return

    def compound_stmt_int_no_return():
        if (current_token["value"] == "{"):
            print("compound_stmt_int_no_return  -  igual {")
            match_value("{")
            local_declarations()
            statement_list_int()
            match_value("}")
        else:
            print("-----ERROR compound_stmt_int_no_return--------")
            return

    def local_declarations():
        if (current_token["tipo"] == "int"):
            print("local_declarations  -  igual int")
            match_tipo("int")
            match_tipo("identifier")
            var_array_declaration()
            match_value(";")
            local_declarations()
        elif (current_token["value"] == "{"
              or current_token["value"] == "}"
              or current_token["tipo"] == "identifier"
              or current_token["tipo"] == "if"
              or current_token["tipo"] == "while"
              or current_token["tipo"] == "input"
              or current_token["tipo"] == "output"
              or current_token["tipo"] == "return"):
            return
        else:
            print("-----ERROR local_declarations--------")
            return

    def statement_list_void():
        if (current_token["value"] == "{"
            or current_token["tipo"] == "identifier"
            or current_token["tipo"] == "if"
            or current_token["tipo"] == "while"
            or current_token["tipo"] == "input"
                or current_token["tipo"] == "output"):
            print("statement_list_void")
            statement_void()
            statement_list_void()
        elif (current_token["value"] == "}"):
            return
        else:
            print("-----ERROR statement_list_void--------")
            return

    def statement_list_int():
        if (current_token["value"] == "{"
            or current_token["tipo"] == "identifier"
            or current_token["tipo"] == "if"
            or current_token["tipo"] == "while"
            # or current_token["tipo"] == "return"
            or current_token["tipo"] == "input"
                or current_token["tipo"] == "output"):
            print("statement_list_int")
            statement_int()
            print("regresa statement_list_int")
            statement_list_int()
        elif (current_token["tipo"] == "return"):
            print("sale de statement_list_int")
            return
        else:
            print("-----ERROR statement_list_int--------")
            return

    def statement_void():
        if (current_token["tipo"] == "identifier"):
            print("statement_void  -  igual identifier")
            assignment_call_stmt()
        elif (current_token["value"] == "{"):
            print("statement_void  -  igual {")
            compound_stmt_void()
        elif (current_token["tipo"] == "if"):
            print("statement_void  -  igual if")
            selection_stmt_void()
        elif (current_token["tipo"] == "while"):
            print("statement_void  -  igual while")
            iteration_stmt_void()
        elif (current_token["tipo"] == "input"):
            print("statement_void  -  igual input")
            input_stmt()
        elif (current_token["tipo"] == "output"):
            print("statement_void  -  igual output")
            output_stmt()
        else:
            print("-----ERROR statement_void--------")
            return

    def statement_int():
        if (current_token["tipo"] == "identifier"):
            print("statement_int  -  igual identifier")
            assignment_call_stmt()
        elif (current_token["value"] == "{"):
            print("statement_int  -  igual {")
            compound_stmt_int_no_return()
        elif (current_token["tipo"] == "if"):
            print("statement_int  -  igual if")
            selection_stmt_int()
        elif (current_token["tipo"] == "while"):
            print("statement_int  -  igual while")
            iteration_stmt_int()
        # elif (current_token["tipo"] == "return"):
        #     print("statement_int  -  igual return")
        #     return_stmt_int()
        #     print("regresa statement_int")
        elif (current_token["tipo"] == "input"):
            print("statement_int  -  igual input")
            input_stmt()
        elif (current_token["tipo"] == "output"):
            print("statement_int  -  igual output")
            output_stmt()
        else:
            print("-----ERROR statement_int--------")
            return

    def assignment_call_stmt():
        if (current_token["tipo"] == "identifier"):
            print("assignment_call_stmt  -  igual identifier")
            match_tipo("identifier")
            assignment_call_stmt_factor()
            match_value(";")
        else:
            print("-----ERROR assignment_call_stmt--------")
            return

    def assignment_call_stmt_factor():
        if (current_token["value"] == "("):
            print("assignment_call_stmt_factor  -  igual (")
            match_value("(")
            args()
            match_value(")")
        elif (current_token["value"] == "[" or current_token["value"] == "="):
            var_array()
            match_value("=")
            expression()
        else:
            print(current_token)
            print("-----ERROR assignment_call_stmt_factor--------")
            return

    def selection_stmt_void():
        if (current_token["tipo"] == "if"):
            print("selection_stmt_void  -  igual if")
            match_tipo("if")
            match_value("(")
            expression()
            match_value(")")
            statement_void()
            selection_stmt_void_else()
        else:
            print("-----ERROR selection_stmt_void--------")
            return

    def selection_stmt_void_else():
        if (current_token["tipo"] == "else"):
            print("selection_stmt_void_else  -  igual else")
            match_tipo("else")
            statement_void()
        elif (current_token["value"] == "{"
              or current_token["value"] == "}"
              or current_token["value"] == "identifier"
              or current_token["value"] == "if"
              or current_token["value"] == "while"
              or current_token["value"] == "input"
              or current_token["value"] == "output"):
            return
        else:
            print("-----ERROR selection_stmt_void_else--------")
            return

    def selection_stmt_int():
        if (current_token["tipo"] == "if"):
            print("selection_stmt_int  -  igual if")
            match_tipo("if")
            match_value("(")
            expression()
            match_value(")")
            statement_int()
            selection_stmt_int_else()
        else:
            print("-----ERROR selection_stmt_int--------")
            return

    def selection_stmt_int_else():
        if (current_token["tipo"] == "else"):
            print("selection_stmt_int_else  -  igual else")
            match_tipo("else")
            statement_int()
        elif (current_token["value"] == "{"
              or current_token["value"] == "}"
              or current_token["value"] == "identifier"
              or current_token["value"] == "if"
              or current_token["value"] == "while"
              or current_token["value"] == "return"
              or current_token["value"] == "input"
              or current_token["value"] == "output"):
            return
        else:
            print("-----ERROR selection_stmt_int_else--------")
            return

    def iteration_stmt_void():
        if (current_token["tipo"] == "while"):
            print("iteration_stmt_void  -  igual while")
            match_tipo("while")
            match_value("(")
            expression()
            match_value(")")
            statement_void()
        else:
            print("-----ERROR iteration_stmt_void--------")
            return

    def iteration_stmt_int():
        if (current_token["tipo"] == "while"):
            print("iteration_stmt_int  -  igual while")
            match_tipo("while")
            match_value("(")
            expression()
            match_value(")")
            statement_int()
        else:
            print("-----ERROR iteration_stmt_int--------")
            return

    def return_stmt_int():
        if (current_token["tipo"] == "return"):
            print("return_stmt_int  -  igual return")
            match_tipo("return")
            return_stmt_int_exp()
            match_value(";")
        else:
            print("-----ERROR return_stmt_int--------")
            return

    def return_stmt_int_exp():
        if (current_token["value"] == "("
                or current_token["tipo"] == "number"
                or current_token["tipo"] == "identifier"):
            expression()

        elif (current_token["value"] == ";"):
            return
        else:
            print("-----ERROR return_stmt_int_exp--------")
            return

    def input_stmt():
        if (current_token["tipo"] == "input"):
            print("input_stmt  -  igual input")
            match_tipo("input")
            match_tipo("identifier")
            var_array()
            match_value(";")
        else:
            print("-----ERROR input_stmt--------")
            return

    def output_stmt():
        if (current_token["tipo"] == "output"):
            print("output_stmt  -  igual ouput")
            match_tipo("output")
            expression()
            match_value(";")
        else:
            print("-----ERROR output_stmt--------")
            return

    def var_array():
        if (current_token["value"] == "["):
            print("var_array  -  igual [")
            match_value("[")
            arithmetic_expression()
            match_value("]")
        elif (current_token["value"] == "="
                or current_token["value"] == ";"
                or current_token["value"] == "<="
                or current_token["value"] == "<"
                or current_token["value"] == ">="
                or current_token["value"] == ">"
                or current_token["value"] == "=="
                or current_token["value"] == "!="
                or current_token["value"] == "]"
                or current_token["value"] == "+"
                or current_token["value"] == "-"
                or current_token["value"] == "/"
                or current_token["value"] == "*"
                or current_token["value"] == ","):
            return
        else:
            print("-----ERROR var_array--------")
            return

    def expression():
        arithmetic_expression()
        expression_factor()

    def expression_factor():
        if (current_token["value"] == "<="
                or current_token["value"] == "<"
                or current_token["value"] == ">="
                or current_token["value"] == ">"
                or current_token["value"] == "=="
                or current_token["value"] == "!="):
            relop()
            arithmetic_expression()
        elif (current_token["value"] == ";" or current_token["value"] == ")"):
            return
        else:
            print("-----ERROR expression_factor--------")
            return

    def relop():
        if (current_token["value"] == "<="):
            print("relop  -  igual <=")
            match_value("<=")
        elif (current_token["value"] == "<"):
            print("relop  -  igual <")
            match_value("<")
        elif (current_token["value"] == ">="):
            print("relop  -  igual >=")
            match_value(">=")
        elif (current_token["value"] == ">"):
            print("relop  -  igual >")
            match_value(">")
        elif (current_token["value"] == "=="):
            print("relop  -  igual ==")
            match_value("==")
        elif (current_token["value"] == "!="):
            print("relop  -  igual !=")
            match_value("!=")
        else:
            print("-----ERROR relop--------")
            return

    def arithmetic_expression():
        term()
        arithmetic_expression_prime()

    def arithmetic_expression_prime():
        if (current_token["value"] == "+" or current_token["value"] == "-"):
            print("arithmetic_expression_prime  -  igual + o -")
            addop()
            term()
            arithmetic_expression_prime()
        elif (current_token["value"] == "]"
              or current_token["value"] == "<="
              or current_token["value"] == "<"
              or current_token["value"] == ">="
              or current_token["value"] == ">"
              or current_token["value"] == "=="
              or current_token["value"] == "!="
              or current_token["value"] == ";"
              or current_token["value"] == ")"
              or current_token["value"] == ","):
            return
        else:
            print("-----ERROR arithmetic_expression_prime--------")
            return

    def addop():
        if (current_token["value"] == "+"):
            print("addop  -  igual +")
            match_value("+")
        elif (current_token["value"] == "-"):
            print("addop -  igual -")
            match_value("-")
        else:
            print("-----ERROR addop--------")
            return

    def term():
        factor()
        term_prime()

    def term_prime():
        if (current_token["value"] == "*" or current_token["value"] == "/"):
            print("term_prime ")
            mulop()
            factor()
            term_prime()
        elif (current_token["value"] == "+"
              or current_token["value"] == "-"
              or current_token["value"] == "]"
              or current_token["value"] == "<="
              or current_token["value"] == "<"
              or current_token["value"] == ">="
              or current_token["value"] == ">"
              or current_token["value"] == "=="
              or current_token["value"] == "!="
              or current_token["value"] == ";"
              or current_token["value"] == ")"
              or current_token["value"] == ","):
            return
        else:
            print("-----ERROR term_prime--------")
            return

    def mulop():
        if (current_token["value"] == "*"):
            print("mulop  -  igual *")
            match_value("*")
        elif (current_token["value"] == "/"):
            print("mulop -  igual /")
            match_value("/")
        else:
            print("-----ERROR mulop--------")
            return

    def factor():
        if (current_token["value"] == "("):
            print("factor  -  igual (")
            match_value("(")
            arithmetic_expression()
            match_value(")")
        elif (current_token["tipo"] == "number"):
            print("factor -  igual number")
            match_tipo("number")
        elif (current_token["tipo"] == "identifier"):
            factor_ID()
        else:
            print("-----ERROR factor--------")
            return

    def factor_ID():
        if (current_token["tipo"] == "identifier"):
            print("factor_ID -  igual identifier")
            match_tipo("identifier")
            factor_factor()
        else:
            print("-----ERROR factor_ID--------")
            return

    def factor_factor():
        if (current_token["value"] == "("):
            print("factor_factor  -  igual (")
            match_value("(")
            args()
            match_value(")")
        else:
            var_array()

    def args():
        if (current_token["value"] == "("
                or current_token["tipo"] == "number"
                or current_token["tipo"] == "identifier"):
            arithmetic_expression()
            args_list()
        elif (current_token["value"] == ")"):
            return

    def args_list():
        if (current_token["value"] == ","):
            match_value(",")
            arithmetic_expression()
            args_list()
        elif (current_token["value"] == ")"):

            return

    def match_tipo(terminal):
        if (current_token["tipo"] == terminal):
            print("igual_tipo: Terminal - ", terminal,
                  ", Current_token - ", current_token["tipo"])
            get_next_token()
        else:
            print("diferentes_tipo: Terminal - ", terminal,
                  ", Current_token - ", current_token["value"])
            print("---------ERROR-TIPO---------")

    def match_value(terminal):
        if (current_token["value"] == terminal):
            print("igual_ symbol: Terminal - ", terminal,
                  ", Current_token - ", current_token["value"])
            get_next_token()
        else:
            print("diferentes_symbol: Terminal - ", terminal,
                  ", Current_token - ", current_token["value"])
            print("-------ERROR-SYMBOL---------")

    def get_next_token():
        global index
        global current_token
        index = index + 1
        current_token = list_tokens[index]

    def program():
        declaration_list()

    program()


if __name__ == '__main__':

    data = analizados_lexico()
    if data["status"] == 0:
        analizados_sintactico(data["list_tokens"])
        # print("\n")
        # print("STATUS - ", data["status"])
        # print("\n")
        # print("Message - ", data["message"])
        # print("\n")
        # print("LISTA DE TOKENS")
        # for element in data["list_tokens"]:
        #     print(element)
        # print("\n")
        # print("LISTA DE IDENTIFICADORES")
        # for element in data["list_identifiers"]:
        #     print(element)
        # print("\n")
        # print("LISTA DE NUMEROS")
        # for element in data["list_numbers"]:
        #     print(element)
        # print("\n")
    else:
        print("\n")
        print("Status - ", data["status"])
        print("\n")
        print("Mensaje - ", data["message"])
        print("\n")

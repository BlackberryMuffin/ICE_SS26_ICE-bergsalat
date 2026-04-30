import parsers.vanilla_parser
interpreter = True

parse = parsers.vanilla_parser.parser.parse




while interpreter:
    try:
        s = input('> ')
    except EOFError:
        break
    if s == "stop":
        break
    if not s: continue
    result = parse(s)
    print(result)



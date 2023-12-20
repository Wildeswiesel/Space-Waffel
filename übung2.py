größe = 8

# Dreieck mit "x" aufsteigend
for i in range(größe + 1):
    print("x" * i, end="")
    spaces = " " * (größe - i)
    chars = "o" * i
    line = spaces + chars
    print(line)

# Dreieck mit "x" absteigend (ohne die Spitze)
for i in range(größe - 1, 0, -1):
    print("x" * i, end="")
    spaces = " " * (größe - i)
    chars = "o" * i
    line = spaces + chars
    print(line)

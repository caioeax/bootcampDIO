curso = "   pyThOn   "

print(curso.upper())
print(curso.lower())
print(curso.title())

print(curso.strip())
print(curso.rstrip())
print(curso.lstrip())

print(curso.center(21, "#"))

print(".".join(curso))

for letra in curso:
    print(letra, end="-")
print()
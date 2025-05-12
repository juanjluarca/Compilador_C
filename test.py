# import subprocess

# subprocess.run(['nasm', '-f', 'elf32', 'input.asm', '-o', 'input.o'], check=True)

# subprocess.run(['ld', '-m', 'elf_i386', 'input.o', '-o', 'input'], check=True)

# subprocess.run(['./input'], check=True)

# Creacion de un diccinario
diccionario = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Madrid'
}
# Recorrer el diccionario
print(diccionario.items())
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

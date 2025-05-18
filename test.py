import subprocess

subprocess.run(['nasm', '-f', 'elf32', 'input.asm', '-o', 'input.o'], check=True)

subprocess.run(['ld', '-m', 'elf_i386', 'input.o', '-o', 'input'], check=True)

subprocess.run(['./input'], check=True)

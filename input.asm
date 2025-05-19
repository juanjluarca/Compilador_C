; Lectura de datos desde teclado y almacenamiento en memoria
; Fecha 20250428
; Para ejecutar (en un archivo.py): 
; subprocess.run(['nasm', '-f', 'elf32', 'input.asm', '-o', 'input.o'], check=True)
; subprocess.run(['ld', '-m', 'elf_i386', 'input.o', '-o', 'input'], check=True)
; subprocess.run(['./input'], check=True)

%include 'funciones.asm'

SECTION .data
    msg1    db      'Ingrese su nombre: ', 0
    msg2    db      'Hola ', 0
    num     dd      88
    newline db      0xA, 0

SECTION .bss
    nombre  resb    20
    char    resb    16

SECTION .text
    global _start

_start:
    mov     eax, msg1
    call    printStr

    mov     eax, nombre     ; buffer para almacenar el input
    mov     ebx, 30         ; tamaño máximo del input
    call    input

    mov     eax, msg2
    call    printStr

    mov     eax, nombre
    call    printStr

    mov     eax, [num]
    call    printnum

    call    quit
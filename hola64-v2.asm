; Hola mundo versión de 64 bits
; nasm -f elf64 hola64-v2.asm -o hola64-v2.o
; ld -o hola64-v2 hola64-v2.o
; ./hola64-v2

%include 'stdio64.asm'

SECTION .data
    msg     db      'Hola mundo! este es un ejemplo de impresion', 10, 0

SECTION .text
    global _start

_start:
    mov     rax, msg
    call printStr

    call salir
    
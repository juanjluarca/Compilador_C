%include 'funciones.asm'

SECTION .data
    msg db 'Hola mundo este es un mensaje!', 0Ah, 0

SECTION .text
    global _start

_start:
    ;-------------------- Imprimir ==> print(msg) ----------------------
    mov eax, msg
    call printstr

    ;-------------------- End ------------------------------------------
    call quit


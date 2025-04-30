; Lectura de datos desde teclado y almacenamiento en memoria
; Fecha 20250428

%include 'funciones.asm'

SECTION .data
    msg1    db      'Ingrese su nombre: ', 0
    msg2    db      'Hola ', 0
    num     dd      88

SECTION .bss
    nombre  resb    20
    char    resb    16

SECTION .text
    global _start

_start:
    mov     eax, msg1
    call    printStr

    mov     edx, 30         ; edx = espacio total para Lectura
    mov     ecx, nombre     ; ecx = dir. de memoria para almacenar el dato
    mov     ebx, 0          ; lee desde STDIN
    mov     eax, 3          ; servicio de sistema SYS_READ
    int     80h             ; llamada al sistema

    mov     eax, msg2
    call    printStr

    mov     eax, nombre
    call    printStr

    mov     eax, [num]
    call    printnum

    call    quit


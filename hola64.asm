; Hola mundo versión de 64 bits
; nasm -f elf64 hola64.asm -o hola64.o
; ld -o hola64 hola64.o
; ./hola64



SECTION .data
    msg     db      'Hola mundo!', 10

SECTION .text
    global _start

_start:
    mov     rdx, 12     ; Tamanio de la cadena
    mov     rsi, msg    ; Apunta a direccion base de la cadena
    mov     rdi, 1      ; STDOUT (monitor)
    mov     rax, 1      ;
    syscall             ; llamada a sistema

    mov     rax, 60
    xor     rdi, rdi
    syscall
    
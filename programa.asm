%include 'funciones.asm'
section .data
   x dd 0
   y dd 0
   z dd 0
   newline db 0xA
section .bss
   char resb 16
section .text
   global _start
_start:
   mov eax, 8 ; Cargar número 8 en eax
   mov [x], eax; Guardar resultado en x
   mov eax, 5 ; Cargar número 5 en eax
   mov [y], eax; Guardar resultado en y
   mov eax, 6 ; Cargar número 6 en eax
   mov [z], eax; Guardar resultado en z
   mov eax, [z] ; Cargar variable z en eax
   call printnum
   call quit
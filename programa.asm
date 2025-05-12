%include 'funciones.asm'
section .data
   a dd 0
   b dd 0
   c dd 0
   x dd 0
   y dd 0
   z dd 0
   newline db 0xA
section .bss
   char resb 16
section .text
   global _start
funcion:
   mov eax, [esp + 4]
   mov [a], eax
   mov eax, [esp + 8]
   mov [b], eax
   mov eax, [esp + 12]
   mov [c], eax
   mov eax, [a] ; Cargar variable a en eax
   push eax; guardar en la pila
   mov eax, [b] ; Cargar variable b en eax
   pop ebx; recuperar el primer operando
   add eax, ebx; eax = eax + ebx
   mov [c], eax; Guardar resultado en c
   mov eax, "Hola mundo prueba de impresion" ; Cargar cadena Hola mundo prueba de impresion en eax
   mov eax, [c] ; Cargar variable c en eax
   call printnum
   mov eax, [c] ; Cargar variable c en eax
   ret ; Retornar desde la subrutina
   ret
_start:
   mov eax, 8 ; Cargar número 8 en eax
   mov [x], eax; Guardar resultado en x
   mov eax, 5 ; Cargar número 5 en eax
   mov [y], eax; Guardar resultado en y
   mov eax, 0 ; Cargar número 0 en eax
   mov [z], eax; Guardar resultado en z
   mov eax, [z] ; Cargar variable z en eax
   push eax
   mov eax, [y] ; Cargar variable y en eax
   push eax
   mov eax, [x] ; Cargar variable x en eax
   push eax
   call funcion
   add esp, 12
   mov eax, [z] ; Cargar variable z en eax
   ret ; Retornar desde la subrutina
   call quit
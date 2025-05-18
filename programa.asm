%include 'funciones.asm'
section .data
   a dd 0
   b dd 0
   c dd 0
   x dd 0
   y dd 0
   z dd 0
   var db 0x00
   variable dd 0
   cadena_0 db 'La variable es', 0
   newline db 0xA
section .bss
   char resb 16
section .text
   global _start
suma:
   mov eax, [esp + 4]
   mov [a], eax
   mov eax, [esp + 8]
   mov [b], eax
   mov eax, [a] ; Cargar variable a en eax
   push eax; guardar en la pila
   mov eax, [b] ; Cargar variable b en eax
   pop ebx; recuperar el primer operando
   add eax, ebx; eax = eax + ebx
   mov [c], eax; Guardar resultado en c
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
   mov eax, 2 ; Cargar número 2 en eax
   mov [z], eax; Guardar resultado en z
   mov eax, Hola Mundo ; Cargar cadena Hola Mundo en eax
   mov [var], eax; Guardar resultado en var
   mov eax, [x] ; Cargar variable x en eax
   call printnum
   mov eax, cadena_0 ; Cargar variable cadena_0 en eax
   call printStr
   mov eax, [z] ; Cargar variable z en eax
   push eax; guardar en la pila
   mov eax, 2 ; Cargar número 2 en eax
   pop ebx; recuperar el primer operando
   add eax, ebx; eax = eax + ebx
   mov [variable], eax; Guardar resultado en variable
   mov eax, [variable] ; Cargar variable variable en eax
   call printnum
   mov eax, [y] ; Cargar variable y en eax
   push eax
   mov eax, [x] ; Cargar variable x en eax
   push eax
   call suma
   add esp, 8
   call quit
section .data
   x dd 0
   z dd 0
   i dd 0
   y dd 0
   a dd 0
   b dd 0
   c dd 0
   newline db 0xA
section .bss
   char resb 16
section .text
   global _start
funcion:
   mov eax, [esp+4]
   mov [a], eax
   mov eax, [esp+8]
   mov [b], eax
   mov eax, [esp+12]
   mov [c], eax
   mov eax, [c] ; Cargar variable c en eax
   call imprimir
   mov eax, [a] ; Cargar variable a en eax
   push eax; guardar en la pila
   mov eax, [c] ; Cargar variable c en eax
   pop ebx; recuperar el primer operando
   cmp eax, ebx; comparar eax y ebx
   mov eax, 0; cargar 0 en eax
   setg al; eax = eax > ebx
   cmp eax, 0 ; Comparar resultado con 0
   jne etiqueta_else ; Saltar a else si la condición es falsa
   mov eax, [a] ; Cargar variable a en eax
   call imprimir
   jmp etiqueta_fin_if ; Saltar al final del if
etiqueta_else:
   mov eax, [b] ; Cargar variable b en eax
   call imprimir
etiqueta_fin_if:
etiqueta_inicio:
   mov eax, [b] ; Cargar variable b en eax
   push eax; guardar en la pila
   mov eax, 11 ; Cargar número 11 en eax
   pop ebx; recuperar el primer operando
   cmp eax, ebx; comparar eax y ebx
   mov eax, 0; cargar 0 en eax
   setl al; eax = eax < ebx
   cmp eax, 0 ; Comparar resultado con 0
   jne etiqueta_fin_while ; Saltar al final si la condición es falsa
   mov eax, [b] ; Cargar variable b en eax
   push eax; guardar en la pila
   mov eax, 1 ; Cargar número 1 en eax
   pop ebx; recuperar el primer operando
   add eax, ebx; eax = eax + ebx
   mov [b], eax; Guardar resultado en b
   jmp etiqueta_inicio ; Saltar al inicio del ciclo
etiqueta_fin_while:
   mov eax, [b] ; Cargar variable b en eax
   call imprimir
   mov eax, 0 ; Cargar número 0 en eax
   mov [i], eax; Guardar resultado en i
for_inicio:
   mov eax, [i] ; Cargar variable i en eax
   push eax; guardar en la pila
   mov eax, 10 ; Cargar número 10 en eax
   pop ebx; recuperar el primer operando
   cmp eax, ebx; comparar eax y ebx
   mov eax, 0; cargar 0 en eax
   setl al; eax = eax < ebx
   cmp eax, 0
   jne for_fin
   mov eax, [i] ; Cargar variable i en eax
   call imprimir
   mov eax, [i] ; Cargar variable i en eax
   push eax; guardar en la pila
   mov eax, 2 ; Cargar número 2 en eax
   pop ebx; recuperar el primer operando
   add eax, ebx; eax = eax + ebx
   mov [i], eax; Guardar resultado en i
   jmp for_inicio
for_fin:
   mov eax, 0 ; Cargar número 0 en eax
   ret ; Retornar desde la subrutina
   ret
_start:
   mov eax, 8 ; Cargar número 8 en eax
   mov [x], eax; Guardar resultado en x
   mov eax, 5 ; Cargar número 5 en eax
   mov [y], eax; Guardar resultado en y
   mov eax, [x] ; Cargar variable x en eax
   push eax; guardar en la pila
   mov eax, [y] ; Cargar variable y en eax
   pop ebx; recuperar el primer operando
   add eax, ebx; eax = eax + ebx
   mov [z], eax; Guardar resultado en z
   mov eax, [z] ; Cargar variable z en eax
   call imprimir
   mov eax, [z] ; Cargar variable z en eax
   push eax
   mov eax, [y] ; Cargar variable y en eax
   push eax
   mov eax, [x] ; Cargar variable x en eax
   push eax
   call funcion
   add esp, 12
   mov eax, 0 ; Cargar número 0 en eax
   ret ; Retornar desde la subrutina
   mov eax, 1
   xor ebx, ebx
   int 0x80
imprimir:
   mov ecx, 10
   mov edi, char+11
   mov byte [edi], 0
   dec edi
   mov byte [edi], 0xA
   dec edi
   mov esi, 2
convert_loop:
   xor edx, edx
   div ecx
   add dl, '0'
   mov [edi], dl
   dec edi
   inc esi
   test eax, eax
   jnz convert_loop
   inc edi
   mov eax, 4
   mov ebx, 1
   mov ecx, edi
   mov edx, esi
   int 0x80
   ret
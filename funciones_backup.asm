;---------------------- Imprimir cadena ----------- 
printStr:
    ; Guardar registros en pila
    push edx
    push ecx
    push ebx
    push eax ; Acá apunta a la cadena

    call strlen   ; llamada a la funcion de conteo de caracter
    
    mov edx, eax ; longitud de cadena
    pop eax
    mov ecx, eax  ; Cadena a imprimir

    mov ebx, 1    ; tipo de salida (1 implica salida por pantalla) (STDOUT file)
    mov eax, 4    ; SYS_WRITE (Kernel opcode 4)
    int 80h       ; Se imprime en pantalla

    pop ebx
    pop ecx
    pop edx

quit:
    mov ebx, 0    ; return 0 status on exit
    mov eax, 1    ; SYS_EXIT (kernel opcode 1)
    int 80h       ; Fin del programa


;--------------------- calculo de longitud de cadena -------------
strlen:
    push ebx
    mov ebx, eax

nextChar:
    cmp byte [eax], 0
    jz finLen
    inc eax
    jmp nextChar

finLen:
    sub eax, ebx
    pop ebx
    ret


;--------------------- Imprimir variables que contengan número --------------

printnum:

    ; Convertir número a string (maneja múltiples dígitos)
    mov ecx, 10         ; Divisor para conversión
    mov edi, char+11
    mov byte [edi], 0   ; Null terminator
    dec edi
    mov byte [edi], 0xA  ; Newline
    dec edi
    mov esi, 2          ; Contador de caracteres (newline + null)",

convert_loop:
    xor edx, edx       ; Limpiar edx para división
    div ecx           ; eax = eax/10, edx = resto
    add dl, '0'         ; Convertir a ASCII
    mov [edi], dl       ; Almacenar dígito
    dec edi
    inc esi
    test eax, eax      ; Verificar si eax es cero
    jnz convert_loop

    ; Ajustar puntero al inicio del número
    inc edi

    ; Imprimir el número con newline
    mov eax, 4          ; sys_write
    mov ebx, 1          ; stdout
    mov ecx, edi        ; Puntero al string
    mov edx, esi        ; Longitud (dígitos + newline)
    int 0x80
    ret  ; Retornar de la función printnum



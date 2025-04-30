;-------------- int strLen(cadena) -----------------------
strLen:
    ; Resguardar registro en pila
    push    rsi
    mov     rsi, rax

nextChar:
    cmp     byte[rax], 0
    jz      finStrLen
    inc     rax
    jmp nextChar

finStrLen:
    sub     rax, rsi
    pop     rsi         ; Restaura el contenido de rsi
    ret




;-------------- printStr(cadena) --------------------------

printStr:
    ; Resguardar registros en pila
    push rdx
    push rsi
    push rdi
    push rax

    ; Llamada a longitud de cadena (cadena en rax)
    call strLen
    ; La longitud se devuelve en rax
    mov     rdx, rax     ; Tamanio de la cadena

    pop     rax         ; Se guarda el mensaje en rax
    mov     rsi, rax    ; Apunta a direccion base de la cadena
    mov     rdi, 1      ; STDOUT (monitor)
    mov     rax, 1      ;
    syscall             ; llamada a sistema

    ; Devolver el contenido a los registros
    pop rdi
    pop rsi
    pop rdx
    ret




; -------------------- Salir() -----------------
salir:
    mov     rax, 60
    xor     rdi, rdi
    syscall
    ret
    
from analizador import *

#------------------------- Análisis semántico -------------------------
class TablaSimbolos:
    def __init__(self):
        self.variables = {} # Almacena variables {nombre: tipo}
        self.funciones = {} # Almacena funciones {nombre: (tipo_retorno, [parametros])}

    def declarar_variable(self, nombre, tipo):
        if nombre in self.variables:
            raise Exception(f"Error: Variable '{nombre}' ya declarada")
        self.variables[nombre] = tipo


    def obtener_tipo_variable(self, nombre):
        if nombre not in self.variables:
            raise Exception(f"Error: Variable '{nombre}' no declarada")
        return self.variables[nombre]
    
    def declarar_funcion(self, nombre, tipo_retorno, parametros):
        if nombre in self.funciones:
            raise Exception(f"Error: Función '{nombre}' ya declarada")
        self.funciones[nombre] = (tipo_retorno, parametros)
    
    def obtener_info_funcion(self, nombre):
        if nombre not in self.funciones:
            raise Exception(f"Error: Función '{nombre}' no declarada")
        return self.funciones[nombre]



class AnalizadorSemantico:
    def __init__(self):
        self.tabla_simbolos = TablaSimbolos()
    def analizar(self, nodo):
        if isinstance(nodo, NodoAsignacion):
            tipo_expr = self.analizar(nodo.expresion)
            # Verificar si la variable ya existe (puede ser un parámetro)
            if nodo.nombre[1] not in self.tabla_simbolos.variables:
                self.tabla_simbolos.declarar_variable(nodo.nombre[1], tipo_expr)
            else:
                # Si ya existe, verificar que los tipos coincidan
                tipo_existente = self.tabla_simbolos.obtener_tipo_variable(nodo.nombre[1])
                if tipo_existente != tipo_expr:
                    raise Exception(f"Error: Tipo incompatible en asignación para '{nodo.nombre[1]}' (esperaba {tipo_existente}, recibió {tipo_expr})")
        elif isinstance(nodo, NodoIdentificador):
            return self.tabla_simbolos.obtener_tipo_variable(nodo.nombre[1])
        elif isinstance(nodo, NodoNumero):
            return "int"
        elif isinstance(nodo, NodoOperacion):
            tipo_izq = self.analizar(nodo.izquierda)
            tipo_der = self.analizar(nodo.derecha)
            if tipo_izq != tipo_der:
                raise Exception(f"Error: Tipos incompatibles {tipo_izq} {nodo.operador} {tipo_der}")
            return tipo_izq
        elif isinstance(nodo, NodoFuncion):
            # Registrar la función en la tabla de símbolos
            self.tabla_simbolos.declarar_funcion(nodo.nombre[1], nodo.tipo_retorno[1], nodo.parametros)
            
            # Registrar los parámetros en la tabla de variables
            for param in nodo.parametros:
                self.tabla_simbolos.declarar_variable(param.nombre[1], param.tipo[1])
            
            # Analizar el cuerpo de la función
            for instruccion in nodo.cuerpo:
                self.analizar(instruccion)
        elif isinstance(nodo, NodoLlamadaFuncion):
            tipo_retorno, parametros = self.tabla_simbolos.obtener_info_funcion(nodo.nombre[1])
            if len(nodo.argumentos) != len(parametros):
                raise Exception(f"Error: La función '{nodo.nombre[1]}' espera {len(parametros)} argumentos, pero recibió {len(nodo.argumentos)}")
            return tipo_retorno
        elif isinstance(nodo, NodoPrograma):
            for funcion in nodo.funciones:
                self.analizar(funcion)
        elif isinstance(nodo, NodoRetorno):
            tipo_expr = self.analizar(nodo.expresion)
            # Aquí deberías comparar con el tipo de retorno de la función actual
            raise NotImplementedError("Análisis de retorno no implementado completamente")
    #     metodo = f'visitar_{type(nodo).__name__}'
    #     if hasattr(self, metodo):
    #         method = getattr(self, metodo)(nodo)
    #         return method
    #     else:
    #         raise Exception(f'No se ha implementado el análisis semántico para {type(nodo).__name__}')
    
    # def visitar_NodoPrograma(self, nodo):
    #     # Programa contiene una lista de NodoFuncion
    #     for funcion in nodo.funciones:
    #         self.analizar(funcion)
        
    # def visitar_NodoFuncion(self, nodo):
    #     if nodo.nombre[1] in self.tabla_simbolos:
    #         raise Exception(f'Error semántico: la función {nodo.nombre[1]} ya está definida')
    #     self.tabla_simbolos[nodo.nombre[1]] = {'tipo': nodo.parametros[0].tipo[1], 
    #                                            'parametros': nodo.parametros}
    #     for param in nodo.parametros:
    #         self.tabla_simbolos[param.nombre[1]] = {'tipo':param.tipo[1]}
    #     for instruccion in nodo.cuerpo:
    #         self.analizar(instruccion)

    # def visitar_NodoAsignacion(self, nodo):
    #     tipo_expresion = self.analizar(nodo.expresion)
    #     self.tabla_simbolos[nodo.nombre[1]] = {'tipo': tipo_expresion}

    # def visitar_NodoOperacion(self, nodo):
    #     tipo_izquierda = self.analizar(nodo.izquierda)
    #     tipo_derecha = self.analizar(nodo.derecha)
    #     if tipo_izquierda != tipo_derecha:
    #         raise Exception(f'Error semántico: tipos incompatibles {tipo_izquierda} y {tipo_derecha}')
    #     return tipo_izquierda
    
    # def visitar_NodoNumero(self, nodo):
    #     return 'int' if '.' not in nodo.valor[1] else 'float'
    
    # def visitar_NodoIdentificador(self, nodo):
    #     if nodo.nombre[1] not in self.tabla_simbolos:
    #         raise Exception(f'Error semántico: La variable {nodo.nombre[1]} no está definida')
    #     return self.tabla_simbolos[nodo.nombre[1]]['tipo']

    # def visitar_NodoRetorno(self, nodo):
    #     return self.analizar(nodo.expresion)


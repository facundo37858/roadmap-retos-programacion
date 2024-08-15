# Funcion sin parametros y retorno

def saludar():
    print("Hola")

# Funcion con parametro sin retorno

def saludar_nombre(mi_nombre):
    print(f"Hola, {mi_nombre}")

# Funcion con parametros y retorno

def area_trinagulo(base , altura):
    return (base*altura)/2

# Funcion anidada

def calcular_area():
    def calcular_perimetro(lado):
        return lado*4
    lado=4
    perimetro = calcular_perimetro(lado)
    area=lado**2
    return area,perimetro
# Funcion predefinidas

def potencia(base,exponente):
    return pow(base,exponente)

# Variable local global

var_global="soy global"

def cambiar_variables():
    var_global="soy local"
    print(f"Dentro de la funcion {var_global}")

print(f"Antes de la funcion {var_global}")
cambiar_variables()
print(f"Despues de la funcion {var_global}")

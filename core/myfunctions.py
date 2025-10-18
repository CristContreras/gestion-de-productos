import os
import time


def limpiar_pantalla():
    os.system("cls")


def pedir_string(mensaje: str) -> str:
    dato: str = input(mensaje)
    while not es_string(dato):
        print("Debe ingresa solo letras")
        dato = input(mensaje)
    return dato


def pedir_numero(mensaje: str) -> int:
    dato: str = input(mensaje)
    while not es_numero(dato):
        print("Debe ingresar un número")
        dato = input(mensaje)
    return int(dato)


def es_string(dato: str) -> bool:
    for letra in dato:
        if es_numero(letra):
            return False
    return True


def es_numero(dato: str) -> bool:
    return dato.isdigit()


def imprimir_producto(lista: list) -> None:
    print(f"Producto: {lista[0]}")
    print(f"Categoria: {lista[1]}")
    print(f"Precio: {lista[2]}")


def pedir_datos_producto(lista: list) -> tuple:
    msj_nombre = "Ingrese nombre del producto: "
    nombre = pedir_string(msj_nombre).strip().title()
    while es_producto_registrado(
        lista, nombre
    ):  
        print("El producto ya fue registrado.")
        nombre = pedir_string(msj_nombre).strip().title()
    categoria: str = pedir_string("Ingrese cateogría: ").strip().title()
    precio: int = pedir_numero("Ingrese precio: ")
    return nombre, categoria, precio


def ingresar_producto(lista: list, nombre: str, categoria: str, precio: str) -> None:
    lista.append([nombre, categoria, precio])


def volver_al_menu() -> None:
    print("\nVolviendo al menú principal...")
    time.sleep(2)


def procesar_ingreso_producto(lista: list) -> None:
    repetir: bool = True
    while repetir:
        print("1. Ingresar producto\n")
        nombre, categoria, precio = pedir_datos_producto(lista)
        ingresar_producto(lista, nombre, categoria, precio)
        print("\n¡Producto ingresado correctamente!")
        repetir = es_otro_ingreso()
        limpiar_pantalla()
    volver_al_menu()


def es_otro_ingreso() -> bool:
    repetir = True
    ciclo = True
    while ciclo:
        respuesta = input("\n¿Ingresar otro producto? (si/no): ").strip().lower()
        if respuesta in ("si", "no"):
            if respuesta in ("no"):
                repetir = False
                ciclo = False
            else:
                ciclo = False
        else:
            print("\nDebe ingresar si o no")
    return repetir


def es_producto_registrado(lista: list, nombre: str) -> bool:
    return obtener_producto(lista, nombre) is not None


def mostrar_menu() -> None:
    print("Bienvenido/a\n")
    print("1. Ingresar nuevo producto.")
    print("2. Mostrar productos registrados.")
    print("3. Buscar producto por nombre.")
    print("4. Eliminar producto.")
    print("5. Salir.")


def procesar_mostrar_productos(lista: list) -> None:
    print("2. Mostrar productos\n")
    if lista:
        for i, item in enumerate(lista, start=1):
            print(f"{i}. Producto: {item[0]}\nCategoría: {item[1]}\nPrecio: {item[2]}")
            print("-" * 20)
    else:
        print("Lista vacía")
    pedir_volver_menu()
    volver_al_menu()


def pedir_volver_menu() -> None:
    repetir = True
    while repetir:
        enter = input("\nPresione enter para volver al menú principal")
        if enter == "":
            repetir = False
        else:
            print("Debe presionar enter para volver.")


def procesar_buscar_producto(lista: list) -> None:
    print("3. Buscar producto\n")
    if lista:
        nombre = pedir_string("Ingrese nombre del producto: ").strip().title()
        sublista = obtener_producto(lista, nombre)
        if sublista is not None:
            imprimir_producto(sublista)
        else:
            print("No se encuentra el producto")
    else:
        print("Lista vacía")
    pedir_volver_menu()
    volver_al_menu()


def obtener_producto(lista: list, nombre: str) -> list | None:
    for item in lista:
        if item[0] == nombre:
            return item
    return None

def obtener_indice_producto(lista:list, nombre):
    for i, item in enumerate(lista):
        if item[0]==nombre:
            return i
    return None
    

def procesar_eliminar_producto(lista: list) -> None:
    print("4. Eliminar producto\n")
    if lista:
        nombre = pedir_string("Ingrese nombre del producto: ").strip().title()
        indice_producto = obtener_indice_producto(lista, nombre)
        if indice_producto is not None:
            eliminar_producto(lista, indice_producto)
            print("\nProducto eliminado correctamente.")
        else:
            print("No se encontro el producto")
    else:
        print("Lista vacia")
    pedir_volver_menu()
    volver_al_menu()


def eliminar_producto(lista: list, indice: int) -> None:
    del lista[indice]

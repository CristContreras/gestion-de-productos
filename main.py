import core.myfunctions as f
import time


def main():
    f.limpiar_pantalla()
    productos: list[list[str|str|int]]=[]
    repetir = True
    while repetir:
        f.limpiar_pantalla()
        f.mostrar_menu()
        opcion: int = f.pedir_numero("\nIngrese una opción: ")
        f.limpiar_pantalla()
        match opcion:
            case 1:
                f.procesar_ingreso_producto(productos)
            case 2:
                f.procesar_mostrar_productos(productos)
            case 3:
                f.procesar_buscar_producto(productos)
            case 4:
                f.procesar_eliminar_producto(productos)
            case 5:
                print("Muchas gracias por utilizar el sistema\n")
                time.sleep(2)
                repetir = False
            case _:
                print("Error: Opción incorrecta")
                time.sleep(2)
                f.limpiar_pantalla()
    f.limpiar_pantalla()


if __name__ == "__main__":
    main()

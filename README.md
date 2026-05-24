def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea(tareas):
    tarea_name = input("Nombre de la tarea a agregar: ")
    if tarea_name.strip() == "":
        print("❌ No se puede agregar una tarea vacía.")
    else:
        tareas.append(tarea_name)
        print(f"✅ La tarea '{tarea_name}' se ha AGREGADO")

def ver_tareas(tareas):
    if not tareas:  # ❗ CORREGIDO: antes era "lista"
        print("📭 La lista está vacía")
    else:
        print("\n📋 TUS TAREAS:")
        for i, tarea in enumerate(tareas, 1):  # ❗ USO enumerate para empezar en 1
            print(f"{i}. {tarea}")

def eliminar_tarea(tareas):
    nombre = input("Ingrese el nombre de la tarea a eliminar: ")
    if nombre in tareas:
        tareas.remove(nombre)  # ❗ CORREGIDO: remove, no del
        print(f"🗑️ La tarea '{nombre}' fue ELIMINADA")
    else:
        print(f"❌ No existe la tarea '{nombre}'")

def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_tarea(tareas)
        elif opcion == "2":
            ver_tareas(tareas)
        elif opcion == "3":
            eliminar_tarea(tareas)
        elif opcion == "4":
            print("👋 Adiós, vuelve pronto.")
            break  # ❗ El break está aquí, no dentro de una función
        else:
            print("❌ Opción inválida. Elige 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()

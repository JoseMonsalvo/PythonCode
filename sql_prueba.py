import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba'
)
cursor = conn.cursor()
final = False
while not final:
    print('1. SELECT')
    print('2. INSERT')
    print('3. UPDATE')
    print('4. DELETE')
    print('5. SALIR')
    option = input('Elige una opción: ')
    if option == '1':
        print('SELECT')
        cursor.execute('SELECT employee_id, first_name, last_name FROM employees')
        for (employee_id, first_name, last_name)in cursor.fetchall():
            print(f'ID: {employee_id}, Nombre: {first_name}, Apellido: {last_name}')
    elif option == '2':
        print('INSERT')
    elif option == '3':
        print('UPDATE')
    elif option == '4':
        print('DELETE')
    elif option == '5':
        final = True
    else:
        print('Opción inválida. Por favor, elige una opción válida.')
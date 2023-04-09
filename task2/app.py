@app.route('/', methods=['GET'])
def index():
    ip_address = request.remote_addr

    # Создаем соединение с базой данных
    conn = psycopg2.connect(
        host='postgres',  # имя контейнера с PostgreSQL
        port=5432,  # порт базы данных
        dbname='postgres',  # имя базы данных
        user='postgres',  # имя пользователя базы данных
        password='password'  # пароль пользователя базы данных
    )

    # Создаем курсор для выполнения SQL-запросов
    cur = conn.cursor()

    # Выполняем SQL-запрос для добавления IP-адреса клиента в базу данных
    cur.execute("INSERT INTO client_ips (ip_address) VALUES (%s)", (ip_address,))

    # Сохраняем изменения
    conn.commit()

    # Закрываем соединение с базой данных
    cur.close()
    conn.close()

    return f'IP-адрес {ip_address} успешно добавлен в базу данных.'
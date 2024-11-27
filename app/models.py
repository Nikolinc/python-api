def create_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    age INT
                )
            """)
            conn.commit()
            print("Таблица создана")
    except Exception as e:
        print("Ошибка при создании таблицы:", e)

def insert_data(conn, name, age):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (name, age) VALUES (%s, %s)",
                (name, age)
            )
            conn.commit()
            print("Данные добавлены")
    except Exception as e:
        print("Ошибка при добавлении данных:", e)

def fetch_data(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
            print("Данные из таблицы:")
            for row in rows:
                print(row)
    except Exception as e:
        print("Ошибка при выборке данных:", e)

def create_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    gender VARCHAR(10) NOT NULL,
                    person_id UUID UNIQUE NOT NULL,
                    date_of_birth DATE NOT NULL
                );
            """)
            conn.commit()
            print("Таблица создана")
    except Exception as e:
        print("Ошибка при создании таблицы:", e)

def insert_data(conn, name, gender,  person_id, date_of_birth):
    try:
        with conn.cursor() as cur:
            query = """
                INSERT INTO users (
                    name,
                    gender,
                    person_id,
                    date_of_birth)
                VALUES (%s, %s, %s, %s);
            """
            cur.execute(query, (name, gender, person_id, date_of_birth))
            conn.commit()
            return 'Данные добавлены'
    except Exception as e:
        print("Ошибка при добавлении данных:", e)

def fetch_data(conn):
    try:
        with conn.cursor() as cur:
            query="""
                SELECT
                    id,
                    name,gender,
                    person_id,
                    date_of_birth
                FROM public.users
            """
            cur.execute(query)
            rows = cur.fetchall()
            return rows
    except Exception as e:
        print("Ошибка при выборке данных:", e)

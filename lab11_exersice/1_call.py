import psycopg2
from config import load_config

def search_database(pattern):
    try:
        # Подключение к базе данных
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Вызов функции из базы данных
                cur.execute("SELECT * FROM search_records(%s)", (pattern,))
                # Получение всех результатов
                results = cur.fetchall()
                return results
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    pattern = input("Введите шаблон поиска: ")
    results = search_database(pattern)
    if results:
        print("Результаты поиска:")
        for row in results:
            print(row)
    else:
        print("Записи не найдены.")

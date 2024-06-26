import psycopg2
from config import load_config

def call_delete_user_data_procedure():
    try:
        # Подключение к базе данных
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Запрос ввода критерия удаления
                delete_criteria = input("Введите имя пользователя или номер телефона для удаления: ")
                # Вызов процедуры с использованием SQL-запроса и введенного критерия с явным указанием типа
                cur.execute("CALL delete_user_dataing(%s::varchar)", (delete_criteria,))
                # Применение изменений к базе данных
                conn.commit()
                print("Procedure executed successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    # Вызов процедуры с запросом ввода пользователя
    call_delete_user_data_procedure()

import psycopg2
from config import load_config

def call_insert_or_update_user_procedure():
    try:
        # Подключение к базе данных
        config = load_config()
        with psycopg2.connect(**config) as conn:
            # Получаем данные от пользователя
            new_name = input("Введите имя пользователя: ")
            new_phone = input("Введите номер телефона: ")
            
            with conn.cursor() as cur:
                # Вызов процедуры с использованием ключевого слова CALL
                cur.execute("CALL insert_or_update_user(%s, %s)", (new_name, new_phone))
                # Применение изменений к базе данных
                conn.commit()
                print("Procedure executed successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == "__main__":
    # Пример вызова процедуры
    call_insert_or_update_user_procedure()
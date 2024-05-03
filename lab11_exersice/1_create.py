import psycopg2
from config import load_config

def create_function():
    commands = [
        "DROP FUNCTION IF EXISTS search_records(TEXT);",
        """
        CREATE OR REPLACE FUNCTION search_records(search_pattern TEXT)
        RETURNS TABLE(fullnames varchar, phone_numbers varchar) AS $$
        BEGIN
            RETURN QUERY
            SELECT fullname, phone_number
            FROM phonebook
            WHERE fullname ILIKE '%' || search_pattern || '%'
                OR phone_number ILIKE '%' || search_pattern || '%';
        END;
        $$ LANGUAGE plpgsql;
        """
    ]
    
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                print("Function created successfully")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_function()

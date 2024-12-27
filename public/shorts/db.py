import sqlite3

def connect_to_db(db_path):
    """Connect to the SQLite database and return the connection object."""
    return sqlite3.connect(db_path)

def list_all_tables(cursor):
    """List all table names in the database."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

def describe_table(cursor, table_name):
    """Describe a given table (show its columns and data types)."""
    cursor.execute(f"PRAGMA table_info({table_name});")
    return cursor.fetchall()

def fetch_table_data(cursor, table_name, limit=5):
    """Fetch and return the first `limit` rows of a table."""
    cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit};")
    return cursor.fetchall()

def count_records(cursor, table_name):
    """Count records in a table."""
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    return cursor.fetchone()[0]

def find_unique_values(cursor, table_name, column_name):
    """Find unique values in a column."""
    cursor.execute(f"SELECT DISTINCT {column_name} FROM {table_name};")
    return cursor.fetchall()

def basic_analysis(cursor, table_name, column_name):
    """Compute average, min, max for numeric columns."""
    cursor.execute(f"SELECT AVG({column_name}), MIN({column_name}), MAX({column_name}) FROM {table_name};")
    return cursor.fetchone()

def search_data(cursor, table_name, condition):
    """Search for specific data in a table based on a given condition."""
    cursor.execute(f"SELECT * FROM {table_name} WHERE {condition};")
    return cursor.fetchall()

def main():
    db_path = "elijah_arbee.db"  # Path to your local database
    conn = connect_to_db(db_path)
    cursor = conn.cursor()

    while True:
        print("Options:")
        print("1. List all tables")
        print("2. Describe a table")
        print("3. Retrieve data from a table")
        print("4. Count records in a table")
        print("5. Find unique values in a column")
        print("6. Basic analysis on a column (avg, min, max)")
        print("7. Search data in a table based on condition")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tables = list_all_tables(cursor)
            print("Tables in the database:", tables)
        elif choice == "2":
            table_name = input("Enter table name: ")
            description = describe_table(cursor, table_name)
            for column in description:
                print(column[1], "-", column[2])
        elif choice == "3":
            table_name = input("Enter table name: ")
            data = fetch_table_data(cursor, table_name)
            for row in data:
                print(row)
        elif choice == "4":
            table_name = input("Enter table name: ")
            count = count_records(cursor, table_name)
            print(f"Total records in {table_name}: {count}")
        elif choice == "5":
            table_name = input("Enter table name: ")
            column_name = input("Enter column name: ")
            unique_values = find_unique_values(cursor, table_name, column_name)
            print("Unique values:", unique_values)
        elif choice == "6":
            table_name = input("Enter table name: ")
            column_name = input("Enter column name: ")
            avg, min_val, max_val = basic_analysis(cursor, table_name, column_name)
            print(f"Average: {avg}, Min: {min_val}, Max: {max_val}")
        elif choice == "7":
            table_name = input("Enter table name: ")
            condition = input("Enter your condition (e.g., 'column_name = value'): ")
            results = search_data(cursor, table_name, condition)
            for row in results:
                print(row)
        elif choice == "8":
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()

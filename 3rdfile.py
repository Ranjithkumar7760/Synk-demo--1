Python
import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    result = cursor.fetchone()
    conn.close()   


    return result

if __name__ == "__main__":
    user_id = input("Enter user ID: ")
    user_data = get_user_data(user_id)
    print(user_data)
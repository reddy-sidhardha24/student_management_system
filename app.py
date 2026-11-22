query = "INSERT INTO students (name, email, age) VALUES (?, ?, ?)"
    cursor.execute(query, (name, email, age))
    conn.commit()
import sqlite3

DB_NAME = "memory.db"


def init_db():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_id TEXT,

            role TEXT,

            content TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_message(
        user_id,
        role,
        content):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations(
            user_id,
            role,
            content
        )
        VALUES(?,?,?)
        """,
        (
            user_id,
            role,
            content
        )
    )

    conn.commit()
    conn.close()


def get_memory(user_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content

        FROM conversations

        WHERE user_id=?

        ORDER BY id DESC

        LIMIT 10
        """,
        (user_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    memory = []

    for row in rows:

        memory.append(
            {
                "role": row[0],
                "content": row[1]
            }
        )

    return memory


init_db()
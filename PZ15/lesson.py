import sqlite3 as sq

with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_Id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        sex INTEGER NOT NULL DEFAULT 1,
        old INTEGER,
        score INTEGER
    )""")

    
    cur.execute("""
        INSERT INTO users (name, sex, old, score)
        VALUES ('вова', 1, 17, 1343),
               ('толик', 0, 18, 20000000),
               ('даниэль', 1, 17, 54254255412541258)
    """)

    con.commit()


    cur.execute('SELECT * FROM users')

    
    rows = cur.fetchall()


    # for row in rows:
    #     print(row)

    info_users = [
        (None, 'Алексей', 1, 22, 1000),
        (None, 'Mишa', 1, 19, 800)
    ]

    cur.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?)", info_users)
    con.commit()

    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    for row in rows:
        print(row)


with sq.connect('saper.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE score > 1000 ORDER BY score DESC")
    result = cur.fetchall()
    print (result) 
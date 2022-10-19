import sqlite3

db = sqlite3.connect('base.db', check_same_thread=False)
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS a_b_c (
    a INT,
    b TEXT,
    c INT
)''')

sql.execute('''CREATE TABLE IF NOT EXISTS a_m (
    a INT,
    res TEXT
)''')

db.commit()

sql.execute('INSERT INTO a_b_c VALUES (?, ?, ?)', (1, 'x', 3))
sql.execute('INSERT INTO a_b_c VALUES (?, ?, ?)', (2, 'y', 4))
sql.execute('INSERT INTO a_b_c VALUES (?, ?, ?)', (3, 'x', 7))
sql.execute('INSERT INTO a_b_c VALUES (?, ?, ?)', (4, 'y', 9))

db.commit()

def main(): #универсальный случай, если значения в столбце b не ограничиваются только x и y
    sql.execute('SELECT * FROM a_b_c')
    a_b_c = sql.fetchall()
    db.commit()

    b_types = []
    m_input = []
    a = 1

    for b in a_b_c:
        if b[1] not in b_types:
            b_types += b[1]

    for b_type in b_types:
        m = ''
        for c in a_b_c:
            if c[1] == b_type:
                m += f'{c[1]}-{c[2]}\n'
        sql.execute(f'INSERT INTO a_m VALUES (?, ?)', (a, m))
        db.commit()
        a += 1

    sql.execute('SELECT * FROM a_m')
    db.commit()

main()
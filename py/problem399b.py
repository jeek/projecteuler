import sqlite3
limit = 100000000
conn = sqlite3.connect('problem399.dat')

c = conn.cursor()
d = conn.cursor()
c.execute('''CREATE TABLE numbers (value text)''')

a = 1
b = 1

count = 0
while count < (1.5 * limit):
    c.execute('INSERT INTO numbers VALUES ("' + str(b) + '")')
    (a, b) = (b, a + b)
#    conn.commit()
    count += 1
    print count, limit*1.5
conn.commit()
for i in range(2, int(limit ** .6)):
    for row in c.execute('SELECT * FROM numbers'):
        if int(row[0]) % (i ** 2) == 0:
            print row[0], i
            d.execute('DELETE FROM numbers WHERE value=("' + row[0] + '")')
            conn.commit()

    j = 2
#    print c.execute('SELECT * FROM numbers')[limit]
    for row in c.execute('SELECT * FROM numbers'):
        if j == limit:
#        if j >= 190:
            print i, j, row
        j += 1
        
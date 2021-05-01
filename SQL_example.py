"""sqlite> CREATE TABLE books (
   ...> id bigint,
   ...> title varchar(50),
   ...> author varchar(100),
   ...> want_to_read bool);
sqlite> SELECT * FROM books;
sqlite> INSERT INTO books
   ...> VALUES (1,'The Hobbit', 'John R. R. Tolkien', false);"""

import sqlite3

conn = sqlite3.connect('C:\sqlite3\db.sqlite')

cur = conn.cursor()

query_select = ''' 
SELECT title, want_to_read
FROM books
WHERE author LIKE 'John R. R. Tolkien' 
'''

cur.execute(query_select)
rows = cur.fetchall()

print('Row SQL query:', rows)

query_update = '''
UPDATE books
SET want_to_read=True
WHERE title='The Hobbit' 
'''

cur.execute(query_update)

conn.commit()

cur.execute(query_select)
rows = cur.fetchall()
print('Updated:', rows)

conn.close()



import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO posts VALUES ('testni post I', 'To je vsebina testenga posta')")
    c.execute("INSERT INTO posts VALUES  ('testni post II', 'To je vsebina drugega testnega posta')")
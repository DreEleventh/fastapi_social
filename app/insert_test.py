import psycopg2
import time

from psycopg2.extras import RealDictCursor


# Number of rows to add in each batch
n = 1000

# Generate single INSERT statement
single_query = """INSERT INTO post (user_id, post_text)
VALUES (1, 'All work and no play makes Jack a dull boy.');"""

# Generate one Big query
big_query = "INSERT INTO post (user_id, post_text) VALUES "
for i in range(n):
    big_query += " (1, 'All work and no play makes Jake a dull boy.'),"
big_query = big_query.strip(',') + ';'

conn = psycopg2.connect(
    host='localhost',
    database='chitter',
    user='postgres',
    password='ZamBase089')
cursor = conn.cursor()

# Time the 'n' individual queries
start_time = time.time()
for i in range(n):
    cursor.execute(single_query)
conn.commit()

stop_time = time.time()
print(f"{n} individual queries took {stop_time - start_time}")


# Time the Big query
start_time = time.time()
cursor.execute(big_query)
stop_time = time.time()
print(f"The query with {n} rows took {stop_time - start_time}")

cursor.close()
conn.close()


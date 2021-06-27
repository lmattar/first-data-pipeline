import psycopg2
import time

time.sleep(10)
conn = psycopg2.connect("host=pg_container dbname=jjoo user=postgres password=postgres")
cur = conn.cursor()
with open('/tmp/countries.csv', 'r') as f:
    # Notitce that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur.copy_from(f, 'countries', sep=',')

conn.commit()

##############################

cur2 = conn.cursor()
with open('/tmp/medals.csv', 'r', encoding='latin_1') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    cur2.copy_from(f, 'medals', sep=',')

conn.commit()


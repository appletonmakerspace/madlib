import os
from flask import Flask
import psycopg2
from urllib.parse import urlparse

url = urlparse(os.environ["DATABASE_URL"])

# Connect to a database
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Create a table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Insert test data
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
print(cur.fetchone())

# Make the changes to the database persistent
conn.commit()

# Close the cursor and the connection to the database
cur.close()
conn.close()


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

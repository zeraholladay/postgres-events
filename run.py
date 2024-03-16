import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Create a new database connection to listen for notifications
listen_conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="localdevelopmentonly",
    host="postgres",
    port=5432
)
listen_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create a cursor to execute SQL commands
cur = listen_conn.cursor()

# Add the channel to listen to
channel_name = 'my_channel'
cur.execute(sql.SQL("LISTEN {}").format(sql.Identifier(channel_name)))

print(f"Listening to channel '{channel_name}'...")

# Loop indefinitely to receive notifications
while True:
    listen_conn.poll()
    while listen_conn.notifies:
        notify = listen_conn.notifies.pop(0)
        print(f"Received notification: {notify.payload}")

# Close the connections
cur.close()
listen_conn.close()

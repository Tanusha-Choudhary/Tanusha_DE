import snowflake.connector
conn = snowflake.connector.connect(
    user="Tanusha",
    password="Sheena@123456789",
    account="jv08206.ap-southeast-7.aws",
    warehouse="COMPUTE_WH",
    database="FIRST_DB",
    schema="PUBLIC"
)
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders
                (order_id INTEGER,
               amount INTEGER,
                country STRING)
    """)
# INSERT DATA
try:
    cursor.execute(
    """
    INSERT INTO orders (order_id,amount,country) 
    VALUES (%s,%s,%s)
    """,(4,400,"AUS")
                   )
    print("data inserted")
except Exception as e:
    print(e)
# Select data from table
cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
conn.close()
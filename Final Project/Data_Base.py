import mysql.connector

# Connect to MySQL Server (Update with your credentials)
conn = mysql.connector.connect(
    host="localhost",       # Change if not local
    user="Himanshu",            # Your MySQL username
    password="Himanshu2006",
    database="bank_system" # Your MySQL password
)

cursor = conn.cursor()
print("Data Addedd Successfully !!")

# # Create database if not exists
# cursor.execute("CREATE DATABASE IF NOT EXISTS bank_system")
# cursor.execute("USE bank_system")

# # Create customers table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS customers (
#     customer_id INT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     address TEXT,
#     phone VARCHAR(15)
# )
# """)

# # Create accounts table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS accounts (
#     account_number INT PRIMARY KEY,
#     customer_id INT,
#     balance DECIMAL(10, 2) DEFAULT 0,
#     account_type VARCHAR(50),
#     interest_rate DECIMAL(4, 2),
#     FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
# )
# """)

# # Create transactions table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS transactions (
#     transaction_id INT AUTO_INCREMENT PRIMARY KEY,
#     account_number INT,
#     txn_type VARCHAR(10),
#     amount DECIMAL(10, 2),
#     timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (account_number) REFERENCES accounts(account_number)
# )
# """)

# conn.commit()
# conn.close()

# print("MySQL database and tables created successfully.")
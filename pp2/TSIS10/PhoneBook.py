import psycopg2

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="20030707",
    host="localhost",
    port="5432"
)


cur = conn.cursor()

cur.execute("""
CREATE TABLE Contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100),
    date_created TIMESTAMP NOT NULL DEFAULT NOW(),
    date_modified TIMESTAMP NOT NULL DEFAULT NOW()
);
""")

cur.execute("""
CREATE TABLE Addresses (
    id SERIAL PRIMARY KEY,
    contact_id INTEGER NOT NULL REFERENCES Contacts(id),
    street_address VARCHAR(100) NOT NULL
);
""")

conn.commit()

cur.execute("""
INSERT INTO Contacts (first_name, last_name, phone, email)
VALUES ('John', 'Doe', '555-1234', 'johndoe@email.com');
""")

cur.execute("""
INSERT INTO Addresses (contact_id, street_address)
VALUES (1, '123 Main St');
""")

conn.commit()

cur.execute("""
UPDATE Contacts
SET phone = '555-4321', date_modified = NOW()
WHERE id = 1;
""")

cur.execute("""
SELECT Contacts.first_name, Contacts.last_name, Addresses.street_address
FROM Contacts
LEFT JOIN Addresses ON Contacts.id = Addresses.contact_id;
""")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("""
DELETE FROM Contacts WHERE first_name = 'John';
""")

conn.commit()

cur.close()
conn.close()
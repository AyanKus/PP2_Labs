-- CREATE DATABASE "PhoneBook"
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'Russian_Russia.1251'
--     LC_CTYPE = 'Russian_Russia.1251'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE Contacts (
--     id SERIAL PRIMARY KEY,
--     first_name VARCHAR(50) NOT NULL,
--     last_name VARCHAR(50) NOT NULL,
--     phone VARCHAR(20) NOT NULL,
--     email VARCHAR(100),
--     date_created TIMESTAMP NOT NULL DEFAULT NOW(),
--     date_modified TIMESTAMP NOT NULL DEFAULT NOW()
-- );

-- CREATE TABLE Addresses (
--     id SERIAL PRIMARY KEY,
--     contact_id INTEGER NOT NULL REFERENCES Contacts(id),
--     street_address VARCHAR(100) NOT NULL
-- );

-- INSERT INTO Contacts (first_name, last_name, phone, email)
-- VALUES ('Issatay', 'Sh', '123-4567', 'issa@email.com');

-- INSERT INTO Addresses (contact_id, street_address)
-- VALUES (1, 'DORM, KBTU');

-- UPDATE Contacts
-- SET phone = '987-6543', date_modified = NOW()
-- WHERE id = 1;

-- SELECT Contacts.first_name, Contacts.last_name, Addresses.street_address
-- FROM Contacts
-- LEFT JOIN Addresses ON Contacts.id = Addresses.contact_id;

-- DELETE FROM Contacts WHERE first_name = 'Issatay'

-- COPY Contacts(first_name, last_name, phone, email, date_created, date_modified)
-- FROM 'C:\Users\Asus\Desktop\Issatay\Programming\Python\TSIS\TSIS10\contacts.csv'
-- DELIMITER ',' CSV HEADER;

-- CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
-- RETURNS TABLE (
--     id INT,
--     first_name TEXT,
--     last_name TEXT,
--     phone TEXT
-- ) AS $$
-- BEGIN
--     RETURN QUERY SELECT * FROM contacts
--     WHERE first_name ILIKE 'Issatay' || pattern || 'Issa'
--     OR last_name ILIKE 'Sh' || pattern || 'Sheg'
--     OR phone ILIKE '987-6543' || pattern || '123-3456';
-- END;
-- $$ LANGUAGE plpgsql;


-- CREATE OR REPLACE PROCEDURE upsert_contacts(
--     first_name TEXT,
--     last_name TEXT,
--     phone TEXT
-- )
-- AS $$
-- BEGIN
--     IF EXISTS (SELECT 1 FROM contacts WHERE first_name = upsert_contacts.first_name) THEN
--         UPDATE contacts SET phone = upsert_contacts.phone
--         WHERE first_name = upsert_contacts.first_name;
--     ELSE
--         INSERT INTO contacts (first_name, last_name, phone)
--         VALUES (upsert_contacts.first_name, upsert_contacts.last_name, upsert_contacts.phone);
--     END IF;
-- END;
-- $$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_multiple_contacts(
    users contacts[],
    OUT invalid_contacts contacts[]
)
AS $$
DECLARE
    user contacts;
BEGIN
    invalid_contacts := ARRAY[]::contacts[];
    FOREACH user IN ARRAY insert_multiple_contacts.users
    LOOP
        IF LENGTH(user.phone) <> 10 THEN
            invalid_contacts := array_append(invalid_contacts, user);
        ELSE
            INSERT INTO contacts (first_name, last_name, phone)
            VALUES (user.first_name, user.last_name, user.phone);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;
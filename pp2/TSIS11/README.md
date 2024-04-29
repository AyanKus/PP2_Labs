-- Function to search records by pattern
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE (
    id SERIAL,
    first_name TEXT,
    last_name TEXT,
    phone TEXT
) AS $$
BEGIN
    RETURN QUERY SELECT * FROM phonebook
    WHERE first_name ILIKE '%' || pattern || '%'
    OR last_name ILIKE '%' || pattern || '%'
    OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Procedure to insert or update user
CREATE OR REPLACE PROCEDURE upsert_phonebook(
    first_name TEXT,
    last_name TEXT,
    phone TEXT
)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = upsert_phonebook.first_name) THEN
        UPDATE phonebook SET phone = upsert_phonebook.phone
        WHERE first_name = upsert_phonebook.first_name;
    ELSE
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (upsert_phonebook.first_name, upsert_phonebook.last_name, upsert_phonebook.phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Procedure to insert multiple users
CREATE OR REPLACE PROCEDURE insert_multiple_phonebook(
    users phonebook[],
    OUT invalid_phonebook phonebook[]
)
AS $$
DECLARE
    user phonebook;
BEGIN
    invalid_phonebook := ARRAY[]::phonebook[];
    FOREACH user IN ARRAY insert_multiple_phonebook.users
    LOOP
        IF LENGTH(user.phone) <> 10 THEN
            invalid_phonebook := array_append(invalid_phonebook, user);
        ELSE
            INSERT INTO phonebook (first_name, last_name, phone)
            VALUES (user.first_name, user.last_name, user.phone);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Function to query phonebook with pagination
CREATE OR REPLACE FUNCTION get_phonebook(
    limit INTEGER,
    offset INTEGER
)
RETURNS TABLE (
    id SERIAL,
    first_name TEXT,
    last_name TEXT,
    phone TEXT
) AS $$
BEGIN
    RETURN QUERY SELECT * FROM phonebook
    ORDER BY last_name, first_name
    LIMIT limit
    OFFSET offset;
END;
$$ LANGUAGE plpgsql;

-- Procedure to delete user by name or phone
CREATE OR REPLACE PROCEDURE delete_phonebook(
    name TEXT,
    phone TEXT
)
AS $$
BEGIN
    IF name IS NOT NULL THEN
        DELETE FROM phonebook WHERE first_name = delete_phonebook.name;
    ELSEIF phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = delete_phonebook.phone;
    END IF;
END;
$$ LANGUAGE plpgsql;

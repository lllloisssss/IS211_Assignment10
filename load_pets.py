load_pets.py
IS211 Assignment 10 - Part 2

Creates pets.db with the required schema and loads all
provided data into the person, pet, and person_pet tables.
"""

import sqlite3

DB_FILE = "pets.db"

# ── Schema ─────────────────────────────────────────────────────────────────
CREATE_TABLES = """
CREATE TABLE IF NOT EXISTS person (
    id          INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    age         INTEGER
);

CREATE TABLE IF NOT EXISTS pet (
    id      INTEGER PRIMARY KEY,
    name    TEXT,
    breed   TEXT,
    age     INTEGER,
    dead    INTEGER
);

CREATE TABLE IF NOT EXISTS person_pet (
    person_id   INTEGER,
    pet_id      INTEGER
);
"""

# ── Data ───────────────────────────────────────────────────────────────────
PEOPLE = [
    (1, 'James',   'Smith',   41),
    (2, 'Diana',   'Greene',  23),
    (3, 'Sara',    'White',   27),
    (4, 'William', 'Gibson',  23),
]

PETS = [
    (1, 'Rusty', 'Dalmation',        4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max',   'Cocker Spaniel',   1, 0),
    (4, 'Rocky', 'Beagle',           7, 0),
    (5, 'Rufus', 'Cocker Spaniel',   1, 0),
    (6, 'Spot',  'Bloodhound',       2, 1),
]

PERSON_PETS = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6),
]


def main():
    conn = sqlite3.connect(DB_FILE)
    cur  = conn.cursor()

    # Create tables
    conn.executescript(CREATE_TABLES)
    print("Tables created.")

    # Insert data
    cur.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", PEOPLE)
    cur.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", PETS)
    cur.executemany("INSERT INTO person_pet VALUES (?, ?)", PERSON_PETS)

    conn.commit()
    conn.close()

    print(f"Data loaded successfully into '{DB_FILE}'.")
    print(f"  {len(PEOPLE)} people inserted.")
    print(f"  {len(PETS)} pets inserted.")
    print(f"  {len(PERSON_PETS)} person-pet relationships inserted.")


if __name__ == "__main__":
    main()

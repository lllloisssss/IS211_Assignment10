"""
query_pets.py
IS211 Assignment 10 - Part 2

Connects to pets.db, asks the user for a person's ID,
and prints that person's info along with all their pets.
Enter -1 to exit.

Purpose of person_pet table:
  The person_pet table is a "junction table" (also called a bridge or
  associative table). It models the many-to-many relationship between
  people and pets — a person can own multiple pets, and (in theory) a
  pet could be owned by multiple people. Instead of storing pet info
  directly on the person row (or vice versa), person_pet links them
  by storing pairs of person_id and pet_id.
"""

import sqlite3
import sys

DB_FILE = "pets.db"


def get_person(cur, person_id):
    """Return a person row by ID, or None if not found."""
    cur.execute(
        "SELECT id, first_name, last_name, age FROM person WHERE id = ?",
        (person_id,)
    )
    return cur.fetchone()


def get_pets_for_person(cur, person_id):
    """Return all pets belonging to the given person."""
    cur.execute("""
        SELECT pt.name, pt.breed, pt.age, pt.dead
        FROM pet pt
        JOIN person_pet pp ON pt.id = pp.pet_id
        WHERE pp.person_id = ?
    """, (person_id,))
    return cur.fetchall()


def display_person_and_pets(person, pets):
    """Print formatted info about a person and their pets."""
    pid, first, last, age = person
    print(f"\n{first} {last}, {age} years old.")

    if not pets:
        print("  This person has no pets on record.")
        return

    print("  Pets:")
    for name, breed, pet_age, dead in pets:
        status = "deceased" if dead else f"{pet_age} years old"
        print(f"    - {first} {last} owned {name}, a {breed}, that was {status}.")


def main():
    try:
        conn = sqlite3.connect(DB_FILE)
    except sqlite3.OperationalError as e:
        print(f"ERROR: Could not open '{DB_FILE}'. Did you run load_pets.py first?")
        print(f"Details: {e}")
        sys.exit(1)

    cur = conn.cursor()
    print("=" * 45)
    print("  Pet Database Lookup")
    print("  (Enter -1 to exit)")
    print("=" * 45)

    while True:
        try:
            user_input = input("\nEnter a person's ID: ").strip()
            person_id  = int(user_input)
        except ValueError:
            print("Please enter a valid integer ID.")
            continue

        if person_id == -1:
            print("Goodbye!")
            break

        person = get_person(cur, person_id)

        if person is None:
            print(f"ERROR: No person found with ID {person_id}.")
        else:
            pets = get_pets_for_person(cur, person_id)
            display_person_and_pets(person, pets)

    conn.close()


if __name__ == "__main__":
    main()

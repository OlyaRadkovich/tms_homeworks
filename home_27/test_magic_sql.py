import pytest
import sqlite3
import random

DB_NAME = "hogwarts.db"
TABLE_NAME = "Gryffindor"


@pytest.fixture
def db_connection():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        f"create table {TABLE_NAME} ("
        "first_name text, "
        "last_name text, "
        "blood_status text, "
        "born int"
        ");"
    )
    connection.commit()

    cursor.execute(
        f"insert into {TABLE_NAME} values "
        f"('Harry', 'Potter', 'Half-blood', 1980),"
        f"('Ronald', 'Weasley', 'Pure-blood', 1979),"
        f"('Hermione', 'Granger', 'Muggle-born', 1979),"
        f"('Neville', 'Longbottom', 'Pure-blood', 1980),"
        f"('Rubeus', 'Hagrid', 'Half-breed', 1928);"
    )
    connection.commit()

    yield connection
    cursor.execute(f"drop table {TABLE_NAME};")
    connection.commit()
    connection.close()


@pytest.mark.usefixtures("db_connection")
class TestGryffindor:

    def test_find_by_year(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(f"select * from Gryffindor where born = 1980;")
        results = cursor.fetchall()
        assert results == [
            ("Harry", "Potter", "Half-blood", 1980),
            ("Neville", "Longbottom", "Pure-blood", 1980),
        ]

    def test_find_oldest(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(f"select * from Gryffindor order by born asc;")
        result = cursor.fetchone()
        assert result == ("Rubeus", "Hagrid", "Half-breed", 1928)

    def test_add_random(self, db_connection):
        cursor = db_connection.cursor()
        first_name = random.choice(["Alice", "Bob", "Charlie", "David", "Eve"])
        last_name = random.choice(["Smith", "Jones", "Brown", "Green", "White"])
        blood_status = random.choice(["Pure-blood", "Half-blood", "Muggle-born"])
        born = random.randint(1970, 2010)
        cursor.execute(
            f"insert into Gryffindor values "
            f"('{first_name}', '{last_name}', '{blood_status}', {born});"
        )
        db_connection.commit()
        cursor.execute(
            f"select * from Gryffindor where first_name = '{first_name}' and last_name = '{last_name}';"
        )
        results = cursor.fetchall()
        assert results == [(first_name, last_name, blood_status, born)]
        cursor.execute(
            f"delete from Gryffindor where first_name = '{first_name}' and last_name = '{last_name}';"
        )
        db_connection.commit()

    def test_exception_by_year(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(f"select * from Gryffindor where born <> 1980;")
        results = cursor.fetchall()
        assert results == [("Ronald", 'Weasley', "Pure-blood", 1979),
                           ("Hermione", "Granger", "Muggle-born", 1979),
                           ("Rubeus", "Hagrid", "Half-breed", 1928)]

    def test_half_blood_and_breed(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute(f"select * from Gryffindor where blood_status in ('Half-blood','Half-breed')")
        results = cursor.fetchall()
        assert results == [("Harry", "Potter", "Half-blood", 1980), ("Rubeus", "Hagrid", "Half-breed", 1928)]


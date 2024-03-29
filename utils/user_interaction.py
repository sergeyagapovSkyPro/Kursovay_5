import psycopg2
from src.hh_vacancy_parser import HHVacancyParsing
from src.db_modyle import DBModyle
from config import config


def user_interaction(value, db_name):
    """Метод получает данные от пользователя сортирует и записывает их в БД"""
    HHVacancyParsing(value)
    module = DBModyle(db_name)
    module.create_tables()
    module.full_tables(value)


def delete_database(db_name):
    """Метод удаления БД"""
    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"DROP DATABASE {db_name}")
    cursor.close()
    conn.close()


def create_database(db_name):
    """Метод создания БД"""
    conn = psycopg2.connect(dbname="postgres", **config())
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f" DROP DATABASE IF EXISTS {db_name}")
    cursor.execute(f"CREATE DATABASE {db_name}")
    cursor.close()
    conn.close()


if __name__ == '__main__':
    delete_database("python")

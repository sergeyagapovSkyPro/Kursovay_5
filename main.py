from utils.user_interaction import user_interaction, delete_database, create_database
from src.db_manager import DBManager


db_name = input("Введите название базы данных:\n")
create_database(db_name)
db_manager = DBManager(db_name)
user_input = input("Введите название компании через запятую, для просмотра.\n"
                   "Если не указать вакансии, по умолчании программа вернет 10 первых.\n").split(",")
user_interaction(user_input, db_name)
print("Список компаний сохранен в базе данных\n")

try:
    while True:
        print('Выберите чисто от 1 до 5:\n'
              '1. Получить список всех компаний и количество вакансий у каждой компании\n'
              '2. Получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки '
              'на вакансию\n'
              '3. Получить среднюю зарплату по вакансиям\n'
              '4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n'
              '5. Получить список всех вакансий, в названии которых содержатся переданные в метод слова, '
              'например python.\n')
        number_user = int(input().strip())
        if number_user == 1:
            db_manager.get_companies_and_vacancies_count()
        elif number_user == 2:
            db_manager.get_all_vacancies()
        elif number_user == 3:
            db_manager.get_avg_salary()
        elif number_user == 4:
            db_manager.get_vacancies_with_higher_salary()
        elif number_user == 5:
            word_user = input("Введите название вакансии.")
            db_manager.get_vacancies_with_keyword(word_user)
        elif number_user not in range(1, 6):
            exit_user = input("Неверные данные!\n"
                              "Введите 0 для выхода или повторите ввод.\n").strip()
            if exit_user == '0':
                break
            else:
                continue
        user_question = input("Желаете продолжить?\n"
                              "1 - Да\n"
                              "2 - Нет\n").strip()
        if user_question == "1":
            continue
        else:
            break
finally:
    db_manager.conn.close()
    print("Удаление данных с базы данных\n")
    delete_database(db_name)
    print("Конец")

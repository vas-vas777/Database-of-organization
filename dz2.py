import json
import os


class Employee:
    def __init__(self, FIO, birthday, SNILS, post='', number_of_hours='', date_of_start=''):
        self.birthday = birthday
        self.FIO = FIO
        self.post = post
        self.number_of_hours = number_of_hours
        self.SNILS = SNILS
        self.date_of_start = date_of_start

    def data_of_employee(self):
        return {self.SNILS: [self.FIO, self.birthday, self.post, self.number_of_hours, self.date_of_start]}


class Department:
    def __init__(self, name_of_department='', description='', vacancy_of_depart=''):
        self.name_of_department = name_of_department
        self.description = description
        self.vacancy_of_depart = vacancy_of_depart
        self.dict_from_file = dict()
        if self.description != '' and self.vacancy_of_depart != '':
            with open("file2.json", "a") as file_json:
                if os.stat(file_json.name).st_size == 0:
                    json.dump({self.name_of_department: {"description": self.description,
                                                         "vacancy": self.vacancy_of_depart, "employees": {}}},
                              file_json, ensure_ascii=False, indent=3)
                else:
                    with open("file2.json", "r") as file:
                        self.dict_from_file = json.load(file)
                        if self.dict_from_file.get(self.name_of_department) is None:
                            self.dict_from_file.update({self.name_of_department: {"description": self.description,
                                                                                  "vacancy": self.vacancy_of_depart,
                                                                                  "employees": {}}})
                            with open("file2.json", "w") as filejson:
                                json.dump(self.dict_from_file, filejson, ensure_ascii=False, indent=3)
                        else:
                            print("Такой отдел уже есть")

    def print_data_of_employees_from_department(self):
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            for key, value in self.dict_from_file.get(self.name_of_department).get("employees").items():
                print(key, value[0], value[1])

    def search_employee_by_SNILS(self, SNILS):
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            for key in self.dict_from_file.keys():
                value = self.dict_from_file.get(key).get("employees").get(SNILS)
                if value is not None:
                    print(SNILS, value)
                    break
            print("Такого сотрудника нет")

    def search_employee_by_FIO(self, FIO):
        flag = 0
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            for key in self.dict_from_file.keys():
                for snils in self.dict_from_file.get(key).get("employees").keys():
                    value = self.dict_from_file.get(key).get("employees").get(snils)
                    if value[0] == FIO:
                        print(snils, value)
                        flag = 1
        if flag == 0:
            print("Такого сотрудника нет")

    def change_data_of_employee_by_SNILS(self, SNILS):
        flag = 0
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            for key in self.dict_from_file.keys():
                value = self.dict_from_file.get(key).get("employees").get(SNILS)
                if value is not None:
                    FIO = input("Введите ФИО:")
                    birthday = input("Введите дату рождения:")
                    post = input("Введите должность:")
                    employee = Employee(FIO, birthday, SNILS, post, value[3], value[4])
                    self.dict_from_file.get(key).get("employees").update(employee.data_of_employee())
                    with open("file2.json", "w") as filejson:
                        json.dump(self.dict_from_file, filejson, ensure_ascii=False, indent=3)
                        flag = 1
                    break
        if flag == 0:
            print("Такого сотрудника нет")

    def search_and_delete_by_SNILS(self, SNILS):
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            for key in self.dict_from_file.keys():
                try:
                    self.dict_from_file.get(key).get("employees").pop(SNILS)
                    with open("file2.json", "w") as filejson:
                        json.dump(self.dict_from_file, filejson, ensure_ascii=False, indent=3)
                    break
                except:
                    print("Такого сотрудника нет")

    def print_name_of_departments(self):
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            print(self.dict_from_file.keys())

    def change_data_of_department(self):
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            if self.dict_from_file.get(self.name_of_department) is not None:
                description_of_department = input("Введите описание отдела:")
                vacancy_of_depart = input("Вакансии отдела + ставки:")
                self.dict_from_file.get(self.name_of_department).update({"description": description_of_department})
                self.dict_from_file.get(self.name_of_department).update({"vacancy": vacancy_of_depart})
                with open("file2.json", "w") as filejson:
                    json.dump(self.dict_from_file, filejson, ensure_ascii=False, indent=3)
            else:
                print("такого отдела нет")

    def del_department(self):
        with open("file2.json", "r") as file_json:
            self.dict_from_file = json.load(file_json)
            dict_of_employees = self.dict_from_file.get(self.name_of_department).get("employees")
            print(dict_of_employees)
            try:
                self.dict_from_file.pop(self.name_of_department)
                print(self.dict_from_file)
                if self.dict_from_file.get("employees") is None:
                    self.dict_from_file.update({"employees": dict_of_employees})
                else:
                    self.dict_from_file.get("employees").update(dict_of_employees)
                print(self.dict_from_file)
                with open("file2.json", "w") as filejson:
                    json.dump(self.dict_from_file, filejson, ensure_ascii=False, indent=3)
            except:
                print("такого отдела нет")

    def search_existing_department(self):
        try:
            with open("file2.json", "r") as file_json:
                self.dict_from_file = json.load(file_json)
                if self.dict_from_file.get(self.name_of_department) is not None:
                    return True
                else:
                    return False
        except:
            return False

    def add_employee_to_department(self):
        with open("file2.json", "r") as file:
            self.dict_from_file = json.load(file)
            if self.name_of_department in self.dict_from_file.keys():
                FIO = input("Введите ФИО:")
                birthday = input("Введите дату рождения:")
                SNILS = input("Введите СНИЛС:")
                post = input("Введите должность:")
                number_of_hours = input("Введите ставку:")
                date_of_start = input("Введите дату приема на работу:")
                employee = Employee(FIO, birthday, SNILS, post, number_of_hours, date_of_start)
                with open("file2.json", "r") as file_json:
                    self.dict_from_file = json.load(file_json)
                    self.dict_from_file.get(self.name_of_department).get("employees").update(
                        employee.data_of_employee())
                with open("file2.json", "w") as filejson:
                    json.dump(self.dict_from_file, filejson, ensure_ascii=False, indent=3)
            else:
                print("Такого отдела нет")


if __name__ == "__main__":
    while True:
        str = input("Введите 1-(Добавить отдел), \n"
                    "2-(Добавить сотрудника в отдел), \n"
                    "3-(Вывод всех сотрудников отдела), \n"
                    "4-(Поиск сотрудника по СИНЛС), \n"
                    "5-(Поиск сотрудников по ФИО), \n"
                    "6-(Поиск сотрудника по СНИЛС для изменения данных), \n"
                    "7-(Поиск сотрудника по СНИЛС и удалению из БД), \n"
                    "8-(Вывод названий всех отделов), \n"
                    "9-(Изменение данных отдела), \n"
                    "10-(Удаление данных отдела, сотрудники не удаляются), \n"
                    "0-(Выход из программы):")
        if str == '1':
            name_department = input("Введите название отдела:")
            depart = Department(name_department)
            if depart.search_existing_department() is True:
                print("Такой отдел уже есть")
            else:
                description_of_department = input("Введите описание отдела:")
                vacancy_of_depart = input("Вакансии отдела + ставки:")
                department = Department(name_department, description_of_department, vacancy_of_depart)
        elif str == '2':
            name_depart = input("Введите название отдела:")
            department = Department(name_depart)
            department.add_employee_to_department()
        elif str == '3':
            name_depart = input("Введите название отдела:")
            department = Department(name_depart)
            department.print_data_of_employees_from_department()
        elif str == '4':
            SNILS = input("Введите СНИЛС:")
            department = Department()
            department.search_employee_by_SNILS(SNILS)
        elif str == '5':
            FIO = input("Введите ФИО:")
            department = Department()
            department.search_employee_by_FIO(FIO)
        elif str == '6':
            SNILS = input("Введите СНИЛС:")
            department = Department()
            department.change_data_of_employee_by_SNILS(SNILS)
        elif str == '7':
            SNILS = input("Введите СНИЛС:")
            department = Department()
            department.search_and_delete_by_SNILS(SNILS)
        elif str == '8':
            department = Department()
            department.print_name_of_departments()
        elif str == '9':
            name_depart = input("Введите название отдела:")
            department = Department(name_depart)
            department.change_data_of_department()
        elif str == '10':
            name_depart = input("Введите название отдела:")
            department = Department(name_depart)
            department.del_department()
        elif str == '0':
            print("Выход")
            break
        else:
            print("Не корректный ввод. Выход")
            break

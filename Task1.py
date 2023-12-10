# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union
class Car:
    def __init__(self, max_speed: Union[int, float], volume: Union[int, float]):
        """
            Создание и подготовка к работе объекта "Машина"

                :param max_speed: Максимальаня скорость
                :param volume: Объем двигателя

                Примеры:
                >>> car = Car(120, 80)  # инициализация экземпляра класса
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if not 0<= max_speed <= 300:
            raise ValueError("Максимальная скорость должна быть положительным числом не более 300")
        self.max_speed = max_speed

        if not isinstance(volume, (int, float)):
            raise TypeError("Кол-во бензина должно быть int или float")
        if not 0 <= volume <= 100:
            raise ValueError("Кол-во бензина должно быть положительным числом не более 100 ")
        self.volume = volume
    def is_empty_bak(self) -> bool:
        """
        Функция которая проверяет является ли бензобак пустым

        :return: Является ли бензобак пустым

        Примеры:
        >>> car = Car(120, 80)
        >>> car.is_empty_bak()
        """
        ...

    def add_benz_to_bak(self, benz: float) -> None:
        """
        Добавление бензина в бензобак.
        :param benz: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемого бензина превышает свободное место в баке, то вызываем ошибку

        Примеры:
        >>> car = Car(120, 80)
        >>> car.add_benz_to_bak(10)
        """
        if not isinstance(benz, (int, float)):
            raise TypeError("Добавляемый бензин должен быть типа int или float")
        if benz < 0:
            raise ValueError("Добавляемый бензин должен быть положительным числом")
        ...

class Student:
    def __init__(self,number: int, grade: int):
        """
                    Создание и подготовка к работе объекта "Студент"

                        :param number: Номер в списке
                        :param grade: Оценка

                        Примеры:
                        >>> student = Student(16, 4)  # инициализация экземпляра класса
                """
        if not isinstance(number, int):
            raise TypeError("Номер в списке должен быть типа int")
        if not 0<= number <= 300:
            raise ValueError("Номер в списке должен быть положительным числом не более 30")
        self.number = number

        if not isinstance(grade, int):
            raise TypeError("Оценка должна быть int")
        if not 0 <= grade <= 100:
            raise ValueError("Оценка должна быть положительным числом от 2 до 5 включительно")
        self.grade = grade

    def increase_in_grade(self, dop: int) -> None:
        """
        Повышение оценки.
        :param dop: То на сколько повышаем оценку

        :raise ValueError: Если велечина добавляемой оценки больше разрешенной то вызываем ошибку

        Примеры:
        >>> student = Student(10, 3)
        >>> student.increase_in_grade(1)
        """
        if not isinstance(dop, int):
            raise TypeError("Добавляемая оценка должна быть типа int")
        if not 0 < dop <= 3:
            raise ValueError("Добавляемая оценка должна положительным числом от 1 до 3")
        ...
    def downgrade(self, dop: int) -> None:
        """
        Повышение оценки.
        :param dop: То на сколько понижаем оценку

        :raise ValueError: Если велечина понижаемой оценки больше разрешенной то вызываем ошибку
        :return: То на сколько была понижена оценка
        Примеры:
        >>> student = Student(10, 3)
        >>> student.downgrade(1)
        """
        if not isinstance(dop, int):
            raise TypeError("Понижаемая оценка должна быть типа int")
        if not 0 < dop <= 3:
            raise ValueError("Понижаемая оценка должна положительным числом от 1 до 3")
        ...

class Employee:
    def __init__(self, name: str, salary: Union[int, float]):
        """
                    Создание и подготовка к работе объекта "Сотрудник"

                        :param name: Имя сотрудника
                        :param salary: Зарплата

                        Примеры:
                        >>> employee = Employee("Artem", 30000)  # инициализация экземпляра класса
                """
        if not isinstance(salary, (int, float)):
            raise TypeError("Зарплата должна быть типа int или float")
        if salary < 0:
            raise ValueError("Зарплата должна быть положительным числом")
        self.salary = salary
    def salary_increase(self, number: float) -> None:
        """
                Повышение зарплаты.
                :param number: Число на которое повышаем зарплату
                Примеры:
                >>> employee = Employee("Artem", 30000)
                >>> employee.salary_increase(10000)
                """
        ...
    def salary_reduction(self,number: float)-> None:
        """
               Понижение зарплаты.
               :param number: Число на которое понижаем зарплату

               :raise ValueError: Если количество понижаемой зарплаты превышает саму зарплату, то вызываем ошибку

               Примеры:
               >>> employee = Employee("Artem", 30000)
               >>> employee.salary_reduction(2000)
               """
        if not isinstance(number, (int, float)):
            raise TypeError("Число должно быть типа int или float")
        if number > self.salary:
            raise ValueError("Число должно быть меньше зарплаты")
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
    doctest.testmod()
from lib.models import *
import pickle


def verification(*args) -> bool:
    print('------------------------------')
    [print(x) for x in args]
    print('------------------------------')
    answer = input('Проверте данные (y/n)? - ')
    return answer == 'y' or answer == 'Y'


class MainController(object):

    def __init__(self):
        self.__catalog = Catalog('Library')
        self.__storage = 'catalog.dat'
        self.load_data()

    def load_data(self) -> None:
        try:
            with open(self.__storage, 'rb') as file:
                self.__catalog = pickle.load(file)
        except FileNotFoundError and EOFError:
            self.save_data()
            self.load_data()

    def save_data(self) -> None:
        with open('catalog.dat', 'wb') as f:
            pickle.dump(self.__catalog, f)

    def display_categories(self) -> list:
        categories_list = self.__catalog.types
        count = 0
        print('-------------------------------')
        for category in categories_list:
            count += 1
            print(f'{count}. {category.get_name()}')
        print('-------------------------------')
        return categories_list

    def select_by_category(self) -> None:
        category = input('Введите название категории: ')
        pos = self.__catalog.find_category(category)
        if pos == -1:
            print(f'Категория {category} - не найдена!')
        else:
            self.__catalog.types[pos].display()

    def show_list_author(self):
        for cat in self.__catalog.types:
            print(f'{cat.get_name()}:')
            for book in cat.category:
                print(f'{book.get_author()} - {book.get_name()}')

    def select_by_author(self):
        target = input('Введите имя автора: ')
        print(f'{target}: ')
        for category in self.__catalog.types:
            for book in category.category:
                if book.get_author() == target:
                    print(f'    {book.get_name()}')

    def select_by_amount(self):
        target = None
        try:
            target = int(input('Введите количество: '))
        except ValueError:
            print('Количество должно быть целым числом!')
        print(f'В количестве - {target}: ')
        for category in self.__catalog.types:
            for book in category.category:
                if book.amount == target:
                    print(f'    {book.get_author()} - {book.get_name()}')

    def add_category(self, category=None):
        print('-----------Добавление категории-----------')
        if category is None:
            category = input('Введите название категории: ')
        pos = self.__catalog.find_category(category)
        if pos == -1:
            self.__catalog.add_category(Category(category))
            self.save_data()
            self.load_data()
        else:
            print('Такая категория уже существует!')
            self.add_category()

    def del_category(self, category=None):
        print('-----------Удаление категории-----------')
        if category is None:
            category = input('Введите название категории: ')
        pos = self.__catalog.find_category(category)
        if pos != -1:
            self.__catalog.del_category(category)
            self.save_data()
            self.load_data()
        else:
            print('Такой категории не существует!')
            self.add_category()

    def add_producer(self):
        target_book = input('Введите название книги: ')
        target = input('Введите производителя: ')
        for category in self.__catalog.types:
            for book in category.category:
                if book.get_name() == target_book:
                    if target not in book.producer:
                        book.producer.append(target)
                    else:
                        print('Данный производитель уже имеется!')
                    self.save_data()
                    self.load_data()

    def del_producer(self):
        target_book = input('Введите название книги: ')
        target = input('Введите производителя: ')
        for category in self.__catalog.types:
            for book in category.category:
                if book.get_name() == target_book:
                    if target in book.producer:
                        del book.producer[book.producer.index(target)]
                        self.save_data()
                        self.load_data()
                    else:
                        print(f'{target} - не производит {target_book}')

    def add_book(self, category=None):
        name = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        producer = list(input("Введите производителей через запятую: ").split(', '))
        amount = 0
        try:
            amount = int(input('Введите количество книг: '))
        except ValueError:
            print('Количество книг должно быть целым числом.')
        if verification(name, author, producer, amount):
            book = Book(name, author, producer, amount)
            if category is None:
                categories = self.display_categories()
                if len(categories) == 0:
                    print('Категорий не найдено!')
                    self.add_category()
                    self.display_categories()
                while True:
                    category = input('Введите название категории для киниги: ')
                    if self.__catalog.find_category(category) != -1:
                        break
                    else:
                        print('Данные не верны!')
            for target in self.__catalog.types:
                if target.get_name() == category:
                    target.add_book(book)
            self.save_data()
            self.load_data()
            answer = input(f'Желаете добавить ещё одну книгу в {category}?\n'
                           f'y/n: ')
            if answer == 'Y' or answer == 'y':
                self.add_book(category)
        else:
            self.add_book()

    def del_book(self):
        target = input('Введите книгу котору нужно удалить: ')
        target_bool = False
        for category in self.__catalog.types:
            for book in category.category:
                if book.get_name() == target:
                    category.del_book(target)
                    target_bool = True
                    self.save_data()
                    self.load_data()
        if target_bool:
            print('Книга успешно удалена!')
        else:
            print('Такой книги не существует!')

    def change_amount_books(self):
        target = input('Введите название книги: ')
        target_bool = False
        for category in self.__catalog.types:
            for book in category.category:
                if book.get_name() == target:
                    print(f'{book.get_name()} - {book.amount}')
                    amount = None
                    try:
                        amount = int(input('Введите новое значение: '))
                    except ValueError:
                        print('Колчиство должно быть целым числом!')
                    book.amount = amount
                    target_bool = True
                    self.save_data()
                    self.load_data()
        if target_bool:
            print('Данные изменены!')
        else:
            print('Книга не найдена!')

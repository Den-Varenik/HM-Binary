class Book(object):

    def __init__(self, name: str, author: str, producer: list, amount: int):
        self.__name = name
        self.__author = author
        self.__producer = producer
        self.__amount = amount

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    @property
    def producer(self):
        return self.__producer

    @producer.setter
    def producer(self, producer):
        self.__producer = producer

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount: int):
        if amount >= 0:
            self.__amount = amount
        else:
            print('Недопустимое значение')

    def __str__(self):
        return f'{self.__author} / {self.__name} / {self.__producer} - {self.__amount}'


class Category(object):
    
    def __init__(self, name: str):
        self.__name = name
        self.__category = list()

    def get_name(self):
        return self.__name

    @property
    def category(self):
        return self.__category

    def add_book(self, book: Book):
        index = self.find_book(book.get_name())
        print(index)
        if index == -1:
            print('Книга добавлена')
            self.__category.append(book)
            self.display()
        else:
            print('Такая книгу уже существует!')

    def find_book(self, name):
        index = -1
        for book in self.__category:
            index += 1
            if book.get_name() == name:
                return index
        return -1

    def del_book(self, name):
        index = self.find_book(name)
        if index != -1:
            del self.__category[index]
        else:
            print(f'{name} - нету в категории {self.__name}')

    def display(self):
        print(f'\n> категория: {self.__name}')
        print('-----------------------------')
        [print(book) for book in self.__category]


class Catalog(object):

    def __init__(self, name: str):
        self.__name = name
        self.__types = list()

    @property
    def types(self):
        return self.__types

    def add_category(self, c: Category) -> None:
        if self.find_category(c.get_name()) == -1:
            self.__types.append(c)

    def find_category(self, name: str) -> int:
        index = -1
        for category in self.__types:
            index += 1
            if category.get_name() == name:
                return index
        return -1

    def del_category(self, name: str) -> None:
        index = self.find_category(name)
        if index != -1:
            del self.__types[index]
        else:
            print(f'{name} - нету в каталоге {self.__name}')

    def display(self) -> None:
        print(f'\n> каталог: {self.__name}')
        print('-----------------------------')
        [print(category) for category in self.__types]

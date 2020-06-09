from lib.models import Book, Category, Catalog
from lib.assistant import Menu
from lib.manage import MainController
from pickle import dump, load

if __name__ == '__main__':

    m = Menu()
    mc = MainController()
    while True:
        m.display()
        k = m.get_choice()

        if k == 1:
            mc.display_categories()
        elif k == 2:
            mc.select_by_category()
        elif k == 3:
            mc.show_list_author()
        elif k == 4:
            mc.select_by_author()
        elif k == 5:
            mc.select_by_amount()
        elif k == 6:
            mc.add_category()
        elif k == 7:
            mc.del_category()
        elif k == 8:
            mc.add_producer()
        elif k == 9:
            mc.del_producer()
        elif k == 10:
            mc.add_book()
        elif k == 11:
            mc.del_book()
        elif k == 12:
            mc.change_amount_books()
        elif k == 0:
            break
        else:
            print('ВЫ выбрали несуществующий вариант!')

        if not m.allow_continue():
            break

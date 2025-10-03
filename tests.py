from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Гарри Поттер', 'Оно', 'Война и мир'])
    def test_add_new_book_valid_name_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    @pytest.mark.parametrize('name, expected', [
        ('', False),
        ('Очень длинное название книги которое превышает лимит в 40 символов', False)
    ])
    def test_add_new_book_invalid_name_book_not_added(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected

    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Оно')
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Роман')
        assert collector.get_book_genre('Оно') == ''

    def test_get_book_genre_no_genre_returns_empty_string(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        assert collector.get_book_genre('Оно') == ''

    @pytest.mark.parametrize('genre, expected_count', [
        ('Ужасы', 2),
        ('Фантастика', 1),
        ('Комедии', 0)
    ])
    def test_get_books_with_specific_genre_returns_correct_books(self, genre, expected_count):
        collector = BooksCollector()
        books = {'Оно': 'Ужасы', 'Сияние': 'Ужасы', 'Марсианин': 'Фантастика'}
        for name, gen in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, gen)
        result = collector.get_books_with_specific_genre(genre)
        assert len(result) == expected_count

    def test_get_books_for_children_returns_safe_books(self):
        collector = BooksCollector()
        test_books = {
            'Оно': 'Ужасы',
            'Марсианин': 'Фантастика',
            'Том и Джерри': 'Мультфильмы'
        }
        for name, genre in test_books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        children_books = collector.get_books_for_children()
        assert 'Оно' not in children_books
        assert 'Марсианин' in children_books
        assert 'Том и Джерри' in children_books

    def test_add_book_in_favorites_valid_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        assert 'Оно' in collector.favorites

    def test_add_book_in_favorites_invalid_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.favorites

    def test_delete_book_from_favorites_book_removed(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.favorites

    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Марсианин')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == 2
        assert 'Оно' in favorites
        assert 'Марсианин' in favorites
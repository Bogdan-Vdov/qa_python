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

    def test_add_new_book_adds_book_with_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre

    def test_add_new_book_does_not_add_book_with_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.books_genre

    def test_add_new_book_does_not_add_book_with_long_name(self):
        collector = BooksCollector()
        long_name = "a" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_add_new_book_adds_only_one_instance_of_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_new_book("Гарри Поттер")
        assert len(collector.books_genre) == 1

    def test_set_book_genre_sets_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_set_book_genre_does_not_set_genre_for_nonexistent_book(self):
        collector = BooksCollector()
        collector.set_book_genre("Неизвестная книга", "Ужасы")
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_set_book_genre_does_not_set_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Неверный жанр")
        assert collector.get_book_genre("Гарри Поттер") == ""

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        assert collector.get_book_genre("Гарри Поттер") == "Фантастика"

    def test_get_books_with_specific_genre_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Шерлок Холмс")
        collector.set_book_genre("Шерлок Холмс", "Детективы")
        result = collector.get_books_with_specific_genre("Фантастика")
        assert "Гарри Поттер" in result
        assert "Шерлок Холмс" not in result

    def test_get_books_with_specific_genre_returns_empty_list_if_no_books(self):
        collector = BooksCollector()
        result = collector.get_books_with_specific_genre("Фантастика")
        assert len(result) == 0

    def test_get_books_genre_returns_current_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        books_genre = collector.get_books_genre()
        assert isinstance(books_genre, dict)
        assert "Гарри Поттер" in books_genre

    def test_get_books_for_children_excludes_age_rated_genres(self):
        collector = BooksCollector()
        collector.add_new_book("Книга ужасов")
        collector.set_book_genre("Книга ужасов", "Ужасы")
        collector.add_new_book("Книга детектива")
        collector.set_book_genre("Книга детектива", "Детективы")
        collector.add_new_book("Книга фантастики")
        collector.set_book_genre("Книга фантастики", "Фантастика")
        collector.add_new_book("Мультик")
        collector.set_book_genre("Мультик", "Мультфильмы")
        collector.add_new_book("Комедия")
        collector.set_book_genre("Комедия", "Комедии")

        children_books = collector.get_books_for_children()
        # Проверяем, что возрастные жанры исключены
        assert "Книга ужасов" not in children_books
        assert "Книга детектива" not in children_books
        # Проверяем, что допустимые жанры есть
        assert "Книга фантастики" in children_books
        assert "Мультик" in children_books
        assert "Комедия" in children_books

    def test_add_book_in_favorites_adds_book_if_exists_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert "Гарри Поттер" in collector.favorites

    def test_add_book_in_favorites_does_not_add_book_if_not_in_books_genre(self):
        collector = BooksCollector()
        collector.add_book_in_favorites("Неизвестная книга")
        assert "Неизвестная книга" not in collector.favorites

    def test_add_book_in_favorites_does_not_add_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_removes_book_if_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert "Гарри Поттер" not in collector.favorites

    def test_delete_book_from_favorites_does_nothing_if_book_not_in_favorites(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("Неизвестная книга")
        assert len(collector.favorites) == 0

    def test_get_list_of_favorites_books_returns_correct_list(self):
        collector = BooksCollector()
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.add_new_book("Шерлок Холмс")
        collector.add_book_in_favorites("Шерлок Холмс")
        favorites = collector.get_list_of_favorites_books()
        assert "Гарри Поттер" in favorites
        assert "Шерлок Холмс" in favorites
        assert len(favorites) == 2

# Тесты для класса BooksCollector

## Реализованные тесты:

- `test_add_new_book_add_two_books` — проверка добавления двух книг
- `test_add_new_book_adds_book_with_valid_name` — добавление книги с валидным именем
- `test_add_new_book_does_not_add_book_with_empty_name` — книга с пустым именем не добавляется
- `test_add_new_book_does_not_add_book_with_long_name` — книга с именем более 40 символов не добавляется
- `test_add_new_book_adds_only_one_instance_of_book` — повторное добавление книги не создает дубликат
- `test_set_book_genre_sets_genre_for_existing_book` — установка жанра для существующей книги
- `test_set_book_genre_does_not_set_genre_for_nonexistent_book` — установка жанра для несуществующей книги
- `test_set_book_genre_does_not_set_invalid_genre` — установка недопустимого жанра не изменяет жанр
- `test_get_book_genre_returns_correct_genre` — получение жанра книги
- `test_get_books_with_specific_genre_returns_correct_list` — получение списка книг по жанру
- `test_get_books_with_specific_genre_returns_empty_list_if_no_books` — получение пустого списка, если книг нет
- `test_get_books_genre_returns_current_dictionary` — получение текущего словаря книг с жанрами
- `test_add_new_book_valid_names` (параметризованный) — проверка добавления книг с валидными именами (1 и 40 символов)
- `test_add_new_book_invalid_names` (параметризованный) — проверка, что книги с невалидными именами (пустое и 41 символ) не добавляются
- `test_get_books_for_children_excludes_age_rated_genres` — проверка, что возрастные жанры исключены из списка детских книг
- `test_add_book_in_favorites_adds_book_if_exists_in_books_genre` — добавление книги в избранное, если она существует в списке книг
- `test_add_book_in_favorites_does_not_add_book_if_not_in_books_genre` — книга не добавляется в избранное, если её нет в списке книг
- `test_add_book_in_favorites_does_not_add_duplicate` — книга не добавляется в избранное дважды
- `test_delete_book_from_favorites_removes_book_if_exists` — удаление книги из избранного
- `test_delete_book_from_favorites_does_nothing_if_book_not_in_favorites` — попытка удаления несуществующей книги из избранного
- `test_get_list_of_favorites_books_returns_correct_list` — получение списка избранных книг

Все тесты проходят, покрывают все основные сценарии использования класса `BooksCollector`.
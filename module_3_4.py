# Пункты задачи:
#
# 1. Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
def single_root_words(root_word, *other_words):

    # 2. Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []

    _root_word = root_word.lower()

    # 3. При помощи цикла for переберите предполагаемо подходящие слова.
    for word in other_words:
        _word = word.lower()

        # 4. Пропишите корректное относительно задачи условие,
        #     при котором добавляются слова в результирующий список same_words.
        if _word.__contains__(_root_word) or _root_word.__contains__(_word):
            same_words.append(word)

    # 5. После цикла верните образованный функцией список same_words.
    return same_words


# 6. Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

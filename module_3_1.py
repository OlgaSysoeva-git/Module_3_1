
# создаём переменную (calls) вне функции - глобальное пространство
calls = 0

# создаём функцию и изменять в ней значение переменной (calls) - локальное пространство
def count_calls() :  # функция будет вызываться в остальных двух функциях (!)
    global calls  # пропишем, что используем глобальные переменные
    calls += 1  # Увеличиваем счётчик при каждом вызове функции
# создаём функцию string_info с параметром string
def string_info(string):
    count_calls() # !
    return (len(string), string.upper(), string.lower())  # функция string_info принимает
                                                          # аргумент - строку и возвращает
                                                          # кортеж из:
                                                          # длины этой строки, строку
                                                          # в верхнем регистре,
                                                          # строку в нижнем регистре
# создаём функцию is_contains с двумя параметрами string и list_to_search
def is_contains(string, list_to_search):
    count_calls() # !
    return string.upper() in [s.upper() for s in list_to_search ]
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


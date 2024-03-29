import pytest

from homeworks import unique_names, top_three_names, min_max_course


@pytest.mark.parametrize("mentors, expected", [
    ([
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
], 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'),
    ([['Иван Иванов', 'Иван Петров'], ['Федор Питонов', 'Иван Фамилия']], 'Уникальные имена преподавателей: Иван, Федор'),
    ([[], []], 'Уникальные имена преподавателей: ')
])
def test_unique_names(mentors, expected):

    result = unique_names(mentors)
    assert expected == result

@pytest.mark.parametrize("mentors, expected", [
    ([
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
], 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'),
    ([['Иван Иванов', 'Кирилл Петров'], ['Федор Питонов', 'Иван Фамилия']], 'Иван: 2 раз(а), Кирилл: 1 раз(а), Федор: 1 раз(а)')
])
def test_top_three_names(mentors, expected):

    result = top_three_names(mentors)
    assert expected == result

# Возникает исключение, если количество уникальных имен меньше трех
@pytest.mark.parametrize("mentors, expected_exception", [
    ([
	["Евгений Шмаргунов", "Евгений Булыгин"],
	["Евгений Воронов", "Евгений Юшин"]
], IndexError),
    ([[], []], IndexError)
])
def test_empty_list_top_three_names(mentors, expected_exception):
    with pytest.raises(expected_exception) as exc_info:
        top_three_names(mentors)
    assert str(exc_info.value) == 'list index out of range'

@pytest.mark.parametrize("courses, durations, expected", [
    (
    ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"],
    [14, 20, 12, 20],
    'Самый короткий курс(ы): Fullstack-разработчик на Python - 12 месяца(ев)\nСамый длинный курс(ы): Java-разработчик с нуля, Frontend-разработчик с нуля - 20 месяца(ев)'
),
    (
    ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"],
    [20, 20, 20, 20],
    'Самый короткий курс(ы):  - 20 месяца(ев)\nСамый длинный курс(ы): Python-разработчик с нуля, Java-разработчик с нуля, Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)'
),
    (
    ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"],
    [14, 20, 12, 0],
    'Самый короткий курс(ы): Frontend-разработчик с нуля - 0 месяца(ев)\nСамый длинный курс(ы): Java-разработчик с нуля - 20 месяца(ев)'
)
])
def test_min_max_course(courses, durations, expected):

    result = min_max_course(courses, durations)
    assert expected == result

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

durations = [14, 20, 12, 20]

def unique_names(mentors):
    all_list = []
    for m in mentors:
        all_list += m

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)

    return f"Уникальные имена преподавателей: {', '.join(all_names_sorted)}"

def top_three_names(mentors):
    all_list = []
    for m in mentors:
        for names in m:
            name = names.split()
            all_list.append(name[0])


    unique_names = set(all_list)

    popular = []
    for name in unique_names:
        popular.append([name, all_list.count(name)]) 

    popular.sort(key=lambda x:x[1], reverse=True)

    top_3 = popular[0:3]
    return f'{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а), {top_3[2][0]}: {top_3[2][1]} раз(а)'

def min_max_course(courses, durations):
    courses_list = []

    for title, duration in zip(courses, durations):
        course_dict = {'title': title, 'duration': duration}
        courses_list.append(course_dict)

    min_d = min(durations)
    max_d = max(durations)

    maxes = []
    minis = []
    for idx, duration in enumerate(durations):
        if duration == max_d:
            maxes.append(idx)
        elif duration == min_d:
            minis.append(idx)

    courses_min = []
    courses_max = []
    for id in minis:
        courses_min.append(courses_list[id]['title'])
    for id in maxes:
        courses_max.append(courses_list[id]['title'])
        
    return(f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_d} месяца(ев)\n'
           f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_d} месяца(ев)')

if __name__ == '__main__':
    print(unique_names(mentors))
    print(top_three_names(mentors))
    print(min_max_course(courses, durations))
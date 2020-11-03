import csv

AGE = 7
IS_ENGLISH = 3  # string
ACHIVE = 11 # string
GENRES = 9 # string
TAGS = 10 # string
RATE = 12
CLIENT_TIME = 15
USERS_NUMBER = 16
PRISE = 17


def get_answers(QuestionList):
    answers = []
    RightFormat = False
    count = 2
    for i in QuestionList:
        if (count == AGE) or (RATE <= count <= PRISE):
            test_str = input(i)
            while not RightFormat:
                try:
                    test_float = float(test_str)
                    RightFormat = True
                except ValueError:
                    test_str = input('Неверный формат ввода. Введите значение коректно')
            answers.append(test_str)
            RightFormat = False
        else:
            answers.append(input(i))
        count += 1
    return answers


def check_variant(StringForCheck, CheckList):
    count = 2
    coin = 0
    for i in CheckList:
        entry = StringForCheck[count]
        if count == len(StringForCheck):
            break
        if count == AGE:
            if int(i) >= int(entry):
                coin += 0.5
        elif count == IS_ENGLISH or count == ACHIVE:
            if (i == 'Да' and int(entry) == 1) or (i == 'Нет' and int(entry) == 0):
                coin += 0.2
        elif GENRES <= count <= TAGS:
            tags_list = i.split(';')
            for j in tags_list:
                if j in entry:
                    coin += 1
        elif RATE <= count <= CLIENT_TIME:
            if float(entry) * 0.65 <= float(i) <= float(entry) * 1.35:
                coin += 0.2
        elif count == USERS_NUMBER:
            average_list = entry.split('-')
            if float(average_list[0]) * 0.8 <= float(i) >= float(average_list[1]) * 1.2:
                coin += 0.3
        elif count == PRISE:
            if float(entry) * 0.8 <= float(i) >= float(entry) * 1.2:
                coin += 0.8
        elif i in entry:
            coin += 0.5
        count += 1
    if coin >= 4.5:
        return True
    else:
        return False


with open('steam.csv', encoding='utf-8') as cvs_file:
    cvsReader = csv.reader(cvs_file)
    gameList = list(cvsReader)
    gameList.pop(0)
    prefList = []
    quesList = ['Укажите примерный год выпуска игры:',  # 2 0
                'English?(Да/Нет):',  # 3 1
                'Игры какого разработчика вам нравятся?',  # 4 2
                'Может, у вас есть любимая компания-издатель?',  # 5 3
                'Укажите ОС, на которой собираетесь играть (с маленькой буквы):',  # 6 4
                'Введите ваш возраст:',  # 7 5
                'Какую категорию игр предпочитаете? (Online Multi-player etc)',  # 8 6
                'Укажите предпочитаемый(е) жанр(ы) через точку с запятой:\n',  # 9 7
                'Попробуем пройтись по тегам Steam Spy. Напишите предпочитаемые теги, либо пропустите этот шаг:',  # 10 8
                'Хотите чтобы в игре были достижения? (Да/Нет)',  # 11 9
                'Сколько положительных отзывов должно быть у продукта?',  # 12 10
                'А отрицательных?\n',  # 13 11
                'Как много времени игроки проводят в этой игре? Напишите среднее количество часов:',  # 14 12
                'А сколько вы готовы потратить времени на эту игру в целом?',  # 15 13
                'Насколько популярна должна быть игра? Укажите примерное число пользователей:',  # 16 14
                'Сколько вы готовы заплатить за игру? (в долларах)']  # 17 15

    answersList = get_answers(quesList)

    # [TEST] answersList = ['2000', 'Да', 'Valve', 'Valve', 'windows', '18', 'Online Multi-Player', 'Action;Slasher',
    # '', 'Да', '5000', '500', '2000', '300', '90000', '5'] 

    for i in gameList:
        if check_variant(i, answersList):
            prefList.append(i[1])
    print('Вам могут понравиться такие игры:')
    for i in range(5):
        print(prefList[i])
    fin = input('\nЕсли хотите увидеть полный список, введите "full":\n')
    if fin == 'full':
        print(prefList)

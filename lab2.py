import csv


def GetAnswers(QuestionList):
    answers = []
    for i in QuestionList:
        print(i)
        answers.append(input())
    return answers


def CheckVariant(StringForCheck, CheckList):
    count = 2
    coin = 0
    for i in CheckList:
        if count == len(StringForCheck):
            break
        if count == 7:
            if int(i) >= int(StringForCheck[count]):
                coin += 0.5
        elif count == 3 or count == 11:
            if (i == 'Да' and int(StringForCheck[count]) == 1) or (i == 'Нет' and int(StringForCheck[count]) == 0):
                coin += 0.2
        elif 9 <= count <= 10:
            tags_list = i.split(';')
            for j in tags_list:
                if j in StringForCheck[count]:
                    coin += 1
        elif 12 <= count <= 15:
            if float(StringForCheck[count])*0.65 <= float(i) <= float(StringForCheck[count])*1.35:
                coin += 0.2
        elif count == 16:
            average_list = StringForCheck[count].split('-')
            if float(average_list[0])*0.8 <= float(i) >= float(average_list[1])*1.2:
                coin += 0.3
        elif count == 17:
            if float(StringForCheck[count]) * 0.8 <= float(i) >= float(StringForCheck[count]) * 1.2:
                coin += 0.8
        elif i in StringForCheck[count]:
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
    quesList = ['Укажите примерный год выпуска игры:',  # 2
                'English?(Да/Нет):',  # 3
                'Игры какого разработчика вам нравятся?',  # 4
                'Может, у вас есть любимая компания-издатель?',  # 5
                'Укажите ОС, на которой собираетесь играть (с маленькой буквы):',  # 6
                'Введите ваш возраст.',  # 7
                'Какую категорию игр предпочитаете? (Online Multi-player etc)',  # 8
                'Укажите предпочитаемый(е) жанр(ы) через точку с запятой:\n',  # 9
                'Попробуем пройтись по тегам Steam Spy. Напишите предпочитаемые теги, либо пропустите этот шаг:',  # 10
                'Хотите чтобы в игре были достижения? (Да/Нет)',  # 11
                'Сколько положительных отзывов должно быть у продукта?',  # 12
                'А отрицательных?\n',  # 13
                'Как много времени игроки проводят в этой игре? Напишите среднее количество часов:',  # 14
                'А сколько вы готовы потратить времени на эту игру в целом?',  # 15
                'Насколько популярна должна быть игра? Укажите примерное число пользователей:',  # 16
                'Сколько вы готовы заплатить за игру? (в долларах)']  # 17

    answersList = GetAnswers(quesList)

    # [TEST] answersList = ['2000', 'Да', 'Valve', 'Valve', 'windows', '18', 'Online Multi-Player', 'Action;Slasher',
    # '', 'Да', '5000', '500', '2000', '300', '90000', '5'] 

    for i in gameList:
        if CheckVariant(i, answersList):
            prefList.append(i[1])
    print('Вам могут понравиться такие игры:')
    for i in range(5):
        print(prefList[i])
    fin = input('\nЕсли хотите увидеть полный список, введите "full":\n')
    if fin == 'full':
        print(prefList)
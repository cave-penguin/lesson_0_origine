# print("Hello, " + "World!")
# print("My name is %s and Im %s years old" % ("Micky", 42))
# print("My name is %(name)s and Im %(years)s years old" % {"name": "Micky", "years": 42})
# print("Im learn in {0}-{1} {0}".format("Urban", "University"))
# print(
#     "Im learn in {title}-{postfix} {title}".format(title="Urban", postfix="University")
# )
# print(f"{'Urban ' * 2} is the best university!")


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
# tasks_total = 82
# time_avg = 45.2
# challenge_result = "Победа команды Волшебники данных!"
#   %
print("В команде Мастера кода участников: %s ! " % 5)
print(
    "Итого сегодня в командах участников: %(first_team)s и %(second_team)s !"
    % {"first_team": team1_num, "second_team": team2_num}
)
#   format
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {time1} с !".format(time1=team1_time))
#   f-string
print(f"Команды решили {score_1} и {score_2} задач.")
result = ""
if score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
elif score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
else:
    result = "Ничья!"

print(f"Результат битвы: {result}")

print(
    f"Сегодня было решено {score_1 + score_2} задач, "
    f"в среднем по {round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу!."
)

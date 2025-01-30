import random
secret_number = random.randint(1, 100)
attempts = 0
print("Гра 'Вгадай число' Я загадаю число від 1 до 100. Відгадай")
while True:
    guess = int(input("Введіть число: "))
    attempts += 1
    if guess < secret_number:
        print("Число більше!")
    elif guess > secret_number:
        print("Загадане число менше!")
    else:
        print(f"Вітаю! Ви вгадали число {secret_number} за {attempts} спроб!")
        break

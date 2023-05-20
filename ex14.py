from sys import argv

script, user_name = argv
prompt = "> "

print(f"Hi {user_name}, The script name is {script}")

print("How old are you?")
age = input(prompt)

print("Where are you from?")
place = input(prompt)

print("What is your favorite subject?")
answer = input(prompt)

print(f"So {user_name}, You are {age} years old and are from {place} and you like {answer}")

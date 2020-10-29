from random import randint
import sys
import logbook

level = logbook.TRACE
log_filename = "random_number_log.txt"

if not log_filename:
    logbook.StreamHandler(sys.stdout, level=level).push_application()
else:
    logbook.TimedRotatingFileHandler(log_filename, level=level).push_application()

app_log = logbook.Logger('App')
begin_number = sys.argv[1]
end_number = sys.argv[2]

app_log.trace("Received input")

random_number = randint(int(begin_number), int(end_number))
print(random_number)


while True:
    try:
        guess_number = int(input(f"Guess a number between {begin_number} and {end_number}? "))
        if int(begin_number) <= int(guess_number) <= int(end_number):
            if guess_number == random_number:
                print('You are a genious')
                break
        else:
            print(f'Please guess a number between {begin_number} and {end_number}!')
    except ValueError:
        print('Please enter a number')
        continue

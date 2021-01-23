from datetime import date, timedelta
import random


def gen_random_name():
    sequence = ('John', 'George', 'David', 'Andrew', 'Bill', 'Donald')
    return random.choice(sequence)


def gen_random_job():
    sequence = ('artist', 'astronaut', 'doctor', 'police', 'teacher', 'firefighter')
    return random.choice(sequence)


def gen_random_int(range_from, range_to):
    return random.randint(range_from, range_to)


def gen_sentence(word_sequence, range_to):
    words_list = [random.choice(word_sequence) for i in range(range_to)] + ['.']
    return ' '.join(words_list)


def gen_random_text(range_from, range_to):
    text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
    dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
    pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    word_sequence = text.split(' ')
    sentence = ''
    for i in range(range_from, range_to):
        sentence += gen_sentence(word_sequence, 8)
    return sentence


def gen_random_date():
    return date.today() + timedelta(days=random.randrange(100))
import re


def my_function(text, multiplier=2):
    return re.sub(re.compile("\d+"), lambda match_obj: str(int(match_obj.group(0)) * multiplier), text)


text = "Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных"
print(my_function(text))
print(my_function(text, 25))

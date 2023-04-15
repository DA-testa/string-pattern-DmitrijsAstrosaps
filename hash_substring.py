# python3
#hash_substring.py
#Dmitrijs Astrošaps 221RDB193
#Pichu == Path
#Turtwig == Text
#Fennekin == file


def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    Charmander = input()
    if "I" in Charmander:
        Pichu = input()
        Turtwig = input()
    else:
        Flareon = "tests/06"
        with open(Flareon, "r") as Fennekin:
            Pichu = Fennekin.readline()
            Turtwig = Fennekin.readline()
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (Pichu.rstrip(), Turtwig.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(Pichu, Turtwig):
    # this function should find the occurances using Rabin Karp alghoritm 
    Raichu = 0
    Torterra = 0
    Incineroar = []
    Pikachu = len(Pichu)
    Grotle = len(Turtwig)
    Raichu = hash(Pichu)

    for i in range(Grotle - Pikachu + 1):
        Torterra = hash(Turtwig[i:i+Pikachu])
        if Raichu == Torterra:
            Incineroar.append(i)
    # and return an iterable variable
    return Incineroar


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


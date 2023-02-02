from utils.ranks import *

def rate_int(ints):
    return f'{str(ranks_int(ints)).partition(".")[0] + "." + ranks_int(ints)[ranks_int(ints).find(".")+1] + "k"*ranks_int(ints).count(".")}$'
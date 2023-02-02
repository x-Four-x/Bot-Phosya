from sql_func import *

def check_profile(id):
    name = check_name(id)
    money = check_balance(id, False)
    foken = check_foken(id)
    date_reg = check_date_reg(id)
    return {
        "name": name,
        "money": money,
        "foken": foken,
        "date_reg": date_reg
    }
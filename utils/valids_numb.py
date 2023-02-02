import phonenumbers


def valid_num(phone_num):
    try:
        num = phonenumbers.parse(phone_num)
        return phonenumbers.is_valid_number(num) == True
    except:
        return False


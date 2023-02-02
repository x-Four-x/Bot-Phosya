import sqlite3 as sql
from utils.rates_user import ranks_int
from datetime import datetime
from loader import bot
from random import choice
from data.config import *
from utils.link_user import link_user

conn = sql.connect("database.db", timeout=1)
cursor = conn.cursor()



def user_exists(id):
    info = cursor.execute('SELECT * FROM user_info WHERE id_user=?', (id,))
    return info.fetchone()

# add - Функции которые добавлюяют что либо

def add_user(id, link):
    now = datetime.now()
    cursor.execute("INSERT OR IGNORE INTO user_info (id_user,name_user,balance_user,reg_date,last_game,balance_foken,url_user) VALUES (?,?,?,?,?,?,?)",
    (id, "Игрок", 2500000, now.strftime('%d-%m-%Y, %H:%M'), None, 0, link))
    return conn.commit()



async def add_ref(invite_id, id):
    cursor.execute('UPDATE user_info SET ref_level=? WHERE id_user=?', (check_ref_lev(invite_id)+1, invite_id))
    prize = random.choice(list(referall.keys()))
    prize_sum = random.randint(referall.get(prize)[1], referall.get(prize)[2])
    cursor.execute(f'UPDATE user_info SET {prize} = ? WHERE id_user=?', (prize_sum, invite_id))
    await bot.send_message(chat_id=invite_id, text=f"{link_user(invite_id)}, по твоей ссылке перешел человек {choice(joi)}\n"
    f"{choice(info)} Твой новый уровень рефералки - {check_ref_lev(invite_id)} {choice(like)}\n"
    f"🎁 Награда - {referall.get(prize)[0]} {ranks_int(prize_sum)}шт.")
    return conn.commit()

def add_money(sum_money, id):
    balance = check_balance(id, False)
    sums = int(balance + sum_money)
    cursor.execute(f'UPDATE user_info SET balance_user = ? WHERE id_user=?', (sums, id))
    return conn.commit()

def add_game(id, game):
    cursor.execute(f'UPDATE user_info SET last_game = ? WHERE id_user=?', (game, id))
    return conn.commit()

# check - Функции которые проверяют что-либо

def check_link(id):
    link = cursor.execute('SELECT url_user FROM user_info WHERE id_user=?', (id,)).fetchone()[0]
    return link

def check_valid_id(id_user):
    id_user = cursor.execute('SELECT * FROM user_info WHERE id_user=?', (id_user,)).fetchone()
    return True if id_user is not None else False

def check_game(id):
    game = cursor.execute('SELECT last_game FROM user_info WHERE id_user=?', (id,))
    return game.fetchone()[0]

def check_ref_lev(id):
    lev = cursor.execute('SELECT ref_level FROM user_info WHERE id_user=?', (id,)).fetchone()[0]
    return int(lev) if lev is not None else 0

def check_foken(id):
    foken = cursor.execute('SELECT balance_foken FROM user_info WHERE id_user=?', (id,)).fetchone()[0]
    return int(foken) if foken is not None else 0

def check_date_reg(id):
    date = cursor.execute('SELECT reg_date FROM user_info WHERE id_user=?', (id,))
    return date.fetchone()[0]

def check_all_users():
    all_users = cursor.execute('SELECT id_user FROM user_info')
    return [x[0] for x in all_users.fetchall()]

def check_balance(id, text):
    money = cursor.execute('SELECT balance_user FROM user_info WHERE id_user=?', (id,))
    if text == True:
        return f"💰 Ваш баланс: {ranks_int(int(money.fetchone()[0]))}$"
    else:
        return int(money.fetchone()[0])

def check_name(id):
    nickname = cursor.execute('SELECT name_user FROM user_info WHERE id_user=?', (id,))
    return nickname.fetchone()[0]

def check_top_balance():
    top = cursor.execute('SELECT balance_user, id_user FROM user_info ORDER BY balance_user DESC LIMIT 10').fetchall()
    return top

def check_money(sum_money, id):
    balance = check_balance(id, False)
    if balance >= sum_money:
        return True
    else:
        return False

def edit_nick(nick, id):
    cursor.execute(f'UPDATE user_info SET name_user = ? WHERE id_user=?', (nick, id))
    return conn.commit()

# withdraw - Функции которые выводят что-либо

def withdraw_money(sum_money, id):
    balance = check_balance(id, False)
    cursor.execute(f'UPDATE user_info SET balance_user = {balance - sum_money} WHERE id_user=?', (id,))
    return conn.commit()
    

def delete_my():
    cursor.execute(f'DELETE FROM progress_info WHERE id_user={admin_id}')
    cursor.execute(f'DELETE FROM user_info WHERE id_user={admin_id}')
    return conn.commit()
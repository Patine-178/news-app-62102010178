from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users} # {"user1":User(1, 'user1', 'abcxyz'), "user2":User(2, 'user2', 'abcxyz')}
userid_table = {u.id: u for u in users} # {1:User(1, 'user1', 'abcxyz'), 2:User(2, 'user2', 'abcxyz')}

# เข้าไป check ว่าตรงกันรึป่าว ( check ใน users )
def authenticate(username, password):
    user = username_table.get(username, None) # เหมือนกับ username_table[username] ถ้าหา key username ไม่เจอจะคือค่า None
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
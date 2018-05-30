from mysql import connector


def get_info(num, start_index):
    conn = connector.connect(user = 'root', password='123456', database='auto_login')
    cursor = conn.cursor(dictionary=True)
    sql = 'select u.id,username,passw,email,rev_email,web_id,url,other_info,remain_days,last_points from ' \
          'users u left join websites w on u.web_id = w.id limit %s,%s;'
    cursor.execute(sql, [start_index, num])
    info = cursor.fetchall()
    conn.close()
    return info

def get_total_num():
    conn = connector.connect(user = 'root', password='123456', database='auto_login')
    cursor = conn.cursor()
    sql = 'select count(id) from users;'
    cursor.execute(sql)
    num = cursor.fetchone()
    conn.close()
    return num

def update_remain(id, days):
    conn = connector.connect(user = 'root', password='123456', database='auto_login')
    cursor = conn.cursor(dictionary=True)
    sql = 'update users set remain_days = %s where id = %s;'
    cursor.execute(sql, [days, id])
    conn.commit()
    conn.close()

if __name__ == '__main__':
    val = get_info(10, 0)
    print(val,type(val), type(val[0]))
    num = get_total_num()
    print('total num = ',num)
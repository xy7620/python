from auto_login.login import login
from auto_login.db_info import get_info,get_total_num,update_remain
from auto_login.smtp import send
from auto_login.log import logger
import time

def all_login():
    user_num = get_total_num()[0]

    logging = logger
    print('******************************************')
    s = '需登录账户数：'+str(user_num)
    logging.info(s)
    print(s)
    i = 0
    while (i < user_num):
        info = get_info(10, i)
        succ_num = 0
        fail_num = 0
        no_remain_num = 0
        i += 10
        for user in info:
            if user['remain_days'] == None or  user['remain_days']<= 0:
                no_remain_num+=1
                continue
            print('*****************************************************')
            r = login(user['url'], user['username'], user['passw'])
            if r != -1:
                succ_num += 1
                s = '用户 '+user['username']+' 登录成功！'+ str(r)+'; 剩余自动登录天数：'+str(user['remain_days']-1)+'\n'+time.asctime()
                logging.info(s+'\n')
                print(s)
                update_remain(user['id'], user['remain_days']-1)
                if user['rev_email'] == 1:
                     send(s, user['email'])
                    # pass
            else:
                s = '用户 '+ user['username']+ ' 登录出错！'
                logging.error(s+'\n')
                print(s)
                fail_num += 1

    print('*****************************************************')
    result_str = '成功登录账户数：'+str(succ_num)+' 失败登录账户数：'+str(fail_num)+' 余额不足账户数：'+str(no_remain_num)+'\n'+time.asctime()
    logging.info(result_str+'\n')
    print(result_str)
    # send(result_str)


def wait_time():
    start_time = '00:01'
    while(True):
        hour_and_min = time.strftime('%H:%M')
        if hour_and_min == start_time:
            print('**************开始执行登录**************',time.asctime())
            all_login()
            time.sleep(85000)
        time.sleep(50)

if __name__ == '__main__':
    all_login()
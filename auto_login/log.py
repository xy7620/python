import logging

def logger_console_file():
    # 创建一个logger
    logger = logging.getLogger('mylog')
    logger.setLevel(logging.INFO)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler('F:\\auto_login.log')
    fh.setLevel(logging.INFO)

    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s :\n %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    # logger.addHandler(ch)

    return logger

logger = logger_console_file()

if __name__ == '__main__':
    logger = logger_console_file()
    logger.info('hello')
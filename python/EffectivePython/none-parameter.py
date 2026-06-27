# 24 使用None为默认参数，以防止问题发生
# logging函数！
from time import sleep
from datetime import datetime


# 一个有问题的函数
def log1(message, when=datetime.now()):
    # when = datetime.now()
    print(f'{when}: {message}')
    # 会导致每次的时间一样


# 通过默认值为None修复问题
def log2(message, when=None):
    """
    log a message with a timestamp.
    Args:
        message: Message to print.
        when :datetime of when the message occured.
            Defaults to the present time.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')


log1('hi, there.')
sleep(0.1)
log1('hi, again.')

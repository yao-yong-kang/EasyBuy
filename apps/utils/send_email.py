from random import Random

from EasyBuy.settings import EMAIL_FROM #导入模型
from user.models import UserProfile #导入模型
from django.core.mail import send_mail #导入发送邮件

def random_str(random_length=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str



def send_register_email(email):
    email_record = UserProfile()
    code = random_str(16)

    email_record.code = code
    email_record.email = email
    email_record.code = code





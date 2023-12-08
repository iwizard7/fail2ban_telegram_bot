import telebot
import subprocess

# Установите токен вашего бота
TOKEN = '####'

# Создайте экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Функция для проверки статуса блокировки IP
def check_ip_status(ip):
    result = subprocess.run(['fail2ban-client', 'status', 'sshd'], capture_output=True)
    output = result.stdout.decode('utf-8')
    if ip in output:
        return True
    else:
        return False

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Привет! Я бот для уведомлений о блокировке IP.')

# Обработчик команды /check_ip
@bot.message_handler(commands=['check_ip'])
def check_ip(message):
    ip = message.text.split()[1]
    if check_ip_status(ip):
        bot.reply_to(message, f'IP {ip} заблокирован.')
    else:
        bot.reply_to(message, f'IP {ip} не заблокирован.')

# Запуск бота
bot.polling()
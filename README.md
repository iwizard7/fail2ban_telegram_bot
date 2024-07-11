[![CodeQL](https://github.com/iwizard7/fail2ban_telegram_bot/actions/workflows/codeql.yml/badge.svg)](https://github.com/iwizard7/fail2ban_telegram_bot/actions/workflows/codeql.yml)
# Fail2Ban IP Notification Bot

Этот бот для Telegram написан на Python и предназначен для отправки уведомлений о блокировке IP-адресов в программе Fail2Ban.

## Установка

1. Установите необходимые зависимости:

```shell
pip install telebot
```

2. Получите токен вашего бота Telegram:

- Создайте нового бота с помощью @BotFather в Telegram.
- Скопируйте полученный токен.

3. Замените `YOUR_TELEGRAM_BOT_TOKEN` в файле `bot.py` на ваш токен бота Telegram.

4. Запустите скрипт:

```shell
python bot.py
```

## Использование

- Запустите бота, используя команду `python bot.py`.
- Добавьте вашего бота в группу или напишите ему в личные сообщения.
- Используйте команду `/check_ip <IP адрес>`, чтобы проверить статус блокировки IP.

## Примеры команд

- `/start` - Начало работы с ботом.
- `/check_ip 192.168.0.1` - Проверить статус блокировки IP адреса `192.168.0.1`.

## Лицензия

Этот проект распространяется под лицензией [MIT](LICENSE).
```

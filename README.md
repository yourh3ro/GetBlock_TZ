# ТЗ DevOps
## Теоретическая часть 

> Приложение запущено в докер-контейнере через docker-compose. Контейнер рестартится, логов нет, так как не успевает писать. Что будешь делать?

> Деплой сервиса провалился с сообщением типа “при запуске контейнера возникла ошибка” без деталей

`docker logs` по контейнеру и разбираться.

> Билд завершился сообщением “Репозиторий не найден“. Что будешь делать?

Проверю связь\просадки сети\доступность со своей машины, проверю с билд сервера, проверю сертификаты, битые ссылки.  

> Есть система неважно какой структуры. Требуется настроить мониторинг с нуля. Какие уровни ты охватишь?

Железо (если bare metal) или VMs
ОС и ее показатели
Приложение
Бизнес-метрики

## Практическая часть

> 1.Напишите Dockerfile для сборки данного проекта
> https://github.com/dogecoin/dogecoin

Каталог dogecoin-container 
```sh
make build && make run
```

> 2.Напишите Ansible роль увеличивающую лимит на количество открытых файлов в Linux

Каталог open-file-limit-up, playbook для запуска в корне проекта (`start-role.yml`)
```sh
vim ./start-role.yml
# change hosts
ansible-playbook start-role.yml
```

> 3.Напишите Python скрипт, который сравнивает время ответа от этих API и значения следующих ключей
> ключ result
> https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken
> ключ height
> https://api.blockcypher.com/v1/eth/main

Каталог pyAPItask
```sh
pipenv shell
pipenv install
python ,/main.py
```

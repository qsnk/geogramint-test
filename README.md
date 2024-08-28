# Тестовое задание по проекту [Geogramint](https://github.com/Alb-310/Geogramint)
## **Сборка приложения**
### *1. Клонировать репозиторий*
```
git clone https://github.com/qsnk/geogramint-test.git
```
### *2. Перейти в директорию*
```
cd geogramint-test
```
### *3. Собрать образ и запустить контейнер*
```
docker-compose up -d
```
### *Остановить контейнер*
```
docker-compose down
```
## **Работа с приложением**
### *Создать API ключи доступа*
- Перейдите по [этой](https://my.telegram.org/auth) ссылке
- Войдите по номеру телефона 
- Перейдите в раздел **API development tools**
- Создайте новое приложение (API app)
- Укажите данные для приложения
- Сохраните app_id, app_hash
### *Показать помощь*
```
docker-compose run --rm geogramint --help
```
### *Показать версию приложения*
```
docker-compose run --rm geogramint --version
```
### *Установить конфигурацию* 
```
docker-compose run --rm geogramint set-config api_id api_hash phone_number
```
**Пример:**
```
docker-compose run --rm geogramint set-config 21772285 c828461e53378cec630e3e91f22def73 +79876543210
```
### *Установить идентификатор API* 
```
docker-compose run --rm geogramint set-id api_id
```
**Пример:**
```
docker-compose run --rm geogramint set-id 21772285
```
### *Установить хэш API* 
```
docker-compose run --rm geogramint set-hash api_hash
```
**Пример:**
```
docker-compose run --rm geogramint set-hash c828461e53378cec630e3e91f22def73
```
### *Установить номер телефона* 
```
docker-compose run --rm geogramint set-phone phone_number
```
**Пример:**
```
docker-compose run --rm geogramint set-phone +79876543210
```
### *Начать сканирование*
```
docker-compose run --rm geogramint start-scan lat lon
```
**Пример:**
```
docker-compose run --rm geogramint start-scan 55.751244 37.618423
```
### *Очистить кэш телеграмма*
```
docker-compose run --rm geogramint reset-scan
```
## База данных
### Посмотреть базу данных
```
http://localhost:8081/
```
### Двнные для входа
- Имя пользователя: admin
- Пароль: pass
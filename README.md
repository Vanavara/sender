README.md для GitLab репозитория
<h2>Сервис Уведомлений</h2>
Данный проект представляет собой сервис управления рассылками с API для администрирования и получения статистики.

<h3>Основные функции:</h3>
Создание новой рассылки.
Просмотр созданных рассылок.
Получение статистики по выполненным рассылкам.
Отправка уведомлений на внешнее API.
Установка и Запуск:
Docker Compose:
Для удобства запуска всех сервисов проекта используйте Docker Compose.

<h3>bash</h3>
Copy code
docker-compose up -d
Эта команда запустит все необходимые контейнеры и сервисы.

<h3>Swagger UI:</h3>
Для просмотра документации API перейдите по адресу: http://127.0.0.1:8001/docs. Здесь представлено описание разработанного API
с возможностью тестирования всех доступных методов.

<h3>Дополнительные задания:</h3>
 Подготовлен docker-compose для запуска всех сервисов проекта одной командой.
 По адресу /docs/ открывается страница со Swagger UI и отображается описание разработанного API.
 Реализован дополнительный сервис, который раз в сутки отправляет статистику по обработанным рассылкам на email.
Обратная связь:
Если у вас возникли вопросы или предложения по улучшению проекта, не стесняйтесь обращаться.

Это базовый README.md для вашего проекта на GitLab. Вы можете дополнительно включить информацию о зависимостях проекта, 
инструкции по тестированию, информацию о лицензии и так далее.
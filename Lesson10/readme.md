Команда	Описание
scoop install allure  "Установка Allure через Scoop"
pip install pytest allure-pytest   "Установка зависимости allure-pytest"
mkdir allure-results  "Создание папки с результатами"
mkdir allure-report "Создание папки с отчетом"
pytest --alluredir=allure-results	"Запуск тестов с сбором данных для Allure"
allure serve allure-results	"Просмотр отчета во временном сервере"
allure generate allure-results --output allure-report --clean	"Генерация статического отчета"
allure open allure-report	"Открытие сгенерированного отчета"
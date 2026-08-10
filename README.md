# autotests_project

Учебный проект автоматизированного тестирования 

## Содержимое
- `api_tests` — тесты API (requests + pytest) 
- `selenium_tests` — UI-тесты (Selenium) 
  - `fixtures` — фикстуры pytest (запуск Chrome)
  - `locators` — локаторы элементов

## Требования
- Python 3.10+
- Google Chrome (для UI-тестов)

## Установка и запуск
1. Клонируем репозиторий:
   `git clone https://github.com/mooncna/autotests_project.git`
   `cd autotests_project`
2. Создадим и активируем виртуальное окружение:
   `python -m venv venv`
   `venv\Scripts\activate` (Windows)
3. Установим зависимости:
   `pip install -r requirements.txt`
4. Запуск тестов:
   - `python -m pytest` — все тесты
   - `python -m pytest api_tests` — только API
   - `python -m pytest selenium_tests` — только UI
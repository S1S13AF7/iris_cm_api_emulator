# Эмулятор сигналов Iris CM Callback API

![PyPI](https://img.shields.io/pypi/v/iris-cm-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/iris-cm-api)
![GitHub](https://img.shields.io/github/license/lordralinc/iris_cm_api_emulator)

# Установка 

## Windows
```shell
# Создаем папку, открываем в этой папке командную строку (shift + ПКМ)
py -m venv env
env\Scripts\activate.bat
pip install https://github.com/timoniq/vkbottle/archive/master.zip
pip install https://github.com/S1S13AF7/iris_cm_api_emulator/archive/master.zip
```

# Настройка
Создайте файл `config.ini` (скопируйте его из файла [config.ini.example](https://github.com/lordralinc/iris_cm_api_emulator/blob/master/config.ini.example)), укажите токен группы в поле `token`

# Запуск
```shell
# Открываем в созданной папке командную строку (shift + ПКМ)
env\Scripts\activate.bat
py -m iris_cm_api
```

# Обновление 
```shell
# Открываем в созданной папке командную строку (shift + ПКМ)
env\Scripts\activate.bat
pip install https://github.com/timoniq/vkbottle/archive/master.zip --upgrade
pip install https://github.com/S1S13AF7/iris_cm_api_emulator/archive/master.zip --upgrade
```


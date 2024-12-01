import locale

def configure_locale():
    try:
        locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
    except locale.Error:
        print("Русская локаль не доступна, используем стандартную.")
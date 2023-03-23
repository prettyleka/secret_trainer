def form_html_text(*args):
    exp = '<div class="st"><ul>'
    for req in args:
        exp += "<li><p>" + req + "</p></li>"
    return exp + '</ul></div>'

RU_NAME = form_html_text("Все буквы русского алфавита, римские цифры, дефис и апостроф", "1-50 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле NAME")
EN_NAME = form_html_text("Все буквы латинского алфавита", "1-50 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле NAME")
SURNAME_NEED = form_html_text("Все буквы русского алфавита", "1-50 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле SURNAME")
SURNAME_NO_NEED = form_html_text("Все буквы русского алфавита", "1-50 символов", "Не обязательное", "Текст ошибки:Неправильно заполнено поле SURNAME")
BIRTHDATE_NEED = form_html_text("Дата в формате DD.MM.YYYY", "Не больше текущей", "Обязательное", "Текст ошибки:Неправильно заполнено поле BIRTHDATE")
BIRTHDATE_NO_NEED = form_html_text("Дата в формате DD.MM.YYYY", "Не больше текущей", "Не обязательное", "Текст ошибки:Неправильно заполнено поле BIRTHDATE")
ID_CARD = form_html_text("Только цифры", "9 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле ID_CARD")
ID_CARD_BAD_DOC = form_html_text("Только цифры", "3 символа", "Обязательное", "Текст ошибки:Неправильно заполнено поле ID_CARD")
PA_NO_SPA = form_html_text("Только цифры", "10 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле PASSPORT")
PA_WH_SPA = form_html_text("Номер паспорта типа 00 00 000000", "Обязательное", "Текст ошибки:Неправильно заполнено поле PASSPORT")
PA_WH_SPA_NO_NEED = form_html_text("Номер паспорта типа 00 00 000000", "Не обязательное", "Текст ошибки:Неправильно заполнено поле PASSPORT")
PASSPORT_ISSUE = form_html_text("Дата в формате DD.MM.YYYY", "Не больше текущей", "Обязательное", "Текст ошибки:Неправильно заполнено поле PASSPORT_ISSUE")
POST_NO = form_html_text("Индекс в формате 000-000", "9 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле POST_NO")
STREET = form_html_text("Все буквы русского алфавита, цифры, пробел, римские цифры, дефис и апостроф", "1-50 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле STREET")
HOUSE = form_html_text("Только цифры", "1-5 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле HOUSE")
FLAT = form_html_text("Только цифры", "1-5 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле FLAT")
CAR_NO = form_html_text("Возможные варианты:", form_html_text("X000XX00", "X000XX000", "XX000X00", "0000XX00", "XX000000"), "Где Х - любая буква из УКЕНХВАРОСМТ", "Где 0 - любая цифра", "Обязательное", "Текст ошибки:Неправильно заполнено поле CAR_NO")
BANK_ACCOUNT = form_html_text("Только цифры", "10 символов", "Обязательное", "Текст ошибки:Неправильно заполнено поле BANK_ACCOUNT")
BALANCE = form_html_text("Баланс типа 12.00", "Не больше 1'000'000'000.00", "Обязательное", "Текст ошибки:Неправильно заполнено поле BALANCE")

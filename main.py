'''
.       1 любой символ, кроме новой строки \n
\d      1 любая цифра == [0-9]
\D      1 любой символ, кроме цифры == [^0-9]
\w      1 любая цифра, буква или '_'
\W      1 любой символ кроме латиницы, цифр или '_'
\s      1 символ пробела
\S      1 любой символ,кроме пробела
\b      граница слова (начало или конец)
[]      1 любой символ из символов в скобках
[^]     1 любой символ кроме тех, что в скобках

?       0 или 1 вхождение шаблона слева
*       0 и более вхождений шаблона слева
+       1 и более вхождений шаблона слева
{m}     m повторений шаблона слева
{n,m}   от n до m повторений шаблона слева (максимум символов)
{n,m}?  от n до m повторений шаблона слева (минимум символов)

^       начало строки
$       окончание строки

()      группирует символы внутри и возвращает только их

|       логическое ИЛИ (либо выражение до, либо выражение после символа)
\       экранирование, для использования метасимволов в качестве обычных (\. "." или \+ "+")
'''
import re

# re.match('AR', 'aARaAR') ищет вхождение в начале строки
# re.search('AR', 'aARaAR') ищет первое совпадение в любом месте строки
# re.findall('AR', 'aARaAR') ищет все совпадения в строке
# re.split()
# re.sub()
# re.compile()
if __name__ == '__main__':
    s = 'aARaARa-3a2 3a     4.5aaaaaaaaaaaa_2 user@mail.ru root@example.com 2021-01-02 2021-01-03 Андрей Семен Василий Олег апельсин'

    # re.match() -> re.Match object
    # ищет вхождение в начале строки
    result = re.match('aAR', s)
    print(result)
    if result is not None:
        print('совпадение: ', result.group())
        print('начало: ', result.start())
        print('конец: ', result.end())

    # re.search() -> re.Match object
    # ищет первое совпадение в строке
    result = re.search('AR', s)
    print(result)
    if result is not None:
        print('совпадение: ', result.group())
        print('начало: ', result.start())
        print('конец: ', result.end())

    # re.findall() -> List[str]
    # ищет все совпадения в строке
    result = re.findall('AR', s)
    print(result)

    # примеры регулярных выражений
    # вернуть первое слово из строки
    print(re.findall(r'^\w+', s))
    # вернуть первые два символа каждого слова
    print(re.findall(r'\b\w\w?', s))
    # вернуть домена из списка email адресов
    print(re.findall(r'@\w+.\w+', s))
    # вернуть домена верхнего уровня из списка email адресов
    print(re.findall(r'@\w+.(\w+)', s))
    # вернуть имена пользователей из списка email адресов
    print(re.findall(r'(\w+)@\w+.\w+', s))
    # вернуть год из найденных дат
    print(re.findall(r'(\d{4})-\d{2}-\d{2}', s))
    # извлечь слова, начинающиеся на гласную
    print(re.findall(r'\b[уеыаоэяиюУЕЫАОЭЯИЮ]\w*', s))
    # извлечь email в виде кортежей (имя_пользователя, домен)
    print(re.findall(r'(\w+)@(\w+.\w+)', s))
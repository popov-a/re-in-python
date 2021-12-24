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

Флаги:

re.ASCII        По умолчанию \w, \W, \b, \B, \d, \D, \s, \S соответствуют все юникодные символы с соответствующим качеством.
                Например, \d соответствуют не только арабские цифры, но и вот такие:
                re.ASCII ускоряет работу, если все соответствия лежат внутри ASCII.

re.IGNORECASE   Не различать заглавные и маленькие буквы. Работает медленнее, но иногда удобно
re.MULTILINE    Специальные символы ^ и $ соответствуют началу и концу каждой строки
re.DOTALL       По умолчанию символ \n конца строки не подходит под точку. С этим флагом точка — вообще любой символ


re.match(шаблон, строка)          ищет вхождение шаблона в начале строки
re.search(шаблон, строка)         ищет первое совпадение с шаблоном в любом месте строки
re.findall(шаблон, строка)        ищет все совпадения с шаблоном в строке

re.finditer(шаблон, строка)       ищет все совпадения с шаблоном в строке и возвращает итерируемый объект,
                                  у которого доступно начало и конец вхождения: m.group(), m.start(), m.end()

re_compiled = re.compile(шаблон)  компилирует шаблон, в дальнейшем можно использовать re_compiled.findall(строка)

re.split(шаблон, строка, maxsplit=0)          разбивает строку используя в качестве разеделителя шаблон
                                              пример:     re.split(r'[ ,\[\]]+', my_string)
                                              разбиваем строку my_string по пробелам, запятым и кватратным скобкам

re.sub(шаблон, замена, строка, count=0, flags=0)      замена в строке найденных шаблонов на "замена"
                                                       пример:     re.sub(r'\b\w+', 'word', 'My name is Ivan', count=3)
                                                       заменить первые три слова на "word"

Пример поиска и использования отдельных шаблонов в строке:

mac_table = '100    aabb.cc10.7000    DYNAMIC     Gi0/1'
            '200    aabb.cc20.7000    DYNAMIC     Gi0/2'

print(re.sub(r' *(\d+) +'
             r'([a-f0-9]+)\.'
             r'([a-f0-9]+)\.'
             r'([a-f0-9]+) +\w+ +'
             r'(\S+)',
             r'\1 \2:\3:\4 \5',
             mac_table))

100 aabb:cc10:7000 Gi0/1
200 aabb:cc20:7000 Gi0/2
'''
import re

if __name__ == '__main__':
    s = 'a aA aa user@mail.ru root@example.com 2021-01-02 2021-01-03 Андрей Семен Василий Олег апельсин'
    print('Строка для исследования:')
    print(s)
    # re.match() -> re.Match object
    # ищет вхождение в начале строки
    result = re.match('a', s)
    print('\n', result)
    if result is not None:
        print('совпадение: ', result.group())
        print('начало: ', result.start())
        print('конец: ', result.end())
        print('интервал: ', result.span())

    # re.search() -> re.Match object
    # ищет первое совпадение в строке
    result = re.search('aA', s)
    print('\n', result)
    if result is not None:
        print('совпадение: ', result.group())
        print('начало: ', result.start())
        print('конец: ', result.end())
        print('интервал: ', result.span())

    # re.findall() -> List[str]
    # ищет все совпадения в строке
    result = re.findall('a', s)
    print(result)

    # примеры регулярных выражений
    print('\nПримеры регулярных выражений:')
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
    # извлечь email в виде кортежей (имя_пользователя, домен)
    print(re.findall(r'(\w+)@(\w+.\w+)', s))
    # вернуть год из найденных дат
    print(re.findall(r'(\d{4})-\d{2}-\d{2}', s))
    # извлечь слова, начинающиеся на гласную
    print(re.findall(r'\b[уеыаоэяиюУЕЫАОЭЯИЮ]\w*', s))

    # итерация по результатм поиска, кроме кортежа найденных выражений мы получаем начало и конец вхождения
    for match in re.finditer(r'\b[уеыаоэяиюУЕЫАОЭЯИЮ]\w*', s):
        print(match.group(), match.start(), match.end())

    # заменить первые 3 слова на слово "word"
    print(re.sub(r'\b\w+', 'word', 'My name is Ivan', count=3))
    # заменить первые все слова начинающиеся на букву 'i' (без учета регистра) на слово "word"
    print(re.sub(r'\bi\w*', 'word', 'My name is Ivan', flags=re.IGNORECASE))

    # все слова на букву b не зависимо от регистра
    text = """ab Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."""
    print(re.findall(r'\bb\w*', text, flags=re.IGNORECASE))

    # удалить все знаки препинания
    sentence = """A, very very; irregular_sentence"""
    print(' '.join(re.findall(r'[A-Za-z]+', sentence)))
    print(' '.join(re.split(r'[,;_ ]+', sentence)))

    # очистить текст от всякой служебной хрени
    tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''


    def clean_tweet(tweet: str) -> str:
        tweet = re.sub(r'rt|cc', '', tweet, flags=re.IGNORECASE)
        tweet = re.sub(r'@\S+', '', tweet)
        tweet = re.sub(r'#\S+', '', tweet)
        tweet = re.sub(r'https\S+', '', tweet, flags=re.IGNORECASE)
        tweet = re.sub(r'\s+', ' ', tweet)
        return tweet


    print(clean_tweet(tweet))

    # извлечь текст между тегами
    html = '''
    <HTML>
    <HEAD>
    <TITLE>Your Title Here</TITLE>
    </HEAD>
    
    <BODY>
    <HR>
    <a href="http://someurl.com">Link Name</a>
    <H1>This is a Header</H1>
    <H2>This is a Medium Header</H2>
    <P>This is a new paragraph!</P>
    <P>This is a another paragraph!</P>
    <B>This is a new sentence without a paragraph break, in bold italics.</B>
    <HR>
    </BODY>
    </HTML>
    '''
    print(re.findall(r'<.+?>(.+?)<.+?>', html))

    # извлечь текст между тегами в разных строках
    html = '''
    <P>This is a new paragraph!
    Second line
    3 line</P>
    <P>This is. a another paragraph!</P>
    '''
    print(re.findall(r'<.+?>([\s\S]*?)<.+?>', html))

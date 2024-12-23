import pytest

from string_utils import StringUtils

string_util = StringUtils()

#Тест-кейс 1: делает первую букву заглавной и возвращает этот же текст.

@pytest.mark.parametrize('string, result', [
    
    #позитивные проверки:
    ("sam", "Sam"),
    ("аннаМария", "Аннамария"),
    ("mary Anne", "Mary anne"),
  
    #негативные проверки:
    ("", ""),
    ("123abc", "123abc"),
    ("MAX", "Max"),
  
])

def test_capitalize(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.capitalize(string)
    print(f"Actual result: {res}")
    assert res == result

#Тест-кейс 2: удаляет пробелы в начале, если они есть

@pytest.mark.parametrize('string, result', [
    
    #позитивные проверки:
    ("  boll", "boll"),
    (" ABC", "ABC"),
    ("  123  ", "123  "),

    #негативные проверки:
    ("", ""),
    ("sa d", "sa d"),
    ("doll", "doll"),

])
def test_trim(string, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    res = string_util.trim(string)
    print(f"Actual result: {res}")
    assert res == result

#Тест-кейс 3: текст с разделителем и возвращает список строк.

@pytest.mark.parametrize('string, divider, result', [
   
    #позитивные проверки:
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1,2,3,4,5", None, ["1", "2", "3", "4", "5"]),
    ("@^%^&^!^*", "^", ["@", "%", "&", "!", "*"]),

    #негативные проверки:
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
    ])

def test_to_list(string, divider, result):
    print(f"Input string: {string}")
    print(f"Expected result: {result}")
    
    if divider is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, divider)
    
    print(f"Actual result: {res}")
    
    assert res == result

#Тест-кейс 4: Возвращает `True`, если строка содержит искомый символ и `False` - если нет.

@pytest.mark.parametrize('string, symbol, result', [
    
    #позитивные проверки:
    ("toy", "t", True),
    (" fest", "f", True),
    ("123", "1", True),
    ("", "", True),

    #негативные проверки:
    ("Moscow", "m", False),
    ("parameter", "P", False),
    ("chair", "d", False),  
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Input string: {string}")
    print(f"Inputed symbol: {symbol}")
    print(f"Expected result: {result}")
    res = string_util.contains(string, symbol)
    print(f"Actual result: {res}")
    assert res == result

#Тест-кейс 5: Удаляет все подстроки из переданной строки.

@pytest.mark.parametrize('string, symbol, result', [
    
    #позитивные проверки:
    ("tom", "t", "om"),
    ("Creed", "r", "Ceed"),
    ("Town", "T", "own"),

    #негативные:
    ("toy", "v", "toy"),
    ("", "", ""),
])
def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    res = string_util.delete_symbol(string, symbol)
    assert res == result

#Тест-кейс 6: Возвращает `True`, если строка начинается с заданного символа и `False` - если нет

@pytest.mark.parametrize('string, symbol, result', [
    
    #позитивные проверки:
    ("parrot", "p", True),
    ("", "", True),
    ("Rabbit", "R", True),

    #негативные проверки:
    ("Walk", "w", False),
    ("bread", "B", False),
])
def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.starts_with(string, symbol)
    assert res == result

#Тест-кейс 7: Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет.

@pytest.mark.parametrize('string, symbol, result', [
   
    #позитивные проверки:
    ("bass", "s", True),
    ("COOL", "L", True),
    ("", "", True),
    ("canal ", "", True),

    #негативные проверки:
    ("what", "D", False),
    ("time", "t", False),
    ("can", "N", False),

])
def test_end_with(string, symbol, result):
    string_util = StringUtils()
    res = string_util.end_with(string, symbol)
    assert res == result

#Тест-кейс 8: Возвращает `True`, если строка пустая и `False` - если нет.

@pytest.mark.parametrize('string, result', [
    
    #позитивные проверки:
    ("", True),
    (" ", True),
    ("  ", True),

    #негативные проверки:
    ("from", False),
    (" not", False),
 
])
def test_is_empty(string, result):
    string_util = StringUtils()
    res = string_util.is_empty(string)
    assert res == result

#Тест-кейс 9: Преобразует список элементов в строку с указанным разделителем.

@pytest.mark.parametrize('lst, joiner, result', [
   
    #позитивные проверки:
    (["a", "b", "c"], ",", "a,b,c"),
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),

    #негативные проверки:
    ([], None, ""),
    ([], "*", "")
])
def test_list_to_string(lst, joiner, result):
    string_util = StringUtils()
    print(f"Input list: {lst}")
    print(f"Expected result: {result}")
    if joiner == None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, joiner)
    print(f"Actual result: {res}")
    assert res == result
def to_upper(s):
    """Функция переводит в верхний регистр"""
    return s.upper()

def capitalize_words(s):
    """Функция переводит первую  букву каждого слова в строке"""
    return ' '.join(word.capitalize() for word in s.split())



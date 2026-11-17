import math
M_DIV = 13
M_MUL = 16
A = 0.6180339887

LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

WORDS = ["У", "ЧУЖИХ", "РУКАХ", "ЗАВЖДИ", "ХЛІБИНА", "БІЛЬША", "А", "ПРАЦЯ", "ЛЕГША"]

def get_word_key(word: str) -> int:
    return sum(LETTER_POSITIONS.get(char, 0) for char in word)

def hash_division(key: int, m: int = M_DIV) -> int:
    return key % m

def hash_multiplication(key: int, m: int = M_MUL) -> int:
    return math.floor(m * ((key * A) % 1))

def build_open_hash_table(words: list, m: int, hash_func) -> list:
    hash_table = [[] for _ in range(m)]
    for word in words:
        key = get_word_key(word)
        address = hash_func(key, m)
        hash_table[address].append(word)
    return hash_table

def display_open_hash_table(table: list, title: str):
    print(f"\n--- {title} ---")
    for i, chain in enumerate(table):
        print(f"Індекс {i:02d}: {chain}")

# Виконання:
open_table_div = build_open_hash_table(WORDS, M_DIV, hash_division)
display_open_hash_table(open_table_div, "Відкрита хеш-таблиця (Метод ділення, M=13)")

open_table_mul = build_open_hash_table(WORDS, M_MUL, hash_multiplication)
display_open_hash_table(open_table_mul, "Відкрита хеш-таблиця (Метод множення, M=16)")

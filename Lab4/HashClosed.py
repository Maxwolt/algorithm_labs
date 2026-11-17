import math
M_DIV = 13
M_MUL = 16
A = 0.6180339887

WORDS = ["У", "ЧУЖИХ", "РУКАХ", "ЗАВЖДИ", "ХЛІБИНА", "БІЛЬША", "А", "ПРАЦЯ", "ЛЕГША"]

LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7,
    'Є': 8, 'Ж': 9, 'З': 10, 'И': 11, 'І': 12, 'Ї': 13,
    'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26,
    'Ц': 27, 'Ч': 28, 'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33 
}

def get_word_key(word: str) -> int:
    return sum(LETTER_POSITIONS.get(char, 0) for char in word)
def primary_hash_division(key: int, m: int = M_DIV) -> int:
    return key % m
def primary_hash_multiplication(key: int, m: int = M_MUL) -> int:
    return math.floor(m * ((key * A) % 1))
def build_closed_hash_table(words: list, m: int, hash_func) -> list:
    hash_table = [None] * m
    inserted_count = 0
    
    for word in words:
        key = get_word_key(word)
        start_address = hash_func(key, m)
        
        for i in range(m):
            address = (start_address + i) % m
            
            if hash_table[address] is None:
                hash_table[address] = word
                inserted_count += 1
                break
        else:
            print(f"Помилка: Таблиця заповнена (M={m}). Не вдалося додати слово: {word}")
            
    return hash_table

def display_hash_table(table: list, title: str):
    print(f"\n--- {title} ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
        value = item if item is not None else "(NULL)"
        print(f"{i:02d} | {value}")

# Виконання:
closed_table_div = build_closed_hash_table(WORDS, M_DIV, primary_hash_division)
display_hash_table(closed_table_div, f"Хеш-таблиця з відкритою адресацією (Метод ділення, M={M_DIV})")

closed_table_mul = build_closed_hash_table(WORDS, M_MUL, primary_hash_multiplication)
display_hash_table(closed_table_mul, f"Хеш-таблиця з відкритою адресацією (Метод множення, M={M_MUL})")

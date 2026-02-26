# # Задача 1: МП-автомат для языка (0^n1^n)+

# def simulate_pda_task1(input_string):
#     print(f"=== Задача 1: Вход = '{input_string}' ===")
    
#     Q_PUSH = 0
#     Q_POP = 1
#     Q_REJECT = 2
    

#     stack = ['Z']  
#     state = Q_PUSH
#     idx = 0
#     takt = 0
    
#     print(f"{'Такт':<6}{'Остаток':<15}{'Символ':<8}{'Состояние':<12}{'Действие':<20}Стек")
#     print("-" * 80)
    
#     while idx < len(input_string) and state != Q_REJECT:
#         takt += 1
#         c = input_string[idx]
#         action = ""
#         state_name = "q_push" if state == Q_PUSH else "q_pop" if state == Q_POP else "q_reject"
#         rest = input_string[idx+1:] if idx+1 < len(input_string) else ""
        

#         if state == Q_PUSH:
#             if c == '0':
#                 stack.append('X')
#                 action = "push(X)"
#                 idx += 1
#             elif c == '1':
#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X) -> q_pop"
#                     state = Q_POP
#                     idx += 1
#                 else:
#                     action = "ошибка: 1 без X"
#                     state = Q_REJECT
#             else:
#                 action = "неверный символ"
#                 state = Q_REJECT
        

#         elif state == Q_POP:
#             if c == '1':
#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X)"
#                     idx += 1
                    

#                     if len(stack) == 1 and stack[-1] == 'Z':
#                         if idx < len(input_string):
#                             if input_string[idx] == '0':
#                                 action += ", стек==Z -> q_push"
#                                 state = Q_PUSH
#                             else:
#                                 action += ", стек==Z и next==1 -> ошибка"
#                                 state = Q_REJECT
#                 else:
#                     action = "ошибка: поп из пустого блока"
#                     state = Q_REJECT
#             elif c == '0':
#                 action = "ошибка: 0 в режиме pop"
#                 state = Q_REJECT
#             else:
#                 action = "неверный символ"
#                 state = Q_REJECT
        

#         print(f"{takt:<6}{rest:<15}{c:<8}{state_name:<12}{action:<20}{stack}")
    

#     accepted = (state != Q_REJECT and 
#                 idx == len(input_string) and 
#                 len(stack) == 1 and stack[-1] == 'Z')
    
#     if accepted:
#         print("Результат: ACCEPT (цепочка принадлежит языку)")
#     else:
#         print("Результат: REJECT (цепочка НЕ принадлежит языку)")
    
#     print()

# print("=" * 60)
# print("ЗАДАЧА 1: МП-автомат для языка (0^n1^n)+")
# print("=" * 60)
# simulate_pda_task1("00110011")
# simulate_pda_task1("0011011")










# # Задача 2: МП-автомат для языка правильных скобочных выражений

# def simulate_pda_task2(input_string):
#     print(f"=== Задача 2: Вход = '{input_string}' ===")
    
#     Q_PUSH = 0
#     Q_REJECT = 1

#     stack = ['Z']  
#     state = Q_PUSH
#     idx = 0
#     takt = 0
    
#     print(f"{'Такт':<6}{'Остаток':<15}{'Символ':<8}{'Состояние':<12}{'Действие':<20}Стек")
#     print("-" * 80)
    
#     while idx < len(input_string) and state != Q_REJECT:
#         takt += 1
#         c = input_string[idx]
#         action = ""
#         state_name = "q_push" if state == Q_PUSH else "q_reject"
#         rest = input_string[idx+1:] if idx+1 < len(input_string) else ""

#         if state == Q_PUSH:
#             if c == '(':
#                 stack.append('X')
#                 action = "push(X)"
#                 idx += 1
#             elif c == ')':
#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X)"
#                     idx += 1
#                 else:
#                     action = "ошибка: ')' без '('"
#                     state = Q_REJECT
#             else:
#                 action = "неверный символ"
#                 state = Q_REJECT

#         print(f"{takt:<6}{rest:<15}{c:<8}{state_name:<12}{action:<20}{stack}")
    

#     accepted = (state != Q_REJECT and 
#                 idx == len(input_string) and 
#                 len(stack) == 1 and stack[-1] == 'Z')
    
#     if accepted:
#         print("Результат: ACCEPT (правильное скобочное выражение)")
#     else:
#         print("Результат: REJECT (НЕ правильное скобочное выражение)")
    
#     print()

# print("\n" + "=" * 60)
# print("ЗАДАЧА 2: МП-автомат для языка правильных скобочных выражений")
# print("=" * 60)
# simulate_pda_task2("(())()")
# simulate_pda_task2("(()")
# simulate_pda_task2(")(")













# # Задача 3: МП-автомат для языка a^k b^m c^k, где k=m или m=k

# def simulate_pda_task3(input_string):
#     print(f"=== Задача 3: Вход = '{input_string}' ===")
    

#     Q_START = 0
#     Q_A2B = 1  
#     Q_A2C = 2  
#     Q_REJECT = 3
    

#     stack = ['Z'] 
#     state = Q_START
#     idx = 0
#     takt = 0
    
#     print(f"{'Такт':<6}{'Остаток':<15}{'Символ':<8}{'Состояние':<12}{'Действие':<20}Стек")
#     print("-" * 80)
    
#     while idx < len(input_string) and state != Q_REJECT:
#         takt += 1
#         c = input_string[idx]
#         action = ""

#         if state == Q_START:
#             state_name = "q_start"
#         elif state == Q_A2B:
#             state_name = "q_a2b"
#         elif state == Q_A2C:
#             state_name = "q_a2c"
#         else:
#             state_name = "q_reject"
            
#         rest = input_string[idx+1:] if idx+1 < len(input_string) else ""
        

#         if state == Q_START:
#             if c == 'a':
#                 stack.append('X')
#                 action = "push(X)"
#                 idx += 1
#             elif c == 'b':

#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X) -> q_a2b"
#                     state = Q_A2B
#                     idx += 1
#                 else:
#                     action = "ошибка: нет 'a' для 'b'"
#                     state = Q_REJECT
#             elif c == 'c':

#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X) -> q_a2c"
#                     state = Q_A2C
#                     idx += 1
#                 else:
#                     action = "ошибка: нет 'a' для 'c'"
#                     state = Q_REJECT
#             else:
#                 action = "неверный символ"
#                 state = Q_REJECT
        

#         elif state == Q_A2B:
#             if c == 'b':
#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X)"
#                     idx += 1
#                 else:
#                     action = "лишний 'b'"
#                     state = Q_REJECT
#             elif c == 'c':

#                 action = "pass 'c'"
#                 idx += 1
#             else:
#                 action = "ошибка"
#                 state = Q_REJECT
        

#         elif state == Q_A2C:
#             if c == 'b':

#                 action = "pass 'b'"
#                 idx += 1
#             elif c == 'c':
#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X)"
#                     idx += 1
#                 else:
#                     action = "лишний 'c'"
#                     state = Q_REJECT
#             else:
#                 action = "ошибка"
#                 state = Q_REJECT

#         print(f"{takt:<6}{rest:<15}{c:<8}{state_name:<12}{action:<20}{stack}")

#     accepted = (state != Q_REJECT and 
#                 idx == len(input_string) and 
#                 len(stack) == 1 and stack[-1] == 'Z')
    
#     if accepted:
#         print("Результат: ACCEPT (цепочка принадлежит языку)")
#     else:
#         print("Результат: REJECT (цепочка НЕ принадлежит языку)")
    
#     print()

# print("\n" + "=" * 60)
# print("ЗАДАЧА 3: МП-автомат для языка a^k b^m c^k, где k=m или m=k")
# print("=" * 60)
# simulate_pda_task3("aabbcc")    # L1: a²b²c² (k=m=2)
# simulate_pda_task3("abbc")      # L2: a¹b²c¹ (m=k=1)
# simulate_pda_task3("aaabbbccc") # L1: a³b³c³ (k=m=3)
# simulate_pda_task3("aabccc")    # Ошибка: лишние c











# # Задача 4: GUI-симулятор МП-автомата для языка (0^n1^n)+

# import tkinter as tk
# from tkinter import ttk

# def pda_simulate(input_string):

#     Q_PUSH = 0
#     Q_POP = 1
#     Q_REJECT = 2

#     stack = ['Z']
#     state = Q_PUSH
#     idx = 0
#     steps = []
#     takt = 0
    
#     while idx < len(input_string) and state != Q_REJECT:
#         takt += 1
#         c = input_string[idx]
#         action = ""

#         if state == Q_PUSH:
#             state_name = "q_push"
#         elif state == Q_POP:
#             state_name = "q_pop"
#         else:
#             state_name = "q_reject"
        

#         if state == Q_PUSH:
#             if c == '0':
#                 stack.append('X')
#                 action = "push(X)"
#                 idx += 1
#             elif c == '1':
#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X) -> q_pop"
#                     state = Q_POP
#                     idx += 1
#                 else:
#                     action = "ошибка: 1 без X"
#                     state = Q_REJECT
#             else:
#                 action = "неверный символ"
#                 state = Q_REJECT
        

#         elif state == Q_POP:
#             if c == '1':
#                 if len(stack) >= 2 and stack[-1] == 'X':
#                     stack.pop()
#                     action = "pop(X)"
#                     idx += 1

#                     if len(stack) == 1 and stack[-1] == 'Z':
#                         if idx < len(input_string):
#                             if input_string[idx] == '0':
#                                 action += ", стек==Z -> q_push"
#                                 state = Q_PUSH
#                             else:
#                                 action += ", стек==Z и next==1 -> ошибка"
#                                 state = Q_REJECT
#                 else:
#                     action = "ошибка: поп из пустого блока"
#                     state = Q_REJECT
#             elif c == '0':
#                 action = "ошибка: 0 в режиме pop"
#                 state = Q_REJECT
#             else:
#                 action = "неверный символ"
#                 state = Q_REJECT
        

#         steps.append({
#             'takt': takt,
#             'rest': input_string[idx:] if idx < len(input_string) else "",
#             'symbol': c,
#             'state': state_name,
#             'action': action,
#             'stack': stack.copy()
#         })
    

#     accepted = (state != Q_REJECT and 
#                 idx == len(input_string) and 
#                 len(stack) == 1 and stack[-1] == 'Z')
    
#     return steps, accepted


# def stack_to_string(stack):
#     return "[" + " ".join(stack) + "]"


# class PDASimulatorGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PDA Симулятор для языка (0^n1^n)+")
#         self.root.geometry("900x600")
        

#         top_frame = tk.Frame(root)
#         top_frame.pack(pady=10, padx=10, fill=tk.X)
        
#         tk.Label(top_frame, text="Введите строку (только 0 и 1):", 
#                 font=("Arial", 11)).pack(side=tk.LEFT, padx=5)
        
#         self.entry = tk.Entry(top_frame, width=40, font=("Arial", 11))
#         self.entry.pack(side=tk.LEFT, padx=5)
#         self.entry.insert(0, "00110011")
        
#         tk.Button(top_frame, text="Запустить симуляцию", 
#                  command=self.run_simulation,
#                  font=("Arial", 11), bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=10)
        
#         tk.Button(top_frame, text="Очистить", 
#                  command=self.clear_table,
#                  font=("Arial", 11), bg="#f44336", fg="white").pack(side=tk.LEFT)

#         examples_frame = tk.Frame(root)
#         examples_frame.pack(pady=5, padx=10, fill=tk.X)
        
#         tk.Label(examples_frame, text="Примеры:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        
#         examples = ["00110011", "0011011", "01", "0011", "010011"]
#         for ex in examples:
#             btn = tk.Button(examples_frame, text=ex, 
#                            command=lambda e=ex: self.set_example(e),
#                            font=("Arial", 9))
#             btn.pack(side=tk.LEFT, padx=2)
        

#         columns = ("takt", "rest", "symbol", "state", "action", "stack")
#         self.tree = ttk.Treeview(root, columns=columns, show="headings", height=15)

#         headings = ["Такт", "Остаток", "Символ", "Состояние", "Действие", "Стек"]
#         widths = [60, 150, 80, 100, 250, 150]
        
#         for col, title, width in zip(columns, headings, widths):
#             self.tree.heading(col, text=title)
#             self.tree.column(col, width=width)
        

#         scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=self.tree.yview)
#         self.tree.configure(yscrollcommand=scrollbar.set)
        
#         self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=10)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)

#         self.result_label = tk.Label(root, text="Результат: ", 
#                                     font=("Arial", 14, "bold"))
#         self.result_label.pack(pady=10)
        

#         info_frame = tk.Frame(root, relief=tk.RIDGE, borderwidth=2)
#         info_frame.pack(pady=5, padx=10, fill=tk.X)
        
#         info_text = """Информация о языке (0^n1^n)+:
#         • Язык состоит из одного или нескольких блоков вида 0^n1^n
#         • Примеры правильных строк: 01, 0011, 00110011, 010011
#         • Примеры неправильных строк: 0011011, 0101, 001110"""
        
#         tk.Label(info_frame, text=info_text, 
#                 font=("Arial", 9), justify=tk.LEFT, wraplength=850).pack(pady=5, padx=5)
    
#     def set_example(self, example):
#         self.entry.delete(0, tk.END)
#         self.entry.insert(0, example)
    
#     def clear_table(self):
#         for item in self.tree.get_children():
#             self.tree.delete(item)
#         self.result_label.config(text="Результат: ", fg="black")
    
#     def run_simulation(self):
#         self.clear_table()
        
#         input_string = self.entry.get().strip()

#         if not all(c in "01" for c in input_string):
#             self.result_label.config(text="Ошибка: можно вводить только символы 0 и 1", 
#                                     fg="red")
#             return
        
#         if not input_string:
#             self.result_label.config(text="Ошибка: введите строку", fg="red")
#             return

#         steps, accepted = pda_simulate(input_string)

#         for step in steps:
#             self.tree.insert("", tk.END, values=(
#                 step['takt'],
#                 step['rest'],
#                 step['symbol'],
#                 step['state'],
#                 step['action'],
#                 stack_to_string(step['stack'])
#             ))

#         if accepted:
#             self.result_label.config(text=f"РЕЗУЛЬТАТ: ACCEPT (строка '{input_string}' принадлежит языку)", 
#                                     fg="green")
#         else:
#             self.result_label.config(text=f"РЕЗУЛЬТАТ: REJECT (строка '{input_string}' НЕ принадлежит языку)", 
#                                     fg="red")

# print("\n" + "=" * 60)
# print("ЗАДАЧА 4: GUI-симулятор МП-автомата")
# print("=" * 60)
# print("Запуск GUI приложения...")


# root = tk.Tk()
# app = PDASimulatorGUI(root)
# root.mainloop()












# # -*- coding: utf-8 -*-
# """
# Программа для построения таблиц идентификаторов тремя методами:
# 1. Метод логарифмического поиска (сортировка + бинарный поиск)
# 2. Метод рехэширования (открытая адресация)
# 3. Метод цепочек (chaining)

# Программа позволяет загружать данные из файла, строить таблицу выбранным методом,
# производить поиск и сравнивать методы по времени выполнения и количеству коллизий.
# """

# import time
# import os
# from bisect import bisect_left
# from typing import List, Optional, Tuple, Dict, Any

# # Размер хэш-таблицы (простое число для уменьшения коллизий)
# TABLE_SIZE = 101

# def hash_func(identifier: str) -> int:
#     """
#     Хэш-функция на основе кодов первых двух букв идентификатора.
    
#     Args:
#         identifier: Строка-идентификатор
        
#     Returns:
#         Хэш-значение в диапазоне [0, TABLE_SIZE-1]
#     """
#     if len(identifier) == 0:
#         return 0
#     if len(identifier) == 1:
#         return ord(identifier[0]) % TABLE_SIZE
#     return (ord(identifier[0]) * 31 + ord(identifier[1])) % TABLE_SIZE


# def rehash(h: int, i: int) -> int:
#     """
#     Линейное рехэширование для метода открытой адресации.
    
#     Args:
#         h: Исходное хэш-значение
#         i: Номер попытки (смещение)
        
#     Returns:
#         Новое хэш-значение
#     """
#     return (h + i) % TABLE_SIZE


# def measure_time(func):
#     """
#     Декоратор для измерения времени выполнения функции.
    
#     Args:
#         func: Функция для измерения времени
        
#     Returns:
#         Обернутая функция, возвращающая результат и время выполнения
#     """
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         execution_time = (end_time - start_time) * 1_000_000  # в микросекундах
#         return result, execution_time
#     return wrapper


# # -------------------------------------------------------------------
# # Метод 1: Логарифмический поиск (сортировка + бинарный поиск)
# # -------------------------------------------------------------------

# class LogarithmicSearchTable:
#     """Реализация таблицы идентификаторов методом логарифмического поиска."""
    
#     def __init__(self, identifiers: List[str]):
#         """
#         Инициализация таблицы.
        
#         Args:
#             identifiers: Список идентификаторов для добавления в таблицу
#         """
#         self.identifiers = list(set(identifiers))  # Удаляем дубликаты
#         self.sorted_table = sorted(self.identifiers)
#         self.collisions = 0  # Для данного метода коллизий нет
    
#     def build_table(self) -> Tuple[float, int]:
#         """
#         Построение таблицы (сортировка).
        
#         Returns:
#             Время построения и количество коллизий
#         """
#         start_time = time.perf_counter()
#         self.sorted_table = sorted(self.identifiers)
#         end_time = time.perf_counter()
#         build_time = (end_time - start_time) * 1_000_000
#         return build_time, self.collisions
    
#     def search(self, identifier: str) -> Tuple[bool, float]:
#         """
#         Поиск идентификатора в таблице методом бинарного поиска.
        
#         Args:
#             identifier: Идентификатор для поиска
            
#         Returns:
#             Флаг найден/не найден и время поиска
#         """
#         start_time = time.perf_counter()
        
#         # Ручная реализация бинарного поиска
#         left, right = 0, len(self.sorted_table) - 1
#         found = False
        
#         while left <= right:
#             mid = (left + right) // 2
#             if self.sorted_table[mid] == identifier:
#                 found = True
#                 break
#             elif self.sorted_table[mid] < identifier:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         end_time = time.perf_counter()
#         search_time = (end_time - start_time) * 1_000_000
        
#         return found, search_time
    
#     def display_table(self, limit: int = 20):
#         """Вывод содержимого таблицы."""
#         print(f"\nТаблица идентификаторов (метод логарифмического поиска):")
#         print(f"Всего уникальных идентификаторов: {len(self.sorted_table)}")
        
#         if len(self.sorted_table) <= limit:
#             print("Содержимое таблицы:")
#             for i, ident in enumerate(self.sorted_table):
#                 print(f"  {i:3d}: {ident}")
#         else:
#             print(f"Первые {limit} элементов таблицы:")
#             for i, ident in enumerate(self.sorted_table[:limit]):
#                 print(f"  {i:3d}: {ident}")
#             print(f"  ... и еще {len(self.sorted_table) - limit} элементов")


# # -------------------------------------------------------------------
# # Метод 2: Рехэширование (открытая адресация)
# # -------------------------------------------------------------------

# class RehashingTable:
#     """Реализация таблицы идентификаторов методом рехэширования."""
    
#     def __init__(self, identifiers: List[str]):
#         """
#         Инициализация таблицы.
        
#         Args:
#             identifiers: Список идентификаторов для добавления в таблицу
#         """
#         self.table = [""] * TABLE_SIZE
#         self.collisions = 0
#         self.build_table(identifiers)
    
#     def build_table(self, identifiers: List[str]) -> Tuple[float, int]:
#         """
#         Построение хэш-таблицы методом рехэширования.
        
#         Args:
#             identifiers: Список идентификаторов для добавления
            
#         Returns:
#             Время построения и количество коллизий
#         """
#         start_time = time.perf_counter()
        
#         for ident in identifiers:
#             h = hash_func(ident)
#             i = 0
            
#             # Поиск свободной ячейки или ячейки с таким же идентификатором
#             while self.table[h] != "" and self.table[h] != ident:
#                 i += 1
#                 self.collisions += 1
#                 h = rehash(h, i)
                
#                 # Защита от бесконечного цикла 
#                 if i >= TABLE_SIZE:
#                     raise MemoryError("Хэш-таблица переполнена")
            
#             # Вставляем идентификатор в найденную ячейку
#             self.table[h] = ident
        
#         end_time = time.perf_counter()
#         build_time = (end_time - start_time) * 1_000_000
        
#         return build_time, self.collisions
    
#     def search(self, identifier: str) -> Tuple[bool, float]:
#         """
#         Поиск идентификатора в хэш-таблице.
        
#         Args:
#             identifier: Идентификатор для поиска
            
#         Returns:
#             Флаг найден/не найден и время поиска
#         """
#         start_time = time.perf_counter()
        
#         h = hash_func(identifier)
#         i = 0
#         found = False
        
#         # Поиск по цепочке рехэширования
#         while self.table[h] != "":
#             if self.table[h] == identifier:
#                 found = True
#                 break
            
#             i += 1
#             h = rehash(h, i)
            
#             # Если прошли всю таблицу или вернулись к начальной позиции
#             if i >= TABLE_SIZE or h == hash_func(identifier):
#                 break
        
#         end_time = time.perf_counter()
#         search_time = (end_time - start_time) * 1_000_000
        
#         return found, search_time
    
#     def display_table(self, limit: int = 20):
#         """Вывод содержимого хэш-таблицы."""
#         print(f"\nХэш-таблица (метод рехэширования):")
#         print(f"Размер таблицы: {TABLE_SIZE}")
#         print(f"Количество коллизий при построении: {self.collisions}")
        
#         # Подсчет заполненных ячеек
#         filled_cells = sum(1 for cell in self.table if cell != "")
#         load_factor = filled_cells / TABLE_SIZE * 100
        
#         print(f"Заполненных ячеек: {filled_cells} ({load_factor:.1f}%)")
        
#         print("\nСодержимое таблицы (непустые ячейки):")
#         count = 0
#         for i, value in enumerate(self.table):
#             if value != "":
#                 print(f"  [{i:3d}]: {value}")
#                 count += 1
#                 if count >= limit:
#                     print(f"  ... и еще {filled_cells - limit} ячеек")
#                     break


# # -------------------------------------------------------------------
# # Метод 3: Метод цепочек (chaining)
# # -------------------------------------------------------------------

# class ChainingTable:
#     """Реализация таблицы идентификаторов методом цепочек."""
    
#     def __init__(self, identifiers: List[str]):
#         """
#         Инициализация таблицы.
        
#         Args:
#             identifiers: Список идентификаторов для добавления в таблицу
#         """
#         self.table = [[] for _ in range(TABLE_SIZE)]
#         self.collisions = 0
#         self.build_table(identifiers)
    
#     def build_table(self, identifiers: List[str]) -> Tuple[float, int]:
#         """
#         Построение хэш-таблицы методом цепочек.
        
#         Args:
#             identifiers: Список идентификаторов для добавления
            
#         Returns:
#             Время построения и количество коллизий
#         """
#         start_time = time.perf_counter()
        
#         for ident in identifiers:
#             h = hash_func(ident)
#             chain = self.table[h]
            
#             # Проверка на дубликаты в цепочке
#             if ident in chain:
#                 continue  # Пропускаем дубликаты
            
#             # Если цепочка не пустая - это коллизия
#             if chain:
#                 self.collisions += 1
            
#             # Добавляем идентификатор в цепочку
#             chain.append(ident)
        
#         end_time = time.perf_counter()
#         build_time = (end_time - start_time) * 1_000_000
        
#         return build_time, self.collisions
    
#     def search(self, identifier: str) -> Tuple[bool, float]:
#         """
#         Поиск идентификатора в хэш-таблице методом цепочек.
        
#         Args:
#             identifier: Идентификатор для поиска
            
#         Returns:
#             Флаг найден/не найден и время поиска
#         """
#         start_time = time.perf_counter()
        
#         h = hash_func(identifier)
#         chain = self.table[h]
#         found = identifier in chain
        
#         end_time = time.perf_counter()
#         search_time = (end_time - start_time) * 1_000_000
        
#         return found, search_time
    
#     def display_table(self, limit: int = 20):
#         """Вывод содержимого хэш-таблицы."""
#         print(f"\nХэш-таблица (метод цепочек):")
#         print(f"Размер таблицы: {TABLE_SIZE}")
#         print(f"Количество коллизий при построении: {self.collisions}")
        
#         # Статистика по цепочкам
#         non_empty_chains = sum(1 for chain in self.table if chain)
#         max_chain_length = max(len(chain) for chain in self.table) if non_empty_chains > 0 else 0
#         avg_chain_length = sum(len(chain) for chain in self.table) / TABLE_SIZE
        
#         print(f"Непустых цепочек: {non_empty_chains}")
#         print(f"Максимальная длина цепочки: {max_chain_length}")
#         print(f"Средняя длина цепочки: {avg_chain_length:.2f}")
        
#         print("\nСодержимое таблицы (непустые цепочки):")
#         count = 0
#         for i, chain in enumerate(self.table):
#             if chain:
#                 print(f"  [{i:3d}]: {' -> '.join(chain)}")
#                 count += 1
#                 if count >= limit:
#                     print(f"  ... и еще {non_empty_chains - limit} цепочек")
#                     break


# # -------------------------------------------------------------------
# # Функции для работы с файлами и меню
# # -------------------------------------------------------------------

# def load_identifiers_from_file(filename: str) -> List[str]:
#     """
#     Загрузка идентификаторов из текстового файла.
    
#     Args:
#         filename: Имя файла с идентификаторами
        
#     Returns:
#         Список идентификаторов
#     """
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             content = file.read()
#             # Разделяем по пробелам и удаляем пустые строки
#             identifiers = [word.strip() for word in content.split() if word.strip()]
        
#         print(f"\nФайл '{filename}' успешно загружен.")
#         print(f"Прочитано идентификаторов: {len(identifiers)}")
        
#         if len(identifiers) == 0:
#             print("Внимание: файл пуст или не содержит идентификаторов.")
        
#         return identifiers
    
#     except FileNotFoundError:
#         print(f"\nОшибка: файл '{filename}' не найден.")
#         print("Проверьте, что файл находится в той же папке, что и программа.")
#         return []
#     except Exception as e:
#         print(f"\nОшибка при чтении файла: {e}")
#         return []


# def create_test_file(filename: str = "identifiers.txt"):
#     """Создание тестового файла с идентификаторами, если он не существует."""
#     if not os.path.exists(filename):
#         test_identifiers = [
#             "main", "count", "total", "result", "sum", 
#             "index", "temp", "result", "sum", "item",
#             "variable", "function", "loop", "if", "else",
#             "while", "for", "return", "class", "struct",
#             "void", "int", "float", "double", "char",
#             "string", "array", "pointer", "reference", "const"
#         ]
        
#         try:
#             with open(filename, 'w', encoding='utf-8') as file:
#                 # Записываем идентификаторы с некоторыми повторениями
#                 for i in range(3):
#                     for ident in test_identifiers:
#                         if i == 0 or ident in ["main", "result", "sum"]:
#                             file.write(f"{ident} ")
            
#             print(f"\nСоздан тестовый файл '{filename}' с идентификаторами.")
#             return True
#         except Exception as e:
#             print(f"\nОшибка при создании тестового файла: {e}")
#             return False
#     return True


# def compare_methods(identifiers: List[str], test_identifier: str = None):
#     """
#     Сравнение всех трех методов по времени и коллизиям.
    
#     Args:
#         identifiers: Список идентификаторов для обработки
#         test_identifier: Идентификатор для тестового поиска
#     """
#     if not identifiers:
#         print("Нет данных для сравнения.")
#         return
    
#     if test_identifier is None:
#         test_identifier = identifiers[0] if identifiers else "test"
    
#     print("\n" + "="*70)
#     print("СРАВНИТЕЛЬНЫЙ АНАЛИЗ МЕТОДОВ ПОСТРОЕНИЯ ТАБЛИЦ ИДЕНТИФИКАТОРОВ")
#     print("="*70)
    
#     results = []
    
#     # Метод 1: Логарифмический поиск
#     print("\n1. Метод логарифмического поиска:")
#     print("-" * 40)
    
#     start_time = time.perf_counter()
#     table1 = LogarithmicSearchTable(identifiers)
#     build_time1, collisions1 = table1.build_table()
#     search_result1, search_time1 = table1.search(test_identifier)
#     total_time1 = (time.perf_counter() - start_time) * 1_000_000
    
#     results.append({
#         'method': 'Логарифмический поиск',
#         'build_time': build_time1,
#         'search_time': search_time1,
#         'total_time': total_time1,
#         'collisions': collisions1,
#         'search_result': search_result1
#     })
    
#     print(f"   Время построения: {build_time1:.2f} мкс")
#     print(f"   Время поиска '{test_identifier}': {search_time1:.2f} мкс")
#     print(f"   Коллизии: {collisions1}")
#     print(f"   Результат поиска: {'найден' if search_result1 else 'не найден'}")
    
#     # Метод 2: Рехэширование
#     print("\n2. Метод рехэширования:")
#     print("-" * 40)
    
#     start_time = time.perf_counter()
#     table2 = RehashingTable(identifiers)
#     build_time2, collisions2 = table2.build_table(identifiers)
#     search_result2, search_time2 = table2.search(test_identifier)
#     total_time2 = (time.perf_counter() - start_time) * 1_000_000
    
#     results.append({
#         'method': 'Рехэширование',
#         'build_time': build_time2,
#         'search_time': search_time2,
#         'total_time': total_time2,
#         'collisions': collisions2,
#         'search_result': search_result2
#     })
    
#     print(f"   Время построения: {build_time2:.2f} мкс")
#     print(f"   Время поиска '{test_identifier}': {search_time2:.2f} мкс")
#     print(f"   Коллизии: {collisions2}")
#     print(f"   Результат поиска: {'найден' if search_result2 else 'не найден'}")
    
#     # Метод 3: Цепочки
#     print("\n3. Метод цепочек:")
#     print("-" * 40)
    
#     start_time = time.perf_counter()
#     table3 = ChainingTable(identifiers)
#     build_time3, collisions3 = table3.build_table(identifiers)
#     search_result3, search_time3 = table3.search(test_identifier)
#     total_time3 = (time.perf_counter() - start_time) * 1_000_000
    
#     results.append({
#         'method': 'Цепочки',
#         'build_time': build_time3,
#         'search_time': search_time3,
#         'total_time': total_time3,
#         'collisions': collisions3,
#         'search_result': search_result3
#     })
    
#     print(f"   Время построения: {build_time3:.2f} мкс")
#     print(f"   Время поиска '{test_identifier}': {search_time3:.2f} мкс")
#     print(f"   Коллизии: {collisions3}")
#     print(f"   Результат поиска: {'найден' if search_result3 else 'не найден'}")
    
#     # Сводная таблица сравнения
#     print("\n" + "="*70)
#     print("СВОДНАЯ ТАБЛИЦА СРАВНЕНИЯ")
#     print("="*70)
    
#     print(f"{'Метод':<25} {'Построение (мкс)':<18} {'Поиск (мкс)':<15} {'Коллизии':<10} {'Результат':<10}")
#     print("-" * 80)
    
#     for result in results:
#         print(f"{result['method']:<25} {result['build_time']:<18.2f} "
#               f"{result['search_time']:<15.2f} {result['collisions']:<10} "
#               f"{'✓' if result['search_result'] else '✗':<10}")
    
#     # Определение лучшего метода по каждому критерию
#     print("\n" + "="*70)
#     print("ОЦЕНКА ЭФФЕКТИВНОСТИ МЕТОДОВ")
#     print("="*70)
    
#     # Лучший по времени построения
#     best_build = min(results, key=lambda x: x['build_time'])
#     print(f"• Самый быстрый метод построения: {best_build['method']} "
#           f"({best_build['build_time']:.2f} мкс)")
    
#     # Лучший по времени поиска
#     best_search = min(results, key=lambda x: x['search_time'])
#     print(f"• Самый быстрый метод поиска: {best_search['method']} "
#           f"({best_search['search_time']:.2f} мкс)")
    
#     # Лучший по количеству коллизий
#     best_collisions = min(results, key=lambda x: x['collisions'])
#     print(f"• Наименьшее количество коллизий: {best_collisions['method']} "
#           f"({best_collisions['collisions']})")
    
#     print("\n" + "="*70)


# def main_menu():
#     """Главное меню программы."""
#     identifiers = []
#     current_filename = ""
    
#     while True:
#         print("\n" + "="*60)
#         print("ТАБЛИЦЫ ИДЕНТИФИКАТОРОВ - ГЛАВНОЕ МЕНЮ")
#         print("="*60)
#         print("1. Загрузить идентификаторы из файла")
#         print("2. Метод логарифмического поиска")
#         print("3. Метод рехэширования")
#         print("4. Метод цепочек")
#         print("5. Сравнить все методы")
#         print("6. Создать тестовый файл")
#         print("7. Информация о программе")
#         print("0. Выход")
#         print("-"*60)
        
#         choice = input("Выберите действие (0-7): ").strip()
        
#         if choice == "0":
#             print("\nЗавершение работы программы. До свидания!")
#             break
        
#         elif choice == "1":
#             filename = input("Введите имя файла (по умолчанию: identifiers.txt): ").strip()
#             if not filename:
#                 filename = "identifiers.txt"
            
#             identifiers = load_identifiers_from_file(filename)
#             if identifiers:
#                 current_filename = filename
        
#         elif choice == "2":
#             if not identifiers:
#                 print("\nСначала загрузите идентификаторы из файла (пункт 1 меню).")
#                 continue
            
#             print("\nМЕТОД ЛОГАРИФМИЧЕСКОГО ПОИСКА")
#             print("-" * 40)
            
#             table = LogarithmicSearchTable(identifiers)
#             build_time, collisions = table.build_table()
            
#             print(f"Время построения таблицы: {build_time:.2f} мкс")
#             print(f"Количество уникальных идентификаторов: {len(table.sorted_table)}")
            
#             table.display_table()
            
#             search_id = input("\nВведите идентификатор для поиска (или Enter для пропуска): ").strip()
#             if search_id:
#                 found, search_time = table.search(search_id)
#                 print(f"\nПоиск идентификатора '{search_id}':")
#                 print(f"  Результат: {'НАЙДЕН' if found else 'НЕ НАЙДЕН'}")
#                 print(f"  Время поиска: {search_time:.2f} мкс")
        
#         elif choice == "3":
#             if not identifiers:
#                 print("\nСначала загрузите идентификаторы из файла (пункт 1 меню).")
#                 continue
            
#             print("\nМЕТОД РЕХЭШИРОВАНИЯ")
#             print("-" * 40)
            
#             table = RehashingTable(identifiers)
#             build_time, collisions = table.build_table(identifiers)
            
#             print(f"Время построения таблицы: {build_time:.2f} мкс")
#             print(f"Количество коллизий: {collisions}")
            
#             table.display_table()
            
#             search_id = input("\nВведите идентификатор для поиска (или Enter для пропуска): ").strip()
#             if search_id:
#                 found, search_time = table.search(search_id)
#                 print(f"\nПоиск идентификатора '{search_id}':")
#                 print(f"  Результат: {'НАЙДЕН' if found else 'НЕ НАЙДЕН'}")
#                 print(f"  Время поиска: {search_time:.2f} мкс")
        
#         elif choice == "4":
#             if not identifiers:
#                 print("\nСначала загрузите идентификаторы из файла (пункт 1 меню).")
#                 continue
            
#             print("\nМЕТОД ЦЕПОЧЕК")
#             print("-" * 40)
            
#             table = ChainingTable(identifiers)
#             build_time, collisions = table.build_table(identifiers)
            
#             print(f"Время построения таблицы: {build_time:.2f} мкс")
#             print(f"Количество коллизий: {collisions}")
            
#             table.display_table()
            
#             search_id = input("\nВведите идентификатор для поиска (или Enter для пропуска): ").strip()
#             if search_id:
#                 found, search_time = table.search(search_id)
#                 print(f"\nПоиск идентификатора '{search_id}':")
#                 print(f"  Результат: {'НАЙДЕН' if found else 'НЕ НАЙДЕН'}")
#                 print(f"  Время поиска: {search_time:.2f} мкс")
        
#         elif choice == "5":
#             if not identifiers:
#                 print("\nСначала загрузите идентификаторы из файла (пункт 1 меню).")
#                 continue
            
#             test_id = input(f"Введите идентификатор для тестового поиска (или Enter для '{identifiers[0]}'): ").strip()
#             if not test_id:
#                 test_id = identifiers[0]
            
#             compare_methods(identifiers, test_id)
        
#         elif choice == "6":
#             if create_test_file():
#                 print("Тестовый файл 'identifiers.txt' готов к использованию.")
        
#         elif choice == "7":
#             print("\n" + "="*60)
#             print("ИНФОРМАЦИЯ О ПРОГРАММЕ")
#             print("="*60)
#             print("Программа реализует три метода построения таблиц идентификаторов:")
#             print("1. Метод логарифмического поиска - сортировка + бинарный поиск")
#             print("2. Метод рехэширования - открытая адресация с линейным рехэшированием")
#             print("3. Метод цепочек - хэш-таблица с разрешением коллизий через списки")
#             print("\nПараметры:")
#             print(f"  • Размер хэш-таблицы: {TABLE_SIZE}")
#             print("  • Хэш-функция: на основе кодов первых двух букв")
#             print("\nДля работы программы необходим файл с идентификаторами.")
#             print("Можно использовать встроенную функцию создания тестового файла.")
#             print("="*60)
        
#         else:
#             print("\nНеверный выбор. Пожалуйста, введите число от 0 до 7.")


# def main():
#     """Точка входа в программу."""
#     print("\n" + "="*60)
#     print("ПРОГРАММА ДЛЯ ПОСТРОЕНИЯ ТАБЛИЦ ИДЕНТИФИКАТОРОВ")
#     print("="*60)
#     print("Реализация трех методов:")
#     print("1. Метод логарифмического поиска")
#     print("2. Метод рехэширования")
#     print("3. Метод цепочек")
#     print("="*60)
    
#     # Проверяем наличие тестового файла
#     if not os.path.exists("identifiers.txt"):
#         print("\nТестовый файл 'identifiers.txt' не найден.")
#         create = input("Создать тестовый файл? (y/n): ").strip().lower()
#         if create == 'y':
#             create_test_file()
    
#     # Запускаем главное меню
#     main_menu()


# if __name__ == "__main__":
#     main()









# # ---
# # Арифметический парсер на Python 3 с расширенными функциями
# # Реализованы задания для самостоятельной работы:
# # 1. Добавление операции возведения в степень ^ (правоассоциативной)
# # 2. Поддержка функций (sin, cos, pow, sqrt, log)
# # 3. Сообщения об ошибках с указанием позиции
# # 4. Поддержка переменных
# # ---

# from enum import Enum, auto
# import re
# import math
# from typing import Dict, List, Optional, Union

# # --- Токены ---
# class TokenType(Enum):
#     END = auto()
#     NUMBER = auto()
#     PLUS = auto()
#     MINUS = auto()
#     MUL = auto()
#     DIV = auto()
#     POWER = auto()        # ^
#     LPAREN = auto()
#     RPAREN = auto()
#     COMMA = auto()        # ,
#     IDENTIFIER = auto()   # имена переменных и функций
#     ASSIGN = auto()       # =

# class Token:
#     """Токен с типом, значением и позицией в исходной строке."""
#     def __init__(self, type_: TokenType, value=None, position: int = 0):
#         self.type = type_
#         self.value = value
#         self.position = position
    
#     def __repr__(self):
#         if self.type == TokenType.NUMBER:
#             return f"NUMBER({self.value})@{self.position}"
#         elif self.type == TokenType.IDENTIFIER:
#             return f"IDENTIFIER({self.value})@{self.position}"
#         return f"{self.type.name}@{self.position}"

# # --- Лексер с отслеживанием позиции ---
# class Lexer:
#     def __init__(self, text: str):
#         self.text = text
#         self.pos = 0
#         self.current_char = text[0] if text else None
    
#     def error(self, message: str):
#         raise SyntaxError(f"Ошибка лексера на позиции {self.pos}: {message}")
    
#     def advance(self):
#         """Перемещает указатель на следующий символ."""
#         self.pos += 1
#         if self.pos < len(self.text):
#             self.current_char = self.text[self.pos]
#         else:
#             self.current_char = None
    
#     def skip_whitespace(self):
#         """Пропускает пробельные символы."""
#         while self.current_char is not None and self.current_char.isspace():
#             self.advance()
    
#     def number(self) -> Token:
#         """Читает число (целое или вещественное)."""
#         start_pos = self.pos
#         result = ''
#         dot_count = 0
        
#         while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
#             if self.current_char == '.':
#                 dot_count += 1
#                 if dot_count > 1:
#                     self.error("Неверный формат числа: несколько точек")
#             result += self.current_char
#             self.advance()
        
#         # Если число заканчивается на точку
#         if result.endswith('.'):
#             result += '0'
        
#         return Token(TokenType.NUMBER, float(result), start_pos)
    
#     def identifier(self) -> Token:
#         """Читает идентификатор (имя переменной или функции)."""
#         start_pos = self.pos
#         result = ''
        
#         while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
#             result += self.current_char
#             self.advance()
        
#         return Token(TokenType.IDENTIFIER, result, start_pos)
    
#     def get_next_token(self) -> Token:
#         """Возвращает следующий токен."""
#         while self.current_char is not None:
#             # Пропускаем пробелы
#             if self.current_char.isspace():
#                 self.skip_whitespace()
#                 continue
            
#             # Числа
#             if self.current_char.isdigit() or (self.current_char == '.' and self.pos + 1 < len(self.text) and self.text[self.pos + 1].isdigit()):
#                 return self.number()
            
#             # Идентификаторы
#             if self.current_char.isalpha() or self.current_char == '_':
#                 return self.identifier()
            
#             # Операторы и разделители
#             start_pos = self.pos
#             char = self.current_char
            
#             if char == '+':
#                 self.advance()
#                 return Token(TokenType.PLUS, None, start_pos)
#             elif char == '-':
#                 self.advance()
#                 return Token(TokenType.MINUS, None, start_pos)
#             elif char == '*':
#                 self.advance()
#                 return Token(TokenType.MUL, None, start_pos)
#             elif char == '/':
#                 self.advance()
#                 return Token(TokenType.DIV, None, start_pos)
#             elif char == '^':
#                 self.advance()
#                 return Token(TokenType.POWER, None, start_pos)
#             elif char == '(':
#                 self.advance()
#                 return Token(TokenType.LPAREN, None, start_pos)
#             elif char == ')':
#                 self.advance()
#                 return Token(TokenType.RPAREN, None, start_pos)
#             elif char == ',':
#                 self.advance()
#                 return Token(TokenType.COMMA, None, start_pos)
#             elif char == '=':
#                 self.advance()
#                 return Token(TokenType.ASSIGN, None, start_pos)
#             else:
#                 self.error(f"Неизвестный символ: '{char}'")
        
#         return Token(TokenType.END, None, self.pos)

# # --- AST ---
# class Expr:
#     """Базовый класс выражений."""
#     def eval(self, variables: Dict[str, float] = None) -> float:
#         raise NotImplementedError
    
#     def to_string(self) -> str:
#         raise NotImplementedError

# class NumberExpr(Expr):
#     def __init__(self, value: float):
#         self.value = value
    
#     def eval(self, variables: Dict[str, float] = None) -> float:
#         return self.value
    
#     def to_string(self) -> str:
#         s = f"{self.value:.10g}"
#         return s.rstrip('0').rstrip('.') if '.' in s else s

# class VariableExpr(Expr):
#     def __init__(self, name: str):
#         self.name = name
    
#     def eval(self, variables: Dict[str, float] = None) -> float:
#         if variables is None or self.name not in variables:
#             raise NameError(f"Неизвестная переменная: '{self.name}'")
#         return variables[self.name]
    
#     def to_string(self) -> str:
#         return self.name

# class UnaryExpr(Expr):
#     def __init__(self, op: str, operand: Expr):
#         self.op = op
#         self.operand = operand
    
#     def eval(self, variables: Dict[str, float] = None) -> float:
#         v = self.operand.eval(variables)
#         return +v if self.op == '+' else -v
    
#     def to_string(self) -> str:
#         return f"{self.op}({self.operand.to_string()})"

# class BinaryExpr(Expr):
#     def __init__(self, op: str, left: Expr, right: Expr):
#         self.op = op
#         self.left = left
#         self.right = right
    
#     def eval(self, variables: Dict[str, float] = None) -> float:
#         a = self.left.eval(variables)
#         b = self.right.eval(variables)
        
#         if self.op == '+':
#             return a + b
#         elif self.op == '-':
#             return a - b
#         elif self.op == '*':
#             return a * b
#         elif self.op == '/':
#             if b == 0:
#                 raise ZeroDivisionError("Деление на ноль")
#             return a / b
#         elif self.op == '^':
#             return math.pow(a, b)
#         else:
#             raise ValueError(f"Неизвестный оператор: {self.op}")
    
#     def to_string(self) -> str:
#         return f"({self.left.to_string()} {self.op} {self.right.to_string()})"

# class FunctionCallExpr(Expr):
#     def __init__(self, func_name: str, args: List[Expr]):
#         self.func_name = func_name
#         self.args = args
    
#     def eval(self, variables: Dict[str, float] = None) -> float:
#         args_values = [arg.eval(variables) for arg in self.args]
        
#         if self.func_name == "sin":
#             if len(args_values) != 1:
#                 raise TypeError(f"Функция sin принимает 1 аргумент, получено {len(args_values)}")
#             return math.sin(args_values[0])
#         elif self.func_name == "cos":
#             if len(args_values) != 1:
#                 raise TypeError(f"Функция cos принимает 1 аргумент, получено {len(args_values)}")
#             return math.cos(args_values[0])
#         elif self.func_name == "tan":
#             if len(args_values) != 1:
#                 raise TypeError(f"Функция tan принимает 1 аргумент, получено {len(args_values)}")
#             return math.tan(args_values[0])
#         elif self.func_name == "sqrt":
#             if len(args_values) != 1:
#                 raise TypeError(f"Функция sqrt принимает 1 аргумент, получено {len(args_values)}")
#             if args_values[0] < 0:
#                 raise ValueError("Корень из отрицательного числа")
#             return math.sqrt(args_values[0])
#         elif self.func_name == "log":
#             if len(args_values) == 1:
#                 if args_values[0] <= 0:
#                     raise ValueError("Логарифм от неположительного числа")
#                 return math.log(args_values[0])
#             elif len(args_values) == 2:
#                 if args_values[0] <= 0 or args_values[1] <= 0 or args_values[1] == 1:
#                     raise ValueError("Недопустимые аргументы для логарифма")
#                 return math.log(args_values[0], args_values[1])
#             else:
#                 raise TypeError(f"Функция log принимает 1 или 2 аргумента, получено {len(args_values)}")
#         elif self.func_name == "pow" or self.func_name == "power":
#             if len(args_values) != 2:
#                 raise TypeError(f"Функция pow принимает 2 аргумента, получено {len(args_values)}")
#             return math.pow(args_values[0], args_values[1])
#         elif self.func_name == "abs":
#             if len(args_values) != 1:
#                 raise TypeError(f"Функция abs принимает 1 аргумент, получено {len(args_values)}")
#             return abs(args_values[0])
#         elif self.func_name == "exp":
#             if len(args_values) != 1:
#                 raise TypeError(f"Функция exp принимает 1 аргумент, получено {len(args_values)}")
#             return math.exp(args_values[0])
#         else:
#             raise NameError(f"Неизвестная функция: '{self.func_name}'")
    
#     def to_string(self) -> str:
#         args_str = ", ".join(arg.to_string() for arg in self.args)
#         return f"{self.func_name}({args_str})"

# class AssignmentExpr(Expr):
#     def __init__(self, var_name: str, value_expr: Expr):
#         self.var_name = var_name
#         self.value_expr = value_expr
    
#     def eval(self, variables: Dict[str, float] = None) -> float:
#         if variables is None:
#             raise NameError("Контекст переменных не инициализирован")
#         value = self.value_expr.eval(variables)
#         variables[self.var_name] = value
#         return value
    
#     def to_string(self) -> str:
#         return f"{self.var_name} = {self.value_expr.to_string()}"

# # --- Парсер с улучшенной обработкой ошибок ---
# class Parser:
#     """Рекурсивный парсер для арифметических выражений с поддержкой функций, переменных и степени."""
    
#     def __init__(self, text: str):
#         self.lexer = Lexer(text)
#         self.current_token = self.lexer.get_next_token()
#         self.variables = {}
    
#     def error(self, message: str):
#         raise SyntaxError(f"Ошибка синтаксиса на позиции {self.current_token.position}: {message}")
    
#     def eat(self, token_type: TokenType):
#         """Проверяет текущий токен и переходит к следующему."""
#         if self.current_token.type == token_type:
#             self.current_token = self.lexer.get_next_token()
#         else:
#             self.error(f"Ожидался {token_type.name}, получен {self.current_token.type.name}")
    
#     def parse(self) -> Expr:
#         """Парсит выражение (может быть присваиванием или просто выражением)."""
#         # Проверяем, не является ли это присваиванием
#         if self.current_token.type == TokenType.IDENTIFIER:
#             # Сохраняем токен для проверки
#             identifier_token = self.current_token
#             identifier_name = identifier_token.value
            
#             # Смотрим следующий токен
#             next_token = self.lexer.get_next_token()
#             # Временно сохраняем текущий токен
#             old_current_token = self.current_token
            
#             # Если следующий токен =, то это присваивание
#             if next_token.type == TokenType.ASSIGN:
#                 # Это присваивание
#                 self.current_token = identifier_token  # Возвращаемся к имени переменной
#                 self.eat(TokenType.IDENTIFIER)
#                 self.eat(TokenType.ASSIGN)
#                 expr = self.parse_expression()
#                 return AssignmentExpr(identifier_name, expr)
#             else:
#                 # Это не присваивание, возвращаемся назад
#                 self.lexer.pos = identifier_token.position
#                 self.lexer.current_char = self.lexer.text[identifier_token.position] if identifier_token.position < len(self.lexer.text) else None
#                 self.current_token = self.lexer.get_next_token()
        
#         # Обычное выражение
#         expr = self.parse_expression()
        
#         if self.current_token.type != TokenType.END:
#             self.error("Неожиданный ввод после конца выражения")
        
#         return expr
    
#     def parse_expression(self) -> Expr:
#         """Парсит выражение уровня сложения/вычитания."""
#         node = self.parse_term()
        
#         while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
#             token = self.current_token
#             if token.type == TokenType.PLUS:
#                 self.eat(TokenType.PLUS)
#                 node = BinaryExpr('+', node, self.parse_term())
#             elif token.type == TokenType.MINUS:
#                 self.eat(TokenType.MINUS)
#                 node = BinaryExpr('-', node, self.parse_term())
        
#         return node
    
#     def parse_term(self) -> Expr:
#         """Парсит выражение уровня умножения/деления."""
#         node = self.parse_factor()
        
#         while self.current_token.type in (TokenType.MUL, TokenType.DIV):
#             token = self.current_token
#             if token.type == TokenType.MUL:
#                 self.eat(TokenType.MUL)
#                 node = BinaryExpr('*', node, self.parse_factor())
#             elif token.type == TokenType.DIV:
#                 self.eat(TokenType.DIV)
#                 node = BinaryExpr('/', node, self.parse_factor())
        
#         return node
    
#     def parse_factor(self) -> Expr:
#         """Парсит выражение уровня степени (правоассоциативное)."""
#         node = self.parse_unary()
        
#         if self.current_token.type == TokenType.POWER:
#             self.eat(TokenType.POWER)
#             # Правоассоциативность: a^b^c = a^(b^c)
#             right = self.parse_factor()
#             node = BinaryExpr('^', node, right)
        
#         return node
    
#     def parse_unary(self) -> Expr:
#         """Парсит унарные операторы + и -."""
#         token = self.current_token
        
#         if token.type == TokenType.PLUS:
#             self.eat(TokenType.PLUS)
#             node = self.parse_unary()
#             return UnaryExpr('+', node)
#         elif token.type == TokenType.MINUS:
#             self.eat(TokenType.MINUS)
#             node = self.parse_unary()
#             return UnaryExpr('-', node)
        
#         return self.parse_primary()
    
#     def parse_primary(self) -> Expr:
#         """Парсит первичные выражения: числа, переменные, скобки, вызовы функций."""
#         token = self.current_token
        
#         if token.type == TokenType.NUMBER:
#             self.eat(TokenType.NUMBER)
#             return NumberExpr(token.value)
        
#         elif token.type == TokenType.IDENTIFIER:
#             identifier_name = token.value
#             self.eat(TokenType.IDENTIFIER)
            
#             # Проверяем, не является ли это вызовом функции
#             if self.current_token.type == TokenType.LPAREN:
#                 self.eat(TokenType.LPAREN)
#                 args = []
                
#                 # Если есть аргументы
#                 if self.current_token.type != TokenType.RPAREN:
#                     args.append(self.parse_expression())
                    
#                     while self.current_token.type == TokenType.COMMA:
#                         self.eat(TokenType.COMMA)
#                         args.append(self.parse_expression())
                
#                 self.eat(TokenType.RPAREN)
#                 return FunctionCallExpr(identifier_name, args)
#             else:
#                 # Простая переменная
#                 return VariableExpr(identifier_name)
        
#         elif token.type == TokenType.LPAREN:
#             self.eat(TokenType.LPAREN)
#             node = self.parse_expression()
#             self.eat(TokenType.RPAREN)
#             return node
        
#         self.error(f"Ожидалось число, переменная, функция или '('")

# # --- Основная программа ---
# def main():
#     """Основная функция программы."""
#     print("=" * 60)
#     print("Арифметический калькулятор с расширенными функциями")
#     print("=" * 60)
#     print("Поддерживаемые операции: + - * / ^ (степень)")
#     print("Поддерживаемые функции: sin, cos, tan, sqrt, log, pow, abs, exp")
#     print("Поддерживаются переменные (например: x = 5, затем 2 * x)")
#     print("Введите 'exit' для выхода")
#     print("=" * 60)
    
#     variables = {}
#     tests = [
#         # Базовые тесты
#         "2 + 3 * 4",
#         "(2 + 3) * 4",
#         "-5 + 2",
#         "-(2 + 3) * 4",
#         "2 + 3 * 4 - 5",
#         "3.5 + 1.25 * (2 - 0.5)",
        
#         # Тесты для степени (задание 1)
#         "2 ^ 3",
#         "2 ^ 3 ^ 2",  # Правоассоциативность: 2^(3^2) = 2^9 = 512
#         "(2 ^ 3) ^ 2",  # Левая ассоциативность в скобках: 8^2 = 64
#         "4 ^ 0.5",  # Квадратный корень
#         "-2 ^ 2",  # Унарный минус имеет более высокий приоритет: -(2^2) = -4
        
#         # Тесты для функций (задание 2)
#         "sin(0)",
#         "cos(0)",
#         "sqrt(16)",
#         "log(100, 10)",  # log10(100) = 2
#         "pow(2, 3)",
#         "abs(-5)",
        
#         # Тесты для переменных (задание 4)
#         "x = 5",
#         "y = 10",
#         "x + y",
#         "x * y - 3",
        
#         # Комбинированные тесты
#         "sin(pi/2)",  # pi пока не определен, но можно определить
#         "sqrt(x^2 + y^2)",
#     ]
    
#     # Добавляем pi в переменные
#     variables['pi'] = math.pi
#     variables['e'] = math.e
    
#     print("\nВыполнение встроенных тестов:")
#     print("-" * 60)
    
#     for test in tests:
#         try:
#             print(f"\nВвод: {test}")
#             parser = Parser(test)
#             parser.variables = variables
#             ast = parser.parse()
#             result = ast.eval(variables)
#             print(f"AST: {ast.to_string()}")
#             print(f"Результат: {result}")
            
#             # Обновляем переменные из парсера
#             variables.update(parser.variables)
#         except Exception as e:
#             print(f"Ошибка: {type(e).__name__}: {e}")
    
#     print("\n" + "=" * 60)
#     print("Интерактивный режим:")
#     print("=" * 60)
    
#     while True:
#         try:
#             line = input("\n> ").strip()
            
#             if line.lower() in ('exit', 'quit', 'выход'):
#                 print("Выход из программы.")
#                 break
#             elif not line:
#                 continue
            
#             parser = Parser(line)
#             parser.variables = variables
#             ast = parser.parse()
#             result = ast.eval(variables)
            
#             print(f"AST: {ast.to_string()}")
#             print(f"Результат: {result}")
            
#             # Обновляем переменные из парсера
#             variables.update(parser.variables)
            
#             # Показываем текущие переменные
#             if variables:
#                 print(f"Текущие переменные: {', '.join(f'{k}={v}' for k, v in variables.items() if k not in ('pi', 'e'))}")
            
#         except EOFError:
#             print("\nВыход из программы.")
#             break
#         except KeyboardInterrupt:
#             print("\nВыход из программы.")
#             break
#         except Exception as e:
#             print(f"Ошибка: {type(e).__name__}: {e}")

# # --- Пример использования и документация ---
# if __name__ == "__main__":
#     print(__doc__)
    
#     # Дополнительные примеры
#     examples = [
#         ("2 + 3 * 4", "Базовое выражение"),
#         ("2 ^ 3 ^ 2", "Правоассоциативная степень (2^(3^2) = 512)"),
#         ("sin(pi/2)", "Тригонометрическая функция"),
#         ("x = 10; y = 20; x * y", "Работа с переменными"),
#         ("sqrt(16) + abs(-5)", "Комбинация функций"),
#     ]
    
#     print("\nПримеры использования:")
#     for expr, desc in examples:
#         print(f"  {expr:30} - {desc}")
    
#     print()
#     main()





# from scipy.integrate import quad
# import numpy as np

# # Определяем функцию
# def my_function(x):
#     return np.sin(x)

# # Вычисляем интеграл от 0 до pi
# # quad возвращает кортеж (результат, оценка ошибки)
# integral_result, error = quad(my_function, 0, np.pi)
# print(f"Численный интеграл (quad): {integral_result} (Ошибка: {error})")





# def val_card(number):
    
#     if len(number) != 16:
#         return False, "Номер должен содержать ровно 16 символов"

#     if not number.isdigit():
#         return False, "Номер должен состоять только из цифр"

#     total_sum = 0
#     for i in range(16):
#         digit = int(number[i])

#         if (15 - i) % 2 == 0:
#             digit *= 2
#             if digit > 9:
#                 digit -= 9
        
#         total_sum += digit

#     if total_sum % 10 == 0:
#         return True, "Номер карты валиден"
#     else:
#         return False, "Неверная контрольная сумма"

# def cal_cost():

#     BASE_COST = 10000
    
#     try:
#         age = int(input("Введите возраст водителя: "))
#         experience = int(input("Введите стаж вождения (лет): "))
#         has_accidents = input("Были ли аварии за последние 3 года? (да/нет): ").lower().strip()
#         if age <= 0 or experience < 0 or experience > age - 16:
#             return "Ошибка: некорректные данные"
#         if age < 25:
#             age_coef = 1.5
#         elif age <= 65:
#             age_coef = 1.0
#         else:
#             age_coef = 1.8

#         if experience < 2:
#             exp_coef = 1.2
#         elif experience <= 10:
#             exp_coef = 1.0
#         else:
#             exp_coef = 0.85

#         accident_coef = 1.25 if has_accidents in ['да', 'yes', 'y', 'д'] else 1.0

#         total_cost = BASE_COST * age_coef * exp_coef * accident_coef
#         return f"Стоимость полиса: {total_cost:.2f} руб."
    
#     except ValueError:
#         return "Ошибка: введите числовые значения"

# def test_card_val():

#     print("=== ТЕСТИРОВАНИЕ ВАЛИДАЦИИ КРЕДИТНЫХ КАРТ ===\n")

#     print("1. МЕТОД ПОКРЫТИЯ ОПЕРАТОРОВ:")
#     test_cases = [
#         "1234567812345670", 
#         "1234567812345678",  
#         "123456789012345",  
#         "12345678901234567", 
#         "1234abc567890123",  
#     ]
    
#     for i, card in enumerate(test_cases, 1):
#         result, message = val_card(card)
#         print(f"Тест {i}: {card} -> {message}")
    
#     print("\n2. МЕТОД ПОКРЫТИЯ УСЛОВИЙ:")
#     conditions_tests = [
#         ("123", False),
#         ("abcdefghijklmnop", False),
#         ("1111111111111111", False),
#         ("4561261212345467", True),
#     ]
    
#     for i, (card, expected) in enumerate(conditions_tests, 1):
#         result, message = val_card(card)
#         status = "✓" if result == expected else "✗"
#         print(f"Тест {i}: {card} -> {message} {status}")
    
#     print("\n3. КОМБИНАТОРНОЕ ПОКРЫТИЕ (Алгоритм Луна):")
#     luhn_tests = [
#         ("0000000000000000", True), 
#         ("5555555555555555", False),
#         ("4111111111111111", True),  
#         ("5500000000000004", True),  
#     ]
    
#     for i, (card, expected) in enumerate(luhn_tests, 1):
#         result, message = val_card(card)
#         status = "✓" if result == expected else "✗"
#         print(f"Тест {i}: {card} -> {message} {status}")

# def test_calc():

#     print("\n=== ТЕСТИРОВАНИЕ РАСЧЕТА СТРАХОВОГО ПОЛИСА ===\n")

#     test_data = [

#         (20, 1, True), 
#         (30, 5, False), 
#         (70, 20, False), 
#         (25, 2, True),   
#         (65, 10, False),
#     ]
    
#     print("1. МЕТОД ПОКРЫТИЯ ОПЕРАТОРОВ:")
#     BASE_COST = 10000
#     for age, exp, accidents in test_data:

#         age_coef = 1.5 if age < 25 else 1.0 if age <= 65 else 1.8
#         exp_coef = 1.2 if exp < 2 else 1.0 if exp <= 10 else 0.85
#         accident_coef = 1.25 if accidents else 1.0
#         cost = BASE_COST * age_coef * exp_coef * accident_coef
        
#         print(f"Возраст: {age}, Стаж: {exp}, Аварии: {accidents}")
#         print(f"Коэффициенты: возраст={age_coef}, стаж={exp_coef}, аварии={accident_coef}")
#         print(f"Итоговая стоимость: {cost:.2f} руб.\n")

#     print("2. МЕТОД ПОКРЫТИЯ УСЛОВИЙ:")
#     conditions = [

#         (24, 5, False),  
#         (25, 5, False), 
#         (66, 5, False),  
        
#         (30, 1, False), 
#         (30, 2, False), 
#         (30, 11, False), 
        
#         (30, 5, True),   
#         (30, 5, False),  
#     ]
    
#     for i, (age, exp, accidents) in enumerate(conditions, 1):
#         age_coef = 1.5 if age < 25 else 1.0 if age <= 65 else 1.8
#         exp_coef = 1.2 if exp < 2 else 1.0 if exp <= 10 else 0.85
#         accident_coef = 1.25 if accidents else 1.0
#         cost = BASE_COST * age_coef * exp_coef * accident_coef
        
#         print(f"Тест {i}: Возраст={age}, Стаж={exp}, Аварии={accidents}")
#         print(f"Стоимость: {cost:.2f} руб.")

#     print("\n3. КОМБИНАТОРНОЕ ПОКРЫТИЕ УСЛОВИЙ:")
#     combinations = [
#         (20, 1, True),  
#         (20, 1, False), 
#         (40, 15, False),
#         (70, 50, False),
#         (70, 1, True), 
#     ]
    
#     for i, (age, exp, accidents) in enumerate(combinations, 1):
#         age_coef = 1.5 if age < 25 else 1.0 if age <= 65 else 1.8
#         exp_coef = 1.2 if exp < 2 else 1.0 if exp <= 10 else 0.85
#         accident_coef = 1.25 if accidents else 1.0
#         cost = BASE_COST * age_coef * exp_coef * accident_coef
        
#         print(f"Комбинация {i}: Возраст={age}, Стаж={exp}, Аварии={accidents}")
#         print(f"Стоимость: {cost:.2f} руб. (коэф: {age_coef}×{exp_coef}×{accident_coef})")

# if __name__ == "__main__":
#     test_card_val()
#     test_calc()
#     print("\n=== ИНТЕРАКТИВНЫЙ РАСЧЕТ СТРАХОВКИ ===")
#     print("Пример ввода для теста:")
#     print("Возраст: 30")
#     print("Стаж: 5") 
#     print("Аварии: нет")
#     result = cal_cost()
#     print(result)













# Практика 8
# Задание 1
# Для мобильного приложения подсчета шагов используется методика черного ящика, так как исходный код для нас недоступен недоступен.
# Соответственно нам нужно обратится к методу, позволяющему что-то сделать даже при нехватке информации, то есть метод черного ящика.

# Задание 2
# Преподаватель использует комбинированный подход: белый ящик, то есть анализ кода, и черный ящик, то есть запуск программы.

# Задание 3
# Бабушка будет использовать методику черного ящика, так как не знает внутренней реализации PHP-приложения, и языки все таки отличаются. 
# Полагаясь на интуицию и общие знания о языках программирования, и ипользуя метод черного ящика, ей возможно удастьтся разобратся.

# Задание 4
# Для доступных 50% модулей можно использовать белый ящик, для недоступных - черный ящик. Таким образом известные данные мы используем как они есть,
# остальные придется проверять методом черного ящика.

# Задание 5
# Для программы проверки параболы целесообразнее использовать белый ящик, так как код доступен и можно обеспечить максимальное покрытие.
# def count(qwwe):
#     a,b,c,x,y = qwwe
#     if a != 0:
#         if y == a * x * x + b * x + c:
#             print("Точка принадлежит параболе")
#         else:
#             print("Точка не принадлежит параболе")
#     else:
#         print("Это не парабола")
# #Позитивные тесты
# count(qwwe=[1,2,3,2,11])
# count(qwwe=[1,2,2,0,2])
# count(qwwe=[1,-2,0,2,0])
# # Негативные тесты
# count(qwwe=[0,2,3,2,1])
# count(qwwe=[1,2,2,0,10011])
# count(qwwe=[1,-2,0,-1.834012,0])









#Лабораторная 19

# Задание 1: Преобразование оценки в текст
# print("=== Задание 1: Преобразование оценки ===")
# grade = int(input("Введите оценку (2-5): "))

# match grade:
#     case 5:
#         print("Отлично")
#     case 4:
#         print("Хорошо")
#     case 3:
#         print("Удовлетворительно")
#     case 2:
#         print("Неудовлетворительно")
#     case _:
#         print("Неверная оценка")

# # Задание 2: День недели
# print("\n=== Задание 2: День недели ===")
# day_number = int(input("Введите номер дня недели (1-7): "))

# match day_number:
#     case 1:
#         print("Понедельник")
#     case 2:
#         print("Вторник")
#     case 3:
#         print("Среда")
#     case 4:
#         print("Четверг")
#     case 5:
#         print("Пятница")
#     case 6:
#         print("Суббота")
#     case 7:
#         print("Воскресенье")
#     case _:
#         print("Неверный день недели")

# # Задание 3: Время года
# print("\n=== Задание 3: Время года ===")
# month = int(input("Введите номер месяца (1-12): "))

# match month:
#     case 12 | 1 | 2:
#         print("Зима")
#     case 3 | 4 | 5:
#         print("Весна")
#     case 6 | 7 | 8:
#         print("Лето")
#     case 9 | 10 | 11:
#         print("Осень")
#     case _:
#         print("Неверный номер месяца")

# # Задание 4: Разница с break и без break
# print("\n=== Задание 4: Успеваемость (с break) ===")
# grade_letter = input("Введите буквенную оценку (A, B, C, D, F): ").upper()

# # С break (как в switch-case)
# match grade_letter:
#     case 'A':
#         print("Отлично")
#     case 'B':
#         print("Хорошо")
#     case 'C':
#         print("Удовлетворительно")
#     case 'D':
#         print("Плохо")
#     case 'F':
#         print("Неудовлетворительно")
#     case _:
#         print("Неизвестная оценка")

# print("\n=== Задание 4: Успеваемость (без break - аналог) ===")
# # Без break (аналог последовательных if)
# if grade_letter == 'A':
#     print("Отлично")
# if grade_letter == 'B':
#     print("Хорошо")
# if grade_letter == 'C':
#     print("Удовлетворительно")
# if grade_letter == 'D':
#     print("Плохо")
# if grade_letter == 'F':
#     print("Неудовлетворительно")

# # Задание 5: Числа от 10 до 1 в обратном порядке
# print("\n=== Задание 5: Числа от 10 до 1 ===")
# for i in range(10, 0, -1):
#     print(i, end=" ")
# print()

# # Задание 6: Нечетные числа от 1 до 20
# print("\n=== Задание 6: Нечетные числа от 1 до 20 ===")
# for i in range(1, 21, 2):
#     print(i, end=" ")
# print()

# # Задание 7: Умножение счетчиков
# print("\n=== Задание 7: Умножение счетчиков ===")
# for i in range(1, 5):
#     for j in range(1, 5):
#         if i < 5 and j < 5:
#             print(f"{i} * {j} = {i * j}")

# # Задание 8: Таблица умножения
# print("\n=== Задание 8: Таблица умножения ===")
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} * {j} = {i * j}")

# # Задание 9: Средний балл студентов
# print("\n=== Задание 9: Средний балл студентов ===")
# students = [
#     ["Анна", [4, 5, 3, 4]],
#     ["Иван", [5, 5, 4, 5]],
#     ["Мария", [3, 4, 5, 3]]
# ]

# for student in students:
#     name = student[0]
#     grades = student[1]
#     average = sum(grades) / len(grades)
#     print(f"{name}: средний балл = {average:.2f}")


#Лабораторная 20
# Задание 1: Сумма чисел от 1 до 100
# print("=== Задание 1: Сумма чисел от 1 до 100 ===")
# total = 0
# for i in range(1, 101):
#     total += i
# print(f"Сумма чисел от 1 до 100: {total}")

# # Задание 2: Четные числа от 2 до 20
# print("\n=== Задание 2: Четные числа от 2 до 20 ===")
# num = 2
# while num <= 20:
#     print(num, end=" ")
#     num += 2
# print()

# # Задание 3: Переворот строки
# print("\n=== Задание 3: Переворот строки ===")
# text = "JavaScript"
# reversed_text = ""
# for char in text:
#     reversed_text = char + reversed_text
# print(f"Исходная строка: {text}")
# print(f"Перевернутая строка: {reversed_text}")

# # Задание 4: Первое число больше 10
# print("\n=== Задание 4: Первое число больше 10 ===")
# numbers = [5, 12, 8, 130, 44]
# for num in numbers:
#     if num > 10:
#         print(f"Первое число больше 10: {num}")
#         break

# # Задание 5: Все элементы кроме 3
# print("\n=== Задание 5: Все элементы кроме 3 ===")
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     if num == 3:
#         continue
#     print(num, end=" ")
# print()

# # Задание 6: Пары ключ-значение объекта
# print("\n=== Задание 6: Пары ключ-значение ===")
# user = {"name": "Alice", "age": 25, "job": "Developer"}
# for key in user:
#     print(f"{key}: {user[key]}")

# # Задание 7: Ввод числа больше 100
# print("\n=== Задание 7: Ввод числа больше 100 ===")
# while True:
#     number = int(input("Введите число больше 100: "))
#     if number > 100:
#         print(f"Спасибо! Вы ввели: {number}")
#         break
#     else:
#         print("Число должно быть больше 100. Попробуйте снова.")

# # Задание 8: Подсчет гласных букв
# print("\n=== Задание 8: Подсчет гласных букв ===")
# text = input("Введите строку для подсчета гласных: ").lower()
# vowels = "aeiou"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print(f"Количество гласных букв в строке: {count}")

# # Задание 9: Последовательность чисел
# print("\n=== Задание 9: Последовательность чисел ===")
# for i in range(1, 5):
#     square = i * i
#     print(f"{i} - {square}")


#Лабораторная 21
# import random
# import time

# # Задание 1: Счетчик
# print("=== Задание 1: Счетчик ===")
# def counter():
#     if not hasattr(counter, 'count'):
#         counter.count = 0
#     counter.count += 1
#     print(f"Текущее значение счетчика: {counter.count}")

# counter()
# counter()
# counter()

# # Задание 2: Максимальное число в массиве
# print("\n=== Задание 2: Максимальное число в массиве ===")
# def findMax(numbers):
#     if not numbers:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num

# numbers = [3, 7, 2, 9, 1, 5]
# print(f"Массив: {numbers}")
# print(f"Максимальное число: {findMax(numbers)}")

# # Задание 3: Таблица умножения с локальной функцией
# print("\n=== Задание 3: Таблица умножения ===")
# def printTable(number):
#     def printRow(multiplier):
#         result = number * multiplier
#         print(f"{number} × {multiplier} = {result}")
    
#     for i in range(1, 11):
#         printRow(i)

# printTable(5)

# # Задание 4: Валидация email
# print("\n=== Задание 4: Валидация email ===")
# def validateEmail(email):
#     at_index = email.find('@.')
#     if at_index == -1:
#         return False

    
#     return True

# emails = ["user@example.com", "invalid.email", "user@.com", "user@domain."]
# for email in emails:
#     print(f"{email}: {'валиден' if validateEmail(email) else 'невалиден'}")

# # Задание 5: Случайное число в диапазоне
# print("\n=== Задание 5: Случайное число в диапазоне ===")
# def randomInRange(min_val, max_val):
#     return random.randint(min_val, max_val)

# print(f"Случайное число от 1 до 10: {randomInRange(1, 10)}")
# print(f"Случайное число от 50 до 100: {randomInRange(50, 100)}")

# # Задание 6: Факториал
# print("\n=== Задание 6: Факториал ===")
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result

# for i in range(6):
#     print(f"Факториал {i} = {factorial(i)}")

# # Задание 7: Отложенное сообщение
# print("\n=== Задание 7: Отложенное сообщение ===")
# def delayedMessage(message, delay):
#     print(f"Сообщение будет показано через {delay} секунд...")
#     time.sleep(delay)
#     print(f"Сообщение: {message}")

# # Пример использования (закомментирован, чтобы не замедлять выполнение)
# # delayedMessage("Привет, мир!", 3)
# # Для теста используем меньшую задержку
# delayedMessage("Тестовое сообщение!", 1)


# Задание 1
# 1.1
# Необходимо добавить обработку исключения неверного типа данных, нельзя вводить строки, только целые числа.
# Исключение ValueError
# Кроме того, нельзя вводить какие либо числа кроме 2,3,4 и 5, здесь еужно создать пользовательское исключение.
        
# 1.2
# Создаем пользовательское исключение для обработки массы, превышающей критический порог, 
# кроме того, исключение нулевых и отрицательных значений и текстовых данных        

# 1.3
# Обрабатываем исключение нулевого значения, и создаем пользовательское исключение обработки суммы на вкладе, 
# для предотвращения возникновения суммы, меньшней неснимаемого остатка


# Задание 2
# Защита от пользовательских ошибок соответсвует в модели качества продукта пункту Удобство использования, 
# и подпункту "Защищенность от пользовательских ошибок".

# Задание 3
# Такое поведение делает вычисления с плавающей точкой более устойчивыми и соотвествующими 
# математическим ожиданиям непрерывных числовых систем, позволяет обрабатывать пределы и некоторые другие ситуации
# Деление на ноль имеет математический смысл в контексте пределов последовательностей.

# Задание 4
# A = []
# i = 1
# while i != 0:
#       i=i+1
#       A.append(i)
# print(A[0])


# # Задание 5

# import random
# def main():
#     # Строка 1: Ввод максимального количества элементов
#     max_length = int(input("Введите максимально возможное число элементов в списке: "))
#     #   может возникнуть ошибка ввода, из-за неправильного типа данных
    
#     # Строка 2: Генерация случайной длины списка
#     #если заданная длина будет меньше 2, то произойдет сбой, так как random не может создать число от 2 до 0 или -1
#     lst_length = random.randint(2, max_length)
    
#     # Строка 3: Создание пустого списка
#     lst = []
    
#     # Строка 4: Заполнение списка случайными числами
#     for i in range(lst_length):
#         lst.append(random.randint(-10, 11))
    
#     # Строка 5: Генерация случайного индекса для удаления
#     num = random.randint(2, max_length)
#     #Может возникнуть исключение выхода за индекс, так как заданное максимальное значение элементов 
#     # в списке не всегда будет равно фактическому
    
#     # Строка 6: Удаление элемента по индексу
#     lst.pop(num)
    
#     print(f"Из списка удален {num}-й элемент")
#     input()  # Ожидание нажатия клавиши

# #Не запуститься программа, name не определено, было name, я добавил __name__
# if __name__ == "__main__":
#     main()


# # Задание 6
# # Здесь нам необходимо создать пользовательское исключение, 
# # так как у нас есть конкретные уникальные условия, при которых должно обрабатываться исключение

# class InvalidPressureError(Exception):
#    pass

# def check_tire_pressure(pressure):

#     MINP = 2.0
#     MAXP = 3.0
    
#     if pressure < MINP:
#         raise InvalidPressureError(
#             pressure, 
#             f"⚠️ ОПАСНО: Слишком низкое давление"
#         )
#     elif pressure > MAXP:
#         raise InvalidPressureError(
#             pressure, 
#             f"⚠️ ОПАСНО: Слишком высокое давление (рекомендую уйти на все четыре стороны, как можно скорее)"
#         )
#     else:
#         print(f"✅ Давление в норме: {pressure} атм")



# #Задание 7
# class SizeError(Exception):
#     pass
# def main():
#     try:
#         # Ввод ширины участка
#         width = int(input("Введите ширину участка: "))
#         #Вводим проверку длины и ширины, если не подходит по условию, вызываем исключение
#         if width <= 0:
#             raise ValueError("Размер не может быть меньше или равен нулю!")
#         # Ввод длины участка
#         length = int(input("Введите длину участка: "))
#         if length <= 0:
#             raise ValueError("Размер не может быть меньше или равен нулю!")
#         #Вводим проверку, больше ли ширина длины, если да, вызываем исключение
#         if width > length:
#             raise SizeError("Размер не может быть меньше или равен нулю!")
        
#         # Вычисление и вывод площади
#         area = width * length
#         #Не вполне корректно брать отрицательную площадь за исключение, ведь конкретное значение, 
#         # длина иои ширина, являются отрицательными, в математическом аппарате, в механике и физике, 
#         # это играет важную роль, по мере рсота числа переменных и усложнению конструкций, необходимо знать какое именно значение ошибочно.
#         print(f"Площадь участка - {area}")
        
#     except ValueError as e:
#         # Обработка ошибки неверного формата данных
#         print("Ошибка: Неверный формат данных! Введите целое число.")
#     except SizeError as e:
#         # Обработка исключений размера
#         print(f"Ошибка размера: {e}")

# if __name__ == "__main__":
#     main()



# # Задание 3
# class InvalidPressureError(Exception):
#    pass
# def check_tire_pressure(pressure):
#     MINP = 2.0
#     MAXP = 3.0
#     if pressure < MINP:
#         raise InvalidPressureError(
#             pressure, 
#             f"⚠️ ОПАСНО: Слишком низкое давление"
#         )
#     elif pressure > MAXP:
#         raise InvalidPressureError(
#             pressure, 
#             f"⚠️ ОПАСНО: Слишком высокое давление (рекомендую уйти на все четыре стороны, как можно скорее)"
#         )
#     else:
#         print(f"✅ Давление в норме: {pressure} атм")
# try:
#         pres = input("Введите давление в шинах (атм): ")
#         Q = float(pres)
#         check_tire_pressure(Q)
# except InvalidPressureError as e:
#         print(e)
#         if "низкое" in str(e):
#             print("💡 Рекомендация: Подкачайте шины до 2.2-2.5 атм")
#         elif "высокое" in str(e):
#             print("💡 Рекомендация: Стравите воздух до 2.5-2.8 атм")
# except ValueError:
#         print("❌ Ошибка: Введите числовое значение (например: 2.5)")

# # Задание 2
# class WeakPasswordError(Exception):
#     pass
# def validate_password(password):
#     if len(password) < 8:
#         raise WeakPasswordError(len(password))
#     print("✅ Пароль принят! Соответствует минимальным требованиям безопасности(Я задаю требования ('_').")
# try:
#     password = input("Введите пароль (минимум 8 символов): ")

#     validate_password(password)
        
# except WeakPasswordError as e:
#         print(f"❌ Ошибка безопасности: {e}")
# except KeyboardInterrupt:
#         print("\n\nПрограмма прервана пользователем")

# # Задание 3
# class RatingError(Exception):
#     pass
# def watch_film(age, rating):
#     if age < rating:
#         print(f"Go touch grass kiddo! You are {age}, that's not enough")
#     if age >= rating:
#         print(f'Okie dokie, you are good to go, {age} is {age}')
# try:
#     age = int(input('Insert your age, please: '))
#     rating = int(input('Insert rating of the film, please: '))
#     watch_film(age, rating)
# except RatingError as LALALALALALA:
#     print(f'Your age is {age}, small kids do not watch this, {LALALALALALA}')
# except ValueError as LALALALALALA:
#     print(f'{LALALALALALA}')






# class Incorrect_Form(Exception):
#     pass
# def Harmony(aria, sonata):
#     if aria < 0 or sonata < 0:
#         raise Incorrect_Form(f"You little trash, {aria}!, you are kidding me, don't try to destroy it!.")
#     print(f'Все тип топ, просто иди дальше!')
#     logos = aria*sonata
#     return logos
# try:
#     aria = int(input(f"Введите длину: "))
#     sonata = int(input(f"Введите ширину: "))
#     Harmony(aria, sonata)
# except Incorrect_Form as e:
#     print(f'Ошибка: {e}')
# except ValueError:
#     print("Ошибка типа данных")



# class Incorrect_Temp(Exception):
#     pass
# def set_refrigerator(tempo):
#     if tempo < -10:
#         raise Incorrect_Temp(f"You little brat, {tempo}!, you are kidding me, don't try to destroy it!.")
#     if tempo > 10:
#         raise Incorrect_Temp(f"You little demon, {tempo}!, you are like a bad omen yo!.")
#     print(f'Все тип топ, просто дверь не держи!')
# try:
#     user_characteristics = int(input(f"Введите температуру: "))
#     set_refrigerator(user_characteristics)
# except Incorrect_Temp as e:
#     print(f'Ошибка: {e}')
# except ValueError:
#     print("Ошибка типа данных")
# try:
#     num = int(input("Введите число: "))
#     file = open("data.txt", "r")
#     data = file.read()
#     result = num + int(data)
#     print(f"Сумма: {result}")
# except (ValueError, TypeError) as e:
#     print(f"Ошибка преобразования данных: {e}")
# except (FileNotFoundError, PermissionError) as e:
#     print(f"Ошибка работы с файлом: {e}")
# except Exception as e:
#     print(f"Неизвестная ошибка: {e}")





# def data_circle():
#     try:
#         num = int(input("Введите число: "))
#         num1 = int(input("Введите число: "))
#         x = num/num1
#     except ValueError:
#         print("Ошибка: Введите целое число")
#         return None
#     except ZeroDivisionError:
#         print("Ошибка: Деление на 0")
#         return None
#     else:
#         print("Вычисления завершились успешно")
#         return x
#     finally:
#         print("Завершение экстраполяции данных...")
# x = data_circle()
# if x is not None:
#     print(f"Результат: {x}")
        
# def cel():
#     try:
#         num = int(input("Введите число в градусах Цельсия: "))
#         x = (num*(9/5)+32)
#     except ValueError:
#         print("Ошибка: Введите целое число")
#         return None
#     else:
#         print("Вычисления завершились успешно")
#         return x
#     finally:
#         print("Завершение экстраполяции данных...")
# x = cel()
# if x is not None:
#     print(f"Результат: {x}")

# class NegativeIMT(Exception):
#     pass
# def IMT():
#     try:
#         num = int(input("Введите вес: "))
#         num1 = int(input("Введите рост в метрах: "))
#         x = num/((num1/100)*(num1/100))
#         print(num1/100)
#     except ValueError:
#         print("Ошибка: Введите число")
#         return None
#     except ZeroDivisionError:
#         print("Ошибка: Деление на 0")
#         return None
#     except NegativeIMT:
#         print("Вес и рост не могут быть отрицательными")
#     else:
#         print("Вычисления завершились успешно")
#         return x
#     finally:
#         print("Завершение экстраполяции данных...")
# x = IMT()
# if x is not None:
#     print(f"Результат: {x}")
#     if x < 18.5:
#         print("Недостаточный вес")
#     if 18.5 < x < 24.9:
#         print("Нормальный вес")
#     if 25 < x < 29.9:
#         print("Избыточный вес")
#     if x > 29.9:
#         print("Ожирение")
        
# class Equation_Error(Exception):
#     pass

# def solve_quadratic():
#     try:
#         a = float(input("Введите a: "))
#         b = float(input("Введите b: "))
#         c = float(input("Введите c: "))

#         if a == 0:
#             if b == 0:
#                 if c == 0:
#                     print("Бесконечное количество решений")
#                     return None
#                 else:
#                     print("Нет решений")
#                     return None
#             else:
#                 x = -c / b
#                 print(f"Линейное уравнение: x = {x}")
#                 return [x]
#         d = b**2 - 4*a*c
#         print(f"Дискриминант: {d}")
#         if d < 0:
#             raise Equation_Error("Дискриминант отрицательный, действительных корней нет")
#         sqrt_d = d**0.5
#         x1 = (-b - sqrt_d) / (2*a)
#         x2 = (-b + sqrt_d) / (2*a)
        
#         if d == 0:
#             print(f"Один корень: x = {x1}")
#             return [x1]
#         else:
#             print(f"Два корня: x1 = {x1}, x2 = {x2}")
#             return [x1, x2]
#     except ValueError:
#         print("Ошибка: Введите число")
#         return None
#     except ZeroDivisionError:
#         print("Ошибка: Деление на 0")
#         return None
#     except Equation_Error as e:
#         print(f"Ошибка уравнения: {e}")
#         return None
#     except Exception as e:
#         print(f"Неизвестная ошибка: {e}")
#         return None
#     finally:
#         print("Завершение вычислений...")
# result = solve_quadratic()
# if result is not None:
#     print(f"Результат: {result}")



# class Equasion_Error(Exception):
#     pass
# def form():
#     try:
#         num = float(input("Введите a: "))
#         num1 = float(input("Введите b: "))
#         num2 = float(input("Введите c: "))
#         d = ((num1**2)-4*num*num2)
#         x = ((-1*num1)-(d**(0.5))/2*num)
#         x1 = ((-1*num1)+(d**(0.5))/2*num)
#         print(d)
#         print(x)
#         print(x1)
#         if d < 0:
#              Equasion_Error
#     except ValueError:
#         print("Ошибка: Введите число")
#         return None
#     except ZeroDivisionError:
#         print("Ошибка: Деление на 0")
#         return None
#     except Equasion_Error:
#         print("a не может быть отрицательным")
#     else:
#         print("Вычисления завершились успешно")
#         return x
#     finally:
#         print("Завершение экстраполяции данных...")
# x = form()

# if x is not None:
#     print(f"Результат: {x} и {x1}")



# try:
#     a = int(input())
#     x = input()
#     b = int(input())
#     if x == "+":
#         print(f"Сложение: {a+b}")
#     elif x == "-":
#         print(f"Вычитание: {a-b}")
#     elif x == "*":
#         print(f"Умножение: {a*b}")
#     elif x == "/":
#         print(f"Деление: {a/b}")
#     else:
#         print(f"Ошибка: {x} не является арифметической операцией")
# except ValueError:
#     print(f"Ошибка: Неправильный тип данных, должно быть число")
# except ZeroDivisionError:
#     print(f"Ошибка: Деление на ноль, одна из переменных равна 0")
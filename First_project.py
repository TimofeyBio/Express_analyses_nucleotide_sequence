from collections import Counter     # Модуль для подсчёта элементов

def nucleotide_counting(Seq):   # Функция подсчёФта нуклеотидов и длины последовательности
    return Counter(Seq), len(Seq)

Seq_DNA = str(input()).upper()  # Ввод последовательности и её исправление на заглавные буквы

if not Seq_DNA:     # Проверка на пустую строку
    print("ERROR - empty value")
else:
    invalid_nucleotides = []

    # Поиск некорректных символов и их позиции
    for position, nuc in enumerate(Seq_DNA, start=1):
        if nuc not in 'GCAT':
            invalid_nucleotides.append((nuc, position))

    # Вывод найденых некорректных символов и их позиций
    if invalid_nucleotides:
        for nuc, position in invalid_nucleotides:
            print(f'ERROR - unknown nucleotide "{nuc}" in position {position}')
    else:

        # Вызов функции подсчёта нуклеотидов и длины последовательности
        Value_Nucleotides, length_DNA = nucleotide_counting(Seq_DNA)
        
        # Вывод результатов
        print(f"Guanine - {Value_Nucleotides['G']}")
        print(f"Cytosine - {Value_Nucleotides['C']}")
        print(f"Adenine - {Value_Nucleotides['A']}")
        print(f"Thymine - {Value_Nucleotides['T']}")
        print(f"Total amount of nucleotides - {length_DNA}")
        print(f"GC percent = {round((Value_Nucleotides['G'] + Value_Nucleotides['C']) / length_DNA * 100, 2)}%")
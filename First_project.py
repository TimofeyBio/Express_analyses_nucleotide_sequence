from collections import Counter     # Модуль для подсчёта элементов

def nucleotide_counting(Seq):   # Функция подсчёФта нуклеотидов и длины последовательности
    return Counter(Seq), int(len(Seq))

file_name = input("Enter the path of the file: ")     # Ввод полного пути до читаемого файла

with open(file_name, "r") as Seq_DNA:    # Открытие файла
    New_seq_DNA = str('')
    s = [str(i) for i in Seq_DNA.readlines()]

    if s[0][0] != ">":
        print("ERROR - incorrect file format")  # Проверка файла на корректную первую строку
    else:

    # Проверка на наличие последовательности ДНК
        if not s[1]:
            print("ERROR - empty value")
        else:

        # Операция по созданию отдельной строки с последовательностью нуклеотидов
            New_seq_DNA = ''.join(s[1:]).upper().replace('\n', '')



            invalid_nucleotides = []

        # Поиск некорректных символов и их позиции
            for position, nuc in enumerate(New_seq_DNA, start=1):
                if nuc not in 'GCAT':
                    invalid_nucleotides.append((nuc, position))

        # Вывод найденых некорректных символов и их позиций
            if invalid_nucleotides:
                for nuc, position in invalid_nucleotides:
                    print(f'ERROR - unknown nucleotide "{nuc}" in position {position}')
            else:

            # Вызов функции подсчёта нуклеотидов и длины последовательности
                Value_Nucleotides, length_DNA = nucleotide_counting(New_seq_DNA)
        
            # Вывод результатов
                print(f"Guanine - {Value_Nucleotides['G']}")
                print(f"Cytosine - {Value_Nucleotides['C']}")
                print(f"Adenine - {Value_Nucleotides['A']}")
                print(f"Thymine - {Value_Nucleotides['T']}")
                print(f"Total amount of nucleotides - {length_DNA}")
                print(f"GC% - {round((Value_Nucleotides['G'] + Value_Nucleotides['C'])/length_DNA*100, 2)}%")
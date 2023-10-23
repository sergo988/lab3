# Задача 3
# Напишите функцию, которая возвращает уникальные элементы из каждой строки матрицы. Напишите такую же фукнкцию, но для столбцов
 
def unique_rows(matrix):
    result = []

    for row in matrix:
        unique = []

        for item in row:
            if item in unique: continue

            unique.append(item) 

        result.append(unique)

    return result

def unique_columns(matrix):
    result = []

    for i in range(len(matrix)):
        unique = []

        for j in range(len(matrix)):
            if matrix[j][i] in unique: continue

            unique.append(matrix[j][i])

        result.append(unique)

    return result

inputFile = open("input.txt", "r")

testCount = int(inputFile.readline())

inputFile.readline()
 
for i in range(testCount):
    print ("Тест {}:".format(i + 1))

    n = int(inputFile.readline())
    
    matrix = []
    
    for i in range(n):
        row = list(map(float, inputFile.readline().split(" ")))

        matrix.append(row)
        
    print("Исходные данные:")

    for row in matrix:
        for item in row:
            print("{}".format(item), end=" ")
        print()

    print("\nУникальные элементы строк:")
    for row in unique_rows(matrix):
        for item in row:
            print("{}".format(item), end=" ")
        print()

    print("\nУникальные элементы колонок:")
    for column in unique_columns(matrix):
        for item in column:
            print("{}".format(item), end=" ")
        print()

    print("--------------------------------------------------")

    inputFile.readline()

inputFile.close()
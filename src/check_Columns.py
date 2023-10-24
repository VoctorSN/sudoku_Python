def Check_Columns(sudoku):
    for column in range(len(sudoku)):
        numbers_in_column=[]
        for row in sudoku:
            if row[column] not in numbers_in_column:
                numbers_in_column.append(row[column])
            else:
                return False
    return True


if __name__ == "__main__" :
    # testing de Check_Columns

    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]
    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]

    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]

    incorrect2 = [[1,2,3,4],
                 [2,3,1,2],
                 [4,1,2,3],
                 [2,3,1,4]]

    print("Check_Columns")
    print(Check_Columns(incorrect2))
    print(Check_Columns(incorrect))
    print(Check_Columns(correct))
    print(Check_Columns(incorrect5))
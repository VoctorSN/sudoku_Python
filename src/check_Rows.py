def Check_Rows(sudoku):
    for row in sudoku:
        for num in row :
            if row.count(num) != 1:
                return False
            else :
                continue
    return True


if __name__ == "__main__":
    # testing de Check_Rows

    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]

    incorrect2 = [[1,2,3,4],
                 [2,3,1,2],
                 [4,1,2,3],
                 [2,3,1,4]]

    incorrect3 = [[1,2,3,4,5],
                 [2,3,1,5,6],
                 [4,5,2,1,3],
                 [3,4,5,2,1],
                 [5,6,4,3,2]]

    print("Check_Rows")
    print(Check_Rows(incorrect3))
    print(Check_Rows(incorrect2))
    print(Check_Rows(incorrect))
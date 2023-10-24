def Check_Square(sudoku,numbers_of_rows):
    for row in sudoku:
        if len(row) != numbers_of_rows:
            return False
    return True


if __name__ == "__main__":
    # testing de Check_Square

    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]
    irregular = [[1,2,3],
                 [2,3,1]]

    irregular2 = [[1,2,3],
                  [2,3,1],
                  [3,1]]
    
    print("Check_Square")
    print(Check_Square(correct,len(correct)))
    print(Check_Square(irregular,len(irregular)))
    print(Check_Square(irregular2,len(irregular2)))
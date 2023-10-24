def Check_Numbers_In_Range(sudoku,numbers_of_rows):
    for row in sudoku:
        for number in row :
            if isinstance(number,int) == False :
                return False
            elif number > numbers_of_rows :
                return False
    return True


if __name__ == "__main__" :
    # testing de Check_Numbers_In_Range
    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]

    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]

    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]


   
    print("Check_Numbers_In_Range")
    print(Check_Numbers_In_Range(correct,len(correct)))
    print(Check_Numbers_In_Range(incorrect4,len(incorrect4)))
    print(Check_Numbers_In_Range(incorrect5,len(incorrect5)))
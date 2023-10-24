import sys
sys.path.append('..')
# Nos situamos en la carpeta anterior para poder acceder a src

from src.check_Rows import Check_Rows
from src.check_Square import Check_Square
from src.check_Numbers_In_Range import Check_Numbers_In_Range
from src.check_Columns import Check_Columns



def Check_Sudoku(sudoku):
    numbers_of_rows=len(sudoku)
    assert isinstance(sudoku,list),  '''la interfaz se asegura de que el codigo que recibe sea una lista'''
    assert isinstance(Check_Square(sudoku,numbers_of_rows) and Check_Numbers_In_Range(sudoku,numbers_of_rows) and Check_Rows(sudoku) and Check_Columns(sudoku),bool)
    return Check_Square(sudoku,numbers_of_rows) and Check_Numbers_In_Range(sudoku,numbers_of_rows) and Check_Rows(sudoku) and Check_Columns(sudoku)

if __name__ == "__main__":
    import sys
    sys.path.append('..')
    import casos_Test.test_Sudoku as Test_Cases
    # testing de Check_Sudoku
    # La siguiente función separa las variables no  ocultas y imprime por pantalla el test que son y el valor que dan
    for attr in sorted(Test_Cases.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, " => ", Check_Sudoku(Test_Cases.__dict__[attr]))
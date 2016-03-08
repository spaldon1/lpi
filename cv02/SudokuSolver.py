import sys,os
sys.path[0:0] = [os.path.join(sys.path[0], '../examples/sat')]
import sat

class SudokuSolver:
    def solve(self,pole):
        def sudoku(x, y, n):
            return 9 * 9 * x + 9 * y + n

        def krok(x):
            return [x // 81, x % 81 // 9, x % 9]

        def ries(x,y,z):
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    for k in range(x, x + 3):
                        for l in range(y, y + 3):
                            if i != k or j != l:
                                subor.write('{} {} 0\n'.format(-(sudoku(i,j,z)), -(sudoku(k,l,z))))

        with open('vystup.txt', 'w') as subor:
            for i in range(9):
                for j in range(9):
                    if pole[i][j] != 0:
                        subor.write('{} 0\n'.format(sudoku(i, j, pole[i][j])))
                    else:
                        for n in range(1, 10):
                            subor.write('{} '.format(sudoku(i, j, n)))  
                        subor.write('0\n')

            for n in range(1, 10):
                for i in range(9):
                    for j in range(9):
                        for k in range(9):
                            if j != k:
                                subor.write('{} {} 0\n'.format(-(sudoku(i, j, n)), -(sudoku(i, k, n))))

                for i in range(9):
                    for j in range(9):
                        for k in range(9):
                            if j != k:
                                subor.write('{} {} 0\n'.format(-(sudoku(j, i, n)), -(sudoku(k, i, n))))

                for i in range(0, 7, 3):
                    for j in range(0, 7, 3):
                        ries(i, j, n)

        solver = sat.SatSolver()
        vysledok, riesenie = solver.solve("vystup.txt", "vystup-out.txt")

        if not vysledok:
            return [[0] * 9] * 9
        
        for x in riesenie:
            if x > 0:
                i, j, n = krok(x - 1)
                n += 1
                pole[i][j] = n

        return pole        

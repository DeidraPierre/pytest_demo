import unittest
import sys
sys.path.append("/home/codio/workspace/")
from boggle_solver import Boggle

class TestGetSolution(unittest.TestCase):
    """
    Test cases for getSolution function using Category Partition Method

    Categories:
    - grid: existence/type, dimensions, content, tile letters, word path
    - dictionary: Type, length, content, word length
    """
    def test_getSolution_1(self):
        #Grid is a list but not a 2D array"
        grid = ['A', 'B', 'C', 'D']
        dictionary = ['AB', 'ABC', 'ABCD']

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()

        solution = [x.upper() for x in solution]
        expected = []

        solution = sorted(solution)
        expected = sorted(expected)

        self.assertEqual(expected, solution)

    def test_getSolution_2(self):
      #Grid is not a list
      grid = 'ABCD'
      dictionary = ['AB', 'ABC', 'ABCD']

      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()

      solution = [x.upper() for x in solution]
      expected = []

      solution = sorted(solution)
      expected = sorted(expected)

      self.assertEqual(expected, solution)

    def test_getSolution_3(self):
      #Grid is empty
      grid = [[]]
      dictionary = ["CAT", "DOG", "BOGGLE"]

      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()

      solution = [x.upper() for x in solution]
      expected = []

      solution = sorted(solution)
      expected = sorted(expected)

      self.assertEqual(expected, solution)
    
    def test_getSolution_4(self):
      #Grid dimension is 1 x 1
      grid = [['A']]
      dictionary = ["A", "AAA", "CAT"]

      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()

      solution = [x.upper() for x in solution]
      expected = []

      solution = sorted(solution)
      expected = sorted(expected)

      self.assertEqual(expected, solution)
    
    def test_getSolution_5(self):
      #Grid dimension is 1 x N (single row)
      grid = [["C", "A", "T", "St"]]
      dictionary = ["CAT", "CATS", "TACS", "DOG", "AT"]

      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()

      solution = [x.upper() for x in solution]
      expected = ["CAT"]

      solution = sorted(solution)
      expected = sorted(expected)

      self.assertEqual(expected, solution)

    def test_getSolution_6(self):
      #Grid dimension is M x 1 (single column)
      grid = [
      ['C'],
      ['A'],
      ['T'],
      ['St']
      ]
      dictionary = ["CAT", "CATS", "TACS", "DOG", "AT"]

      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()

      solution = [x.upper() for x in solution]
      expected = ["CAT"]

      solution = sorted(solution)
      expected = sorted(expected)

      self.assertEqual(expected, solution)

    def test_getSolution_7(self):
      #Grid dimension is uneven (non-rectangular)
      grid = [
      ['A'],
      ['B', 'C'],
      ['D', 'E', 'F']
      ]
      dictionary = ["AB", "ABC", "DEF"]

      mygame = Boggle(grid, dictionary)
      solution = mygame.getSolution()

      solution = [x.upper() for x in solution]
      expected = []

      solution = sorted(solution)
      expected = sorted(expected)

      self.assertEqual(expected, solution)

    def test_getSolution_8(self):
        #Grid contains non strings
        grid = [["A", 123], ["C", "D"]]
        dictionary = ["ACD", "CAD"]
       
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
       
        solution = [x.upper() for x in solution]
        expected = []
       
        solution = sorted(solution)
        expected = sorted(expected)
       
        self.assertEqual(expected, solution)

    def test_getSolution_9(self):
        #Dictionary word ends in Q
        grid = [
        ["A", "B"],
        ["C", "Qu"]
        ]
        dictionary = ["ABC", "ABQ", "ACQ"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["ABC"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution_10(self):
        #Dictionary word ends in S
        grid = [
        ["A", "B"],
        ["C", "St"]
        ]
        dictionary = ["ABC", "ABS", "ACS", "STAB"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["ABC", "STAB"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution_11(self):
        #Dictrionary word ends in I
        grid = [
        ["A", "B"],
        ["C", "Ie"]
        ]
        dictionary = ["ABC", "ABI", "ACI"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["ABC"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution_12(self):
        #Q paired with non-u character
        grid = [["QA", "B"], ["C", "D"]]
        dictionary = ["QAB", "QABCD", "CAT"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = []
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution_13(self):
        #S paired with non-T character
        grid = [["SA", "B"], ["C", "D"]]
        dictionary = ["SAB", "SABCD", "CAT"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = []
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)
    
    def test_getSolution_14(self):
        #I paired with non-E character
        grid = [["IA", "B"], ["C", "D"]]
        dictionary = ["IAB", "IABCD", "CAT"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = []
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution_15(self):
        #Non-Adjacent Tiles
        grid = [
            ["C", "A", "T"],
            ["D", "E", "F"],
            ["X", "Y", "Z"]
        ]
        dictionary = ["CZT", "CTX", "CAT", "DEF"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT", "DEF"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution16(self):
        #Dictionary is not a list
        grid = [
            ["C", "A", "T"],
            ["D", "O", "G"],
            ["B", "I", "T"]
        ]
        dictionary = 12345
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = []
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)  
    
    def test_getSolution17(self):
        #Dictionary empty
        grid = [
            ["C", "A", "T"],
            ["D", "O", "G"],
            ["B", "I", "T"]
        ]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = []
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)     

    def test_getSolution18(self):
        #Dictionary length = 1
        grid = grid = [
            ["C", "A", "T"],
            ["D", "O", "G"],
            ["B", "Ie", "T"]
        ]
        dictionary = ['CAT']
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)    
    
    def test_getSolution19(self):
        #Dictionary contains non-strings
        grid = [
            ["C", "A", "T"],
            ["D", "O", "G"],
            ["B", "I", "T"]
        ]
        dictionary = ["CAT", 123, "DOG"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = []
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)    

    def test_getSolution20(self):
        #MxN rectangular grid with valid strings, duplicate letters, horizontal word path, and a list dictionary (>1) containing words <3 characters.
        grid = [
            ["C", "A", "T"],
            ["C", "A", "N"]
        ]
        dictionary = ["CAT", "CAN", "AT", "AN", "C"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT", "CAN"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)    
    
    def test_getSolution21(self):
       #MxN rectangular grid with valid strings, duplicate letters, horizontal word path, and a list dictionary (>1 words) containing 3-character strings.
        grid = [
            ["C", "A", "T"],
            ["B", "A", "T"]
        ]
        dictionary = ["CAT", "BAT", "TAB", "RAT"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT", "BAT", "TAB"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)   

    def test_getSolution22(self):
        #Rectangular MxN grid with valid strings, duplicate letters, vertical word path, and a list dictionary (>1) containing 3-character strings.
        grid = [
            ["C", "B"],
            ["A", "A"],
            ["T", "T"]
        ]
        dictionary = ["CAT", "TAC", "BAT", "TAB", "RAT"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT", "TAC", "BAT", "TAB"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution23(self):
        #Rectangular MxN grid with valid strings, unique letters, horizontal word path, and a list dictionary (>1) containing words longer than 3 characters.
        grid = [
            ["C", "A", "R", "D"],
            ["B", "E", "St", "T"]
        ]
        dictionary = ["CARD", "DRAC", "BEST", "TSEB", "CART", "BIRD"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CARD", "DRAC", "BEST", "CART"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution24(self):
        #Rectangular MxN grid with valid strings, unique letters, vertical word path, and a list dictionary (>1) containing 3-character words.
        grid = [
            ["C", "D"],
            ["A", "O"],
            ["T", "G"]
        ]
        dictionary = ["CAT", "TAC", "DOG", "GOD", "RAT"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT", "TAC", "DOG", "GOD"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution25(self):
        #Rectangular MxN grid with valid strings, unique letters, diagonal word path, and a list dictionary (>1) containing 3-character words.
        grid = [
            ["C", "X", "D"],
            ["Y", "A", "Z"],
            ["G", "W", "T"]
        ]
        dictionary = ["CAT", "TAC", "DAG", "GAD", "RAT"]
        
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT", "TAC", "DAG", "GAD"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution26(self):
    # Grid size 4 x 4
        grid = [
            ["Qu", "A", "R", "T"],
            ["St", "O", "R", "M"],
            ["Ie", "C", "E", "D"],
            ["F",  "L", "A", "T"]
        ]
        dictionary = ["QUART", "STORM", "ICED", "FLAT", "SNOW"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["FLAT", "QUART", "STORM"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution27(self):
    #Grid size 8 x8
        grid = [
            ["Qu", "A", "D", "E", "F", "G", "H", "A"],
            ["St", "A", "R", "T", "U", "V", "W", "X"],
            ["Ie", "N", "D", "E", "X", "Y", "Z", "A"],
            ["B",  "C", "D", "E", "F", "G", "H", "Ie"],
            ["J",  "K", "L", "M", "N", "O", "P", "St"],
            ["Qu", "R", "St","T", "U", "V", "W", "Qu"],  
            ["A",  "B", "C", "D", "E", "F", "G", "H"],
            ["Ie", "J", "K", "L", "M", "N", "O", "P"]
        ]
        dictionary = ["QUAD", "START", "INDEX", "NOTHERE"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["QUAD", "START"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)

    def test_getSolution28(self):
        #16 x 16 grid
        grid = [
            ["Qu", "A",  "R",  "T",  "E",  "R",  "L",  "Y",  "B",  "O",  "U",  "N",  "D",  "St",  "E",  "T"],
            ["St", "A",  "R",  "L",  "Ie",  "G",  "H",  "T",  "C",  "A",  "N",  "D",  "L",  "E",  "St",  "W"],
            ["Ie", "N",  "St",  "Ie",  "D",  "E",  "R",  "St",  "F",  "L",  "O",  "W",  "E",  "R",  "St",  "P"],
            ["F",  "L",  "A",  "T",  "L",  "A",  "N",  "D",  "G",  "A",  "R",  "D",  "E",  "N",  "St",  "O"],
            ["C",  "A",  "T",  "St",  "D",  "O",  "G",  "St",  "B",  "Ie",  "R",  "D",  "St",  "F",  "L",  "Y"],
            ["M",  "O",  "U",  "N",  "T",  "A",  "Ie",  "N",  "R",  "Ie",  "V",  "E",  "R",  "St",  "E",  "A"],
            ["W",  "Ie",  "N",  "T",  "E",  "R",  "St",  "U",  "M",  "M",  "E",  "R",  "F",  "A",  "L",  "L"],
            ["St",  "P",  "R",  "Ie",  "N",  "G",  "T",  "Ie",  "M",  "E",  "F",  "O",  "R",  "E",  "St",  "T"],
            ["A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "Ie",  "J",  "K",  "L",  "M",  "N",  "O",  "P"],
            ["Qu",  "R",  "St",  "T",  "U",  "V",  "W",  "X",  "Y",  "Z",  "A",  "B",  "C",  "D",  "E",  "F"],
            ["G",  "H",  "Ie",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Qu",  "R",  "St",  "T",  "U",  "V"],
            ["W",  "X",  "Y",  "Z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H",  "Ie",  "J",  "K",  "L"],
            ["M",  "N",  "O",  "P",  "Qu",  "R",  "St",  "T",  "U",  "V",  "W",  "X",  "Y",  "Z",  "A",  "B"],
            ["C",  "D",  "E",  "F",  "G",  "H",  "Ie",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Qu",  "R"],
            ["St",  "T",  "U",  "V",  "W",  "X",  "Y",  "Z",  "A",  "B",  "C",  "D",  "E",  "F",  "G",  "H"],
            ["Ie",  "J",  "K",  "L",  "M",  "N",  "O",  "P",  "Qu",  "R",  "St",  "T",  "U",  "V",  "W",  "X"]
        ]
        dictionary = ["QUART", "STAR", "FLAT", "CATS","CAT", "DOGS","DOG", "NOTHERE"]

        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        
        solution = [x.upper() for x in solution]
        expected = ["CAT", "DOG", "FLAT", "QUART", "STAR"]
        
        solution = sorted(solution)
        expected = sorted(expected)
        
        self.assertEqual(expected, solution)    

if __name__ == '__main__':
    unittest.main()()
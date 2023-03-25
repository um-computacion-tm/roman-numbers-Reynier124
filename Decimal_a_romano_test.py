import unittest
def decimal_to_roman(decimal):
    if decimal <= 3:
        return "I" * decimal
    elif decimal == 4:
        return "IV"
    elif decimal == 5:
        return "V"
    elif decimal == 6:
        return "VI"
    elif decimal == 7:
        return "VII"
    elif decimal == 8:
        return "VIII"
    elif decimal == 9:
        return "IX"
    else:
        return "X"
def roman_to_decimal(roman):
    if roman == "I":
        return 1
    elif roman == "II":
        return 2
    elif roman == "III":
        return 3
    elif roman == "IV":
        return 4
    elif roman == "V":
        return 5
    elif roman == "VI":
        return 6
    elif roman == "VII":
        return 7
    elif roman == "VIII":
        return 8
    elif roman == "IX":
        return 9
    else:
        return 10
        

class TestDecimanalToRoman(unittest.TestCase):
    def test_1(self):
        #proceso
        resultado = decimal_to_roman(1)
        #verificación
        self.assertEqual(resultado, "I")
    def test_2(self):
        #proceso
        resultado = decimal_to_roman(2)
        #verificación
        self.assertEqual(resultado, "II")
    def test_3(self):
        #proceso
        resultado = decimal_to_roman(3)
        #verificación
        self.assertEqual(resultado, "III")
    def test_4(self):
        #proceso
        resultado = decimal_to_roman(4)
        #verificación
        self.assertEqual(resultado, "IV")
    def test_5(self):
        #proceso
        resultado = decimal_to_roman(5)
        #verificación
        self.assertEqual(resultado, "V")
    def test_6(self):
        #proceso
        resultado = decimal_to_roman(6)
        #verificación
        self.assertEqual(resultado, "VI")
    def test_7(self):
        #proceso
        resultado = decimal_to_roman(7)
        #verificación
        self.assertEqual(resultado, "VII")
    def test_8(self):
        #proceso
        resultado = decimal_to_roman(8)
        #verificación
        self.assertEqual(resultado, "VIII")
    def test_9(self):
        #proceso
        resultado = decimal_to_roman(9)
        #verificación
        self.assertEqual(resultado, "IX")
    def test_10(self):
        #proceso
        resultado = decimal_to_roman(10)
        #verificación
        self.assertEqual(resultado, "X")
class TestRomantodecimal(unittest.TestCase):
    def test_1(self):
        resultado = roman_to_decimal("I")
        self.assertEqual(resultado, 1)
    def test_2(self):
        resultado = roman_to_decimal("II")
        self.assertEqual(resultado, 2)
    def test_3(self):
        resultado = roman_to_decimal("III")
        self.assertEqual(resultado, 3)
    def test_4(self):
        resultado = roman_to_decimal("IV")
        self.assertEqual(resultado, 4)
    def test_5(self):
        resultado = roman_to_decimal("V")
        self.assertEqual(resultado, 5)
    def test_6(self):
        resultado = roman_to_decimal("VI")
        self.assertEqual(resultado, 6)
    def test_7(self):
        resultado = roman_to_decimal("VII")
        self.assertEqual(resultado, 7)
    def test_8(self):
        resultado = roman_to_decimal("VIII")
        self.assertEqual(resultado, 8)
    def test_9(self):
        resultado = roman_to_decimal("IX")
        self.assertEqual(resultado, 9)
    def test_10(self):
        resultado = roman_to_decimal("X")
        self.assertEqual(resultado, 10)
    
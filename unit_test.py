import unittest
from check_password import is_valid_password

# Класс, в котором реализованы Unit-тесты, наследуемый от класса "unittest.TestCase"
class TestPasswordRegex(unittest.TestCase):

    # Unit-тест для пароля, проходящего по всем критериям
    def test_valid(self):
        self.assertTrue(is_valid_password("NormPass321$"))

    # Unit-тест для пароля, в котором не хватает заглавной буквы
    def test_no_uppercase(self):
        self.assertFalse(is_valid_password("badpassword5729*"))

    # Unit-тест для пароля, в котором не хватает строчных букв
    def test_no_lowercase(self):
        self.assertFalse(is_valid_password("BIGPASSWORD*7843"))

    # Unit-тест для пароля, в котором не хватает строчных цифр
    def test_no_digit(self):
        self.assertFalse(is_valid_password("NoDigitsPassword$"))

    # Unit-тест для пароля, в котором не хватает специальных символов
    def test_no_special(self):
        self.assertFalse(is_valid_password("CommonPassword#"))

    # Unit-тест для пароля, длина которого < 12
    def test_short(self):
        self.assertFalse(is_valid_password("tooShort2&"))

    # Unit-тест для пароля, в котором присутствуют пробелы
    def test_with_space(self):
        self.assertFalse(is_valid_password("Hello world!341"))

# Запуск всех тестов
if __name__ == "__main__":
    unittest.main()
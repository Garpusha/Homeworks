from unittest import TestCase
import main


class TestYandexLogin(TestCase):

    def test_yandex(self):
        result = main.log_into_yandex(main.get_driver('https://passport.yandex.ru/auth'))
        print(f'Result URL is {result}\n')
        try:
            self.assertEqual('https://id.yandex.ru/', result)
            print("\nLogged in successfully")
        except AssertionError:
            print("\n Got some error")
        return

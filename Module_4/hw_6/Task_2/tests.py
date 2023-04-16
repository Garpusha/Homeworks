from unittest import TestCase
import configparser
import main
import requests



class TestYandex(TestCase):

    def test_yandex(self, yandex_, dir_name):
        result = yandex_.make_dir(dir_name)
        self.assertEqual(201, result, 'Error')
        return


mytest = TestYandex()
token = main.read_config('tokens.ini', 'Tokens', 'YandexToken')
my_yandex = main.YandexDisk(token)
mytest.test_yandex(my_yandex, 'TestDir')

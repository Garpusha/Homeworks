from unittest import TestCase
import main


class TestYandex(TestCase):

    def test_yandex(self):
        token = main.read_config('tokens.ini', 'Tokens', 'YandexToken')
        my_yandex = main.YandexDisk(token)
        dir_name = 'TestDir'
        result = my_yandex.make_dir(dir_name)
        try:
            self.assertEqual(201, result)
            print("\nFolder was created successfully")
        except AssertionError:
            match result:
                case 409:
                    print("\nError. Folder already exists")
                case 401:
                    print("\nError. You're not authorized to proceed")
                case 404:
                    print('\nError. Resource not found')
                case 429:
                    print('\nError. Too many requests')
                case 503:
                    print('\nError. Service is not available')
                case 507:
                    print('\nError. Not enough space')
                case _:
                    print("\n Unknown error")
        return

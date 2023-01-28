import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

        # проверяю наличие каталога Test_Folder, если его нет, создаю
        params = {'path': 'disk:/Test_Folder'}
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 404:
            params = {'path': 'disk:/Test_Folder'}
            requests.put(url, headers=headers, params=params)

        # получаю ссылку для загрузки файла
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': 'disk:/Test_Folder/testfile.txt', 'overwrite': 'true'}
        res = requests.get(url=url, headers=headers, params=params)
        my_href = res.json()['href']

        # загружаю файл
        with open(file_path, 'rb') as my_file:
            data = my_file.read()

        res = requests.put(my_href, data=data)
        return res.status_code


        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'http_Task_2\\testfile.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    if result == 201:
        print(f'Файл {path_to_file} успешно загружен.')
    else:
        print(f'Хьюстон, у нас проблемы. Код {result}')
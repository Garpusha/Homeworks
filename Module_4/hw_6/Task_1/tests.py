import pytest
from functions import task_1, task_2, task_3


class TestMe:
    @pytest.mark.parametrize(
        "data, expected",
        [
            (
                [
                    {"visit1": ["Москва", "Россия"]},
                    {"visit2": ["Дели", "Индия"]},
                    {"visit3": ["Владимир", "Россия"]},
                    {"visit4": ["Лиссабон", "Португалия"]},
                    {"visit5": ["Париж", "Франция"]},
                    {"visit6": ["Лиссабон", "Португалия"]},
                    {"visit7": ["Тула", "Россия"]},
                    {"visit8": ["Тула", "Россия"]},
                    {"visit9": ["Курск", "Россия"]},
                    {"visit10": ["Архангельск", "Россия"]},
                ],
                6,
            )
        ],
    )
    def test_task_1(self, data, expected):
        result = task_1(data)
        assert result == expected

    @pytest.mark.parametrize(
        "data, expected",
        [
            (
                {
                    "user1": [213, 213, 213, 15, 213],
                    "user2": [54, 54, 119, 119, 119],
                    "user3": [213, 98, 98, 35],
                },
                {98, 35, 15, 213, 54, 119},
            )
        ],
    )
    def test_task_2(self, data, expected):
        result = task_2(data)
        assert result == expected

    @pytest.mark.parametrize(
        "data, expected",
        [
            (
                [
                    "смотреть сериалы онлайн",
                    "новости спорта",
                    "афиша кино",
                    "курс доллара",
                    "сериалы этим летом",
                    "курс по питону",
                    "сериалы про спорт",
                ],
                {2: 42.86, 3: 57.14},
            )
        ],
    )
    def test_task_3(self, data, expected):
        result = task_3(data)
        assert result == expected

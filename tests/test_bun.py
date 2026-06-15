import allure
from praktikum.bun import Bun


class TestBun:

    @allure.title("Проверка что булочке можно дать название")
    def test_get_bun_name(self):
        bun = Bun("Земная булочка", 1000)

        assert bun.get_name() == "Земная булочка"

    @allure.title("Проверка что булочке можно назначить цену")
    def test_get_bun_price(self):
        bun = Bun("Лунная булочка", 2000)

        assert bun.get_price() == 2000
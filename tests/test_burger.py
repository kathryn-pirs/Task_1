import allure
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import Mock


class TestBurger:

    @allure.title("Проверка что булочке устанавливается правильное название и цена")
    def test_set_bun_return_correct_name_and_price(self):

        bun = Bun("Земная булочка", 1000)
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun == bun
        assert burger.bun.get_name() == "Земная булочка"
        assert burger.bun.get_price() == 1000

    @allure.title("Проверка добавления ингридиентов")
    def test_add_ingredient(self):
        burger = Burger()
        ingr = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        burger.add_ingredient(ingr)

        assert burger.ingredients[0] == ingr

    @allure.title("Проверка Удаления ингридиентов")
    def test_remove_ingredient(self):
        burger = Burger()
        ingr1 = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)
        ingr2 = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
        burger.add_ingredient(ingr1)
        burger.add_ingredient(ingr2)
        burger.remove_ingredient(1)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingr1

    @allure.title("Проверка изменения порядка ингридиентов ингридиентов")
    def test_move_ingredient(self):

        burger = Burger()
        ingrs = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                 Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                 Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                 Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                 Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                 Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)]

        for ingr in ingrs:
            burger.add_ingredient(ingr)

        burger.move_ingredient(3, 1)
        burger.move_ingredient(4, 3)

        expected = [ingrs[0], ingrs[3], ingrs[1], ingrs[4], ingrs[2], ingrs[5]]

        assert burger.ingredients == expected

    @allure.title("Проверка расчёта общей стоимости")
    def test_get_total_price_calculates(self):

        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = 1000

        prices = [100, 200, 300, 100, 200, 300]
        mocks = []

        for price in prices:
            mock_ingr = Mock()
            mock_ingr.get_price.return_value = price
            burger.add_ingredient(mock_ingr)
            mocks.append(mock_ingr)

        burger.set_buns(mock_bun)
        total = burger.get_price()

        assert mock_bun.get_price.call_count == 1
        for mock in mocks:
            mock.get_price.assert_called_once()

        assert total == 3200

    @allure.title("Проверка чека")
    def test_get_correct_receipt(self):

        burger = Burger()
        bun = Bun("Земная булочка", 1000)
        sauce = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                 Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                 Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)]

        filling = [Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                   Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                   Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)]

        burger.set_buns(bun)

        for ingr in sauce + filling:
            burger.add_ingredient(ingr)

        receipt = burger.get_receipt()

        expected_receipt = [
            "(==== Земная булочка ====)",
            "= sauce hot sauce =",
            "= sauce sour cream =",
            "= sauce chili sauce =",
            "= filling cutlet =",
            "= filling dinosaur =",
            "= filling sausage =",
            "(==== Земная булочка ====)",
            "",
            "Price: 3200"
        ]
        assert receipt == '\n'.join(expected_receipt)
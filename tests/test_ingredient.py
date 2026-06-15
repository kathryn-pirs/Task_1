import allure
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @allure.title("Проверка заданного типа ингридиента")
    def test_ingredient_get_type(self):
        ingr = Ingredient(INGREDIENT_TYPE_SAUCE, "Земная булочка", 1000)

        assert ingr.get_type() == INGREDIENT_TYPE_SAUCE

    @allure.title("Проверка заданного имени ингридиента")
    def test_ingredient_get_name(self):
        ingr = Ingredient(INGREDIENT_TYPE_FILLING, "Лунная булочка", 2000)

        assert ingr.get_name() == "Лунная булочка"

    @allure.title("Проверка заданной цены ингридиента")
    def test_ingredient_get_price(self):
        ingr = Ingredient(INGREDIENT_TYPE_FILLING, "Марсианская булочка", 3000)

        assert ingr.get_price() == 3000
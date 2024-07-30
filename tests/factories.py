# tests/factories.py

import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category

class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = factory.Faker('word')
    description = factory.Faker('sentence')
    price = FuzzyDecimal(0.01, 100.00)
    available = FuzzyChoice([True, False])
    category = FuzzyChoice([Category.CLOTHS, Category.ELECTRONICS, Category.FOOD, Category.TOYS])

# features/steps/load_steps.py

from behave import given
from service.models import db, Product

@given('the following products')
def step_impl(context):
    """ Load products from a table """
    db.session.query(Product).delete()
    db.session.commit()
    for row in context.table:
        product = Product(name=row['name'], description=row['description'], price=row['price'], available=row['available'] == 'True', category=row['category'])
        product.create()

#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

    print("Deleting data...")
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    print("Creating restaurants...")
    shack = Restaurant(name="Karen's Pizza Shack", address='address1')
    bistro = Restaurant(name="Sanjay's Pizza", address='address2')
    palace = Restaurant(name="Kiki's Pizza", address='address3')

    print("Creating pizzas...")
    cheese = Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")

    db.session.add_all([shack, bistro, palace, cheese, pepperoni, california])
    db.session.commit()

    print("Creating RestaurantPizza...")

    pr1 = RestaurantPizza(restaurant_id=shack.id, pizza_id=cheese.id, price=1)
    pr2 = RestaurantPizza(restaurant_id=bistro.id, pizza_id=pepperoni.id, price=4)
    pr3 = RestaurantPizza(restaurant_id=palace.id, pizza_id=california.id, price=5)

    db.session.add_all([pr1, pr2, pr3])
    db.session.commit()

    print("✅ Seeding done!")

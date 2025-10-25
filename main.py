main.py

from product import Product
from product_manager import ProductManager

# Kreiranje instance ProductManager
manager = ProductManager()

# Dodavanje proizvoljnih proizvoda
p1 = Product("Laptop", 1200.00, 5)
p2 = Product("Miš", 15.50, 50)
p3 = Product("Tastatura", 45.99, 20)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Ažuriranje količine jednog proizvoda
p1.update_quantity(3)

# Prikaz proizvoda
manager.display_all_products()

# Prikaz ukupne vrednosti inventara
total_value = manager.get_total_inventory_value()
print(f"\nUkupna vrednost inventara: {total_value:.2f} KM")

from cart import Cart # Dodajte na početak main.py

# --- TESTIRANJE KLASNE CART ---

# Kreiranje instance Cart
customer_cart = Cart()

# Dodavanje proizvoda u korpu (koristimo postojeće objekte p1, p2, p3)
customer_cart.add_product_to_cart(p1, 1) # Laptop
customer_cart.add_product_to_cart(p2, 2) # Miš
customer_cart.add_product_to_cart(p3, 1) # Tastatura
customer_cart.add_product_to_cart(p2, 3) # Dodavanje još Miša

# Prikaz sadržaja korpe i ukupne vrednosti
customer_cart.display_cart_contents()
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
product_manager.py

from product import Product

class ProductManager:
    """
    Klasa koja upravlja kolekcijom proizvoda (inventarom).
    """
    def __init__(self):
        # Lista svih dostupnih proizvoda
        self.products = []

    def add_product(self, product):
        """Dodaje novi proizvod u inventar."""
        if isinstance(product, Product):
            self.products.append(product)
            print(f"Proizvod '{product.name}' dodan u inventar.")
        else:
            print("Greška: Dodat mora biti instanca klase Product.")

    def display_all_products(self):
        """Prikazuje informacije o svim proizvodima u inventaru."""
        print("\n--- INVENTAR PROIZVODA ---")
        if not self.products:
            print("Inventar je prazan.")
            return

        for product in self.products:
            print(product.display_info())
        print("--------------------------")

    def get_total_inventory_value(self):
        """Izračunava ukupnu vrednost svih proizvoda (cena * količina)."""
        total_value = sum(p.price * p.quantity for p in self.products)
        return total_value
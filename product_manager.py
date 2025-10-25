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
    
class ProductManager:
    # ... (postojeći kod __init__, add_product, display_all_products, get_total_inventory_value)

    def remove_product_by_name(self, product_name):
        """Uklanja proizvod iz inventara prema imenu."""
        initial_count = len(self.products)
        # Kreiramo novu listu proizvoda, isključujući onaj koji želimo da uklonimo
        self.products = [p for p in self.products if p.name != product_name]

        if len(self.products) < initial_count:
            print(f"Proizvod '{product_name}' je uspešno uklonjen iz inventara.")
        else:
            print(f"Greška: Proizvod '{product_name}' nije pronađen u inventaru.")
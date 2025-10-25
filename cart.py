cart.py

from product import Product

class Cart:
    """
    Klasa koja predstavlja korpu kupca.
    """
    def __init__(self):
        # Lista stavki u korpi, gde je svaka stavka tuple (Product, quantity_in_cart)
        self.cart_items = []

    def add_product_to_cart(self, product, quantity):
        """Dodaje proizvod u korpu."""
        if not isinstance(product, Product):
            print("Greška: Možete dodati samo instancu klase Product.")
            return

        if quantity <= 0:
            print("Greška: Količina mora biti veća od nule.")
            return

        # Provera da li je proizvod već u korpi
        for i, (item_product, item_quantity) in enumerate(self.cart_items):
            if item_product.name == product.name:
                # Ažuriranje količine ako proizvod već postoji
                self.cart_items[i] = (item_product, item_quantity + quantity)
                print(f"Količina za '{product.name}' u korpi je ažurirana na {item_quantity + quantity}.")
                return

        # Dodavanje novog proizvoda
        self.cart_items.append((product, quantity))
        print(f"Proizvod '{product.name}' (x{quantity}) dodan u korpu.")

    def calculate_total_value(self):
        """Izračunava ukupnu vrednost korpe."""
        total = sum(item_product.price * item_quantity for item_product, item_quantity in self.cart_items)
        return total

    def display_cart_contents(self):
        """Prikazuje sadržaj korpe."""
        print("\n--- SADRŽAJ KORPE ---")
        if not self.cart_items:
            print("Korpa je prazna.")
            return

        for product, quantity in self.cart_items:
            line_total = product.price * quantity
            print(f"- {product.name} (Cena: {product.price:.2f} KM) x {quantity} = {line_total:.2f} KM")

        total = self.calculate_total_value()
        print(f"--------------------------")
        print(f"Ukupno za naplatu: {total:.2f} KM")
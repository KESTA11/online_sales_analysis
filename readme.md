# ONLINE SALES ANALYSIS

Ovaj projekat predstavlja jednostavan sistem za upravljanje inventarom proizvoda i simulaciju korpe za kupovinu, implementiran korišćenjem objektno-orijentisanog programiranja u Pythonu. Projekat služi za demonstraciju osnovnih Python funkcionalnosti i vežbu Git i GitHub operacija (grane, spajanje, .gitignore).

## Struktura klasa

### 1. `Product` (product.py)
* **Atributi:** `name`, `price`, `quantity`.
* **Funkcionalnosti:** Prikaz informacija o proizvodu, ažuriranje količine.

### 2. `ProductManager` (product_manager.py)
* **Atributi:** Lista svih dostupnih proizvoda.
* **Funkcionalnosti:** Dodavanje proizvoda, prikaz svih proizvoda, prikaz ukupne vrednosti inventara, **uklanjanje proizvoda po imenu**.

### 3. `Cart` (cart.py)
* **Atributi:** `cart_items` (lista proizvoda i njihovih količina u korpi).
* **Funkcionalnosti:** Dodavanje proizvoda u korpu, računanje ukupne vrednosti za naplatu, prikaz sadržaja korpe.

## Faze razvoja (Git istorija)

1.  Inicijalna implementacija `Product` i `ProductManager`.
2.  Dodavanje funkcionalnosti za uklanjanje proizvoda (grana `add-product-removal`).
3.  Implementacija klase `Cart` (grana `add-cart-functionality`).
4.  Konfigurisanje `.gitignore` datoteke.
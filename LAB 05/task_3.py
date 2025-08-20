import random

# Sample product database
product_db = {
    "soap": ["Dettol Soap", "Dove Soap", "Lux Soap", "Pears Soap"],
    "mobile": ["iPhone 14", "Samsung Galaxy S23", "OnePlus 11", "Google Pixel 7"],
    "toys": ["Lego Set", "Barbie Doll", "Hot Wheels Car", "Rubik's Cube"],
    "games": ["Monopoly", "Chess", "Scrabble", "Uno"],
}

# Search history
search_history = []

def recommend_products(search_term):
    # Recommend products based on search term or history
    if search_term in product_db:
        products = product_db[search_term]
        print(f"Recommended products for '{search_term}':")
        for product in products:
            print("-", product)
    else:
        # If not found, recommend based on history
        if search_history:
            last_search = search_history[-1]
            products = product_db.get(last_search, [])
            if products:
                print(f"No direct matches. Based on your last search '{last_search}', you might like:")
                for product in products:
                    print("-", product)
            else:
                print("No recommendations available.")
        else:
            print("No recommendations available.")

def main():
    print("Product Recommendation System")
    print("Type 'exit' to quit.")
    while True:
        search_term = input("Search for a product: ").strip().lower()
        if search_term == "exit":
            break
        search_history.append(search_term)
        recommend_products(search_term)

if __name__ == "__main__":
    main()
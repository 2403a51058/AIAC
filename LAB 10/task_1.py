def _get_discount_rate(price, category):
    rules = {
        "student": lambda p: 0.1 if p > 1000 else 0.05,
        "regular": lambda p: 0.15 if p > 2000 else 0.0,
    }
    rate_fn = rules.get(category, rules["regular"])  # default to regular rules
    return rate_fn(price)

def discount(price, category):
    rate = _get_discount_rate(price, category)
    return price * (1 - rate)

if __name__ == "__main__":
    a = discount(1000, "student")
    print(a)
def recommend_products(products, user):
    scored = []

    for product in products:
        score = 0

        if product["price"] <= user.budget:
            score += 10

        if user.gaming and "gaming" in product["use_case"]:
            score += 20

        if user.coding and "coding" in product["use_case"]:
            score += 15

        scored.append((score, product))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [p for s,p in scored[:2]]
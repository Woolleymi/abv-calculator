def shine_on_calculator():
    # Input recipe details
    recipe_name = input("Enter recipe name: ").strip() or "Test Run"
    while True:
        try:
            gallons_water = float(input("Enter gallons of water: "))
            if gallons_water <= 0:
                print("Gallons must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    adjusted_water = gallons_water
    while True:
        try:
            adj_input = input("Enter water adjustment for honey/molasses/agave (or press Enter for 0): ").strip()
            adjusted_water = float(adj_input) if adj_input else gallons_water
            if adjusted_water <= 0:
                print("Adjusted water must be positive.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    # Input ingredients
    ingredients = []
    total_lbs = 0
    for i in range(1, 6):
        flavor = input(f"Enter flavor for Ingredient {i} (or press Enter to skip): ").strip()
        if not flavor:
            break
        while True:
            try:
                gravity = float(input(f"Enter gravity for {flavor}: "))
                lbs = float(input(f"Enter lbs for {flavor}: "))
                if lbs < 0:
                    print("Lbs cannot be negative.")
                    continue
                total_lbs += lbs
                ingredients.append((flavor, gravity, lbs))
                break
            except ValueError:
                print("Please enter valid numbers.")

    # Input other ingredients
    other_ingredients = []
    for i in range(1, 6):
        name = input(f"Enter name for Other Ingredient {i} (or press Enter to skip): ").strip()
        if not name:
            break
        while True:
            try:
                rec_amount = float(input(f"Enter recommended amount for {name} (tsp): "))
                used_amount = float(input(f"Enter used amount for {name} (tsp): "))
                other_ingredients.append((name, rec_amount, used_amount))
                break
            except ValueError:
                print("Please enter valid numbers.")

    # Calculations
    print(f"\nShine On Calculator v1.9")
    print(f"Make a new recipe!")
    print(f"Section 1 Make a Recipe")
    print(f"  Water adjust for Honey, Molasses or Agave etc.  {adjusted_water:.2f}")
    print(f"  Gallons of water  {gallons_water:.2f}              Grain Efficiency %  100")
    print(f"  Gallons of Wash Expected  {adjusted_water:.2f}")
    print(f"  Recipe Name: {recipe_name}")
    print("| Flavor Ingredient | Gravity | lbs | SG    | ABV  | Percentage |")
    print("|-------------------|---------|-----|-------|------|------------|")

    total_sg = 0
    total_abv = 0
    for flavor, gravity, lbs in ingredients:
        sg = (lbs * gravity * 1000) / (adjusted_water * 1000)  # Simplify to lbs * gravity / gallons
        abv = (sg - 1) * 131.25
        pct = (lbs / total_lbs * 100) if total_lbs > 0 else 0
        total_sg += sg
        total_abv += abv
        print(f"| {flavor:<17} | {gravity:>7} | {lbs:>4.2f} | {sg:>5.3f} | {abv:>4.2f} | {pct:>10.2f}% |")
    print("|-------------------|---------|-----|-------|------|------------|")
    print(f"|{'Totals':<17} |         | {total_lbs:>4.2f} | {total_sg:>5.3f} | {total_abv:>4.2f} | {100.00:>10.2f}% |")

    # Other ingredients and potential alcohol
    print("\n| Other Ingredients | Recommended Amount | Amt Used | Potential Alcohol |")
    print("|-------------------|---------------------|----------|-------------------|")
    potential_alcohol_gallons = total_abv * adjusted_water / 100
    conversions = [
        ("gallons", 1),
        ("half gallons", 2),
        ("quarts", 4),
        ("pints", 8),
        ("half pints", 16)
    ]
    for name, rec_amount, used_amount in other_ingredients:
        print(f"| {name:<17} | {rec_amount:>17.1f} tsp | {used_amount:>8.1f} | {'':>17} |")
    print("|-------------------|---------------------|----------|-------------------|")
    for unit, factor in conversions:
        value = potential_alcohol_gallons * factor
        print(f"| {'':<17} | {'':>17} | {'':>8} | {value:>17.1f} {unit} |")

if __name__ == "__main__":
    shine_on_calculator()
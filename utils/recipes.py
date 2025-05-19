import random

# Recipe database
RECIPES = [
    {
        "name": "Apple Cinnamon Oatmeal",
        "ingredients": ["apple", "oats", "cinnamon", "milk", "honey"],
        "instructions": "Dice the apple. Cook oats with milk. Add diced apple, cinnamon, and honey.",
        "healthy_score": 9
    },
    {
        "name": "Vegetable Stir Fry",
        "ingredients": ["carrot", "broccoli", "bell pepper", "onion", "garlic", "soy sauce", "rice","tomato"],
        "instructions": "Chop all vegetables. Stir fry with garlic. Add soy sauce. Serve over rice.",
        "healthy_score": 8
    },
    {
        "name": "Fruit Salad",
        "ingredients": ["apple", "banana", "orange", "grapes", "honey", "lemon juice"],
        "instructions": "Dice all fruits. Mix with honey and lemon juice.",
        "healthy_score": 10
    },
    {
        "name": "Roasted Vegetables",
        "ingredients": ["potato", "carrot", "onion", "bell pepper", "olive oil", "salt", "pepper", "rosemary"],
        "instructions": "Chop vegetables. Toss with oil and seasonings. Roast at 400°F for 30 minutes.",
        "healthy_score": 9
    },
    {
        "name": "Banana Smoothie",
        "ingredients": ["banana", "milk", "yogurt", "honey", "cinnamon"],
        "instructions": "Blend all ingredients until smooth.",
        "healthy_score": 8
    },
    {
        "name": "Tomato Rice",
        "ingredients": ["tomato", "rice", "onion", "garlic", "spices"],
        "instructions": "Cook rice separately. Prepare tomato gravy with onion, garlic, and spices. Mix together.",
        "healthy_score": 8
    },
    {
        "name": "Tomato Soup",
        "ingredients": ["tomato", "onion", "garlic", "salt", "pepper", "cream"],
        "instructions": "Cook tomatoes with onion and garlic. Blend and season. Serve hot.",
        "healthy_score": 9
    }
]

def recommend_recipes(main_ingredients, available_ingredients, is_fresh=True):
    if not is_fresh:
        return []

    if isinstance(main_ingredients, str):
        all_ingredients = [main_ingredients] + available_ingredients
    else:
        all_ingredients = main_ingredients + available_ingredients

    print(f"DEBUG: All Available Ingredients: {all_ingredients}\n")

    possible_recipes = []

    for recipe in RECIPES:
        required_ingredients = recipe["ingredients"]
        available_count = sum(1 for ing in required_ingredients if ing in all_ingredients)
        match_percentage = (available_count / len(required_ingredients)) * 100

        # Debug prints
        print(f"Checking Recipe: {recipe['name']}")
        print(f" - Required Ingredients: {required_ingredients}")
        print(f" - Ingredients You Have: {all_ingredients}")
        print(f" - Matched Ingredients: {[ing for ing in required_ingredients if ing in all_ingredients]}")
        print(f" - Match Count: {available_count} / {len(required_ingredients)}")
        print(f" - Match Percentage: {match_percentage:.2f}%\n")

        if match_percentage >= 50:
            recipe_copy = recipe.copy()
            recipe_copy["match_percentage"] = match_percentage
            possible_recipes.append(recipe_copy)

    recommended_recipes = sorted(
        possible_recipes,
        key=lambda x: (x["match_percentage"], x["healthy_score"]),
        reverse=True
    )

    print("\nDEBUG: Recommended Recipes after sorting:")
    for rec in recommended_recipes:
        print(f" - {rec['name']}: Match {rec['match_percentage']:.2f}%, Healthy Score {rec['healthy_score']}")

    return recommended_recipes

# TESTING
main_ingredients = ["tomato", "orange", "apple", "potato", "banana"]
available_ingredients = ["onion", "garlic", "rice", "milk", "honey", "carrot"]

recommended_recipes = recommend_recipes(main_ingredients, available_ingredients, is_fresh=True)

print("\nFinal Recommended Recipes:")
if recommended_recipes:
    for recipe in recommended_recipes:
        print(f"Recipe: {recipe['name']}, Match Percentage: {recipe['match_percentage']:.2f}%, Healthy Score: {recipe['healthy_score']}")
else:
    print("No recipes found with your available ingredients.")


    




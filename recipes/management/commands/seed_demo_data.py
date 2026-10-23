from django.core.management.base import BaseCommand

from cooks.models import Cook
from recipes.models import Category, Ingredient, Recipe, RecipeIngredient
from reviews.models import Review


RECIPES = [
    (
        "Lemon ricotta pancakes", "Breakfast", "Fluffy pancakes with creamy ricotta and fresh lemon.",
        "Whisk the ricotta, milk, egg, lemon zest, and juice. Fold in the dry ingredients. Cook small pancakes on a buttered skillet until golden on both sides.",
        25, 4, [("ricotta", 180, "g"), ("flour", 150, "g"), ("milk", 180, "ml"), ("egg", 1, "piece"), ("lemon", 1, "piece")],
    ),
    (
        "Mushroom and spinach omelet", "Breakfast", "A quick savory omelet filled with sauteed mushrooms and spinach.",
        "Saute sliced mushrooms in olive oil until browned. Add spinach until wilted. Pour in beaten eggs, cook until nearly set, fold, and serve.",
        15, 1, [("egg", 3, "pieces"), ("mushrooms", 100, "g"), ("spinach", 40, "g"), ("olive oil", 1, "tbsp")],
    ),
    (
        "Overnight apple cinnamon oats", "Breakfast", "A make-ahead breakfast with rolled oats, apple, and warming cinnamon.",
        "Combine oats, milk, yogurt, grated apple, and cinnamon in a jar. Cover and refrigerate overnight. Add walnuts before serving.",
        10, 2, [("rolled oats", 100, "g"), ("milk", 160, "ml"), ("yogurt", 100, "g"), ("apple", 1, "piece"), ("walnuts", 20, "g")],
    ),
    (
        "Avocado tomato toast", "Breakfast", "Crunchy sourdough topped with lemony avocado and ripe tomatoes.",
        "Toast the sourdough. Mash avocado with lemon juice, salt, and pepper. Spread over the toast and finish with sliced tomatoes.",
        10, 2, [("sourdough bread", 2, "slices"), ("avocado", 1, "piece"), ("tomato", 1, "piece"), ("lemon", 0.5, "piece")],
    ),
    (
        "Roasted red pepper soup", "Lunch", "A smooth, comforting soup made with sweet roasted peppers and tomatoes.",
        "Roast peppers until charred and peel them. Saute onion and garlic, add tomatoes, stock, and peppers, then simmer for 20 minutes. Blend until smooth.",
        45, 4, [("red pepper", 4, "pieces"), ("tomato", 3, "pieces"), ("onion", 1, "piece"), ("vegetable stock", 700, "ml"), ("garlic", 2, "cloves")],
    ),
    (
        "Chickpea cucumber salad", "Lunch", "A fresh lemon-herb salad with chickpeas, cucumber, and feta.",
        "Rinse and drain chickpeas. Dice cucumber and onion, then toss with chickpeas, crumbled feta, parsley, olive oil, and lemon juice.",
        15, 3, [("chickpeas", 400, "g"), ("cucumber", 1, "piece"), ("feta", 100, "g"), ("parsley", 15, "g"), ("lemon", 1, "piece")],
    ),
    (
        "Roasted vegetable couscous", "Lunch", "Pearl couscous tossed with caramelized seasonal vegetables.",
        "Roast chopped zucchini, pepper, and red onion with olive oil until tender. Cook couscous in stock, fluff, and combine with vegetables and lemon zest.",
        35, 4, [("pearl couscous", 250, "g"), ("zucchini", 1, "piece"), ("red pepper", 1, "piece"), ("red onion", 1, "piece"), ("vegetable stock", 400, "ml")],
    ),
    (
        "Tomato basil bruschetta", "Lunch", "Toasted bread topped with juicy tomatoes, basil, and garlic.",
        "Dice tomatoes and mix with torn basil, olive oil, salt, and pepper. Toast bread, rub lightly with garlic, and spoon the tomato mixture on top.",
        20, 4, [("tomato", 4, "pieces"), ("basil", 15, "g"), ("bread", 4, "slices"), ("garlic", 1, "clove"), ("olive oil", 2, "tbsp")],
    ),
    (
        "Creamy pumpkin soup", "Soup", "Silky pumpkin soup with ginger and a swirl of cream.",
        "Saute onion and ginger. Add cubed pumpkin and stock, then simmer until tender. Blend smooth and stir through cream before serving.",
        40, 4, [("pumpkin", 800, "g"), ("onion", 1, "piece"), ("ginger", 10, "g"), ("vegetable stock", 700, "ml"), ("cream", 100, "ml")],
    ),
    (
        "Tuscan white bean soup", "Soup", "A hearty bean soup with kale, tomatoes, and Italian herbs.",
        "Soften onion, carrot, and celery in olive oil. Add garlic, tomatoes, beans, stock, and herbs. Simmer for 25 minutes, stir in kale, and cook until tender.",
        45, 6, [("white beans", 400, "g"), ("kale", 100, "g"), ("tomato", 2, "pieces"), ("carrot", 1, "piece"), ("vegetable stock", 900, "ml")],
    ),
    (
        "Chicken lemon orzo soup", "Soup", "A bright chicken soup with tender orzo and fresh lemon.",
        "Simmer chicken with onion, carrot, and stock until cooked. Shred the chicken, add orzo, and cook until tender. Finish with lemon juice and parsley.",
        40, 5, [("chicken breast", 350, "g"), ("orzo", 150, "g"), ("carrot", 2, "pieces"), ("chicken stock", 1, "l"), ("lemon", 1, "piece")],
    ),
    (
        "Carrot ginger soup", "Soup", "Sweet carrots and fresh ginger blended into a warming soup.",
        "Saute onion and grated ginger. Add sliced carrots and stock, simmer until soft, then blend until creamy. Season and serve warm.",
        35, 4, [("carrot", 600, "g"), ("ginger", 15, "g"), ("onion", 1, "piece"), ("vegetable stock", 750, "ml")],
    ),
    (
        "Spinach pesto pasta", "Dinner", "Pasta coated in a quick spinach, basil, and parmesan pesto.",
        "Cook pasta until al dente. Blend spinach, basil, parmesan, garlic, olive oil, and lemon juice. Toss with pasta and a splash of cooking water.",
        25, 4, [("pasta", 350, "g"), ("spinach", 80, "g"), ("basil", 20, "g"), ("parmesan", 50, "g"), ("olive oil", 3, "tbsp")],
    ),
    (
        "Baked salmon with dill yogurt", "Dinner", "Oven-baked salmon served with a cool dill and yogurt sauce.",
        "Season salmon with lemon, salt, and pepper. Bake at 200 C for 12 to 15 minutes. Stir chopped dill into yogurt and serve alongside the fish.",
        25, 2, [("salmon fillet", 2, "pieces"), ("yogurt", 120, "g"), ("dill", 10, "g"), ("lemon", 1, "piece")],
    ),
    (
        "Lentil coconut curry", "Dinner", "Red lentils simmered in coconut milk with fragrant curry spices.",
        "Saute onion, garlic, and curry powder. Add rinsed lentils, coconut milk, and stock. Simmer until creamy, then finish with lime juice and cilantro.",
        35, 4, [("red lentils", 250, "g"), ("coconut milk", 400, "ml"), ("onion", 1, "piece"), ("curry powder", 2, "tsp"), ("lime", 1, "piece")],
    ),
    (
        "Beef and broccoli stir-fry", "Dinner", "Tender beef and crisp broccoli in a savory ginger soy sauce.",
        "Sear thinly sliced beef in a hot pan and set aside. Stir-fry broccoli, garlic, and ginger. Return beef to the pan with soy sauce and serve over rice.",
        30, 4, [("beef strips", 400, "g"), ("broccoli", 300, "g"), ("soy sauce", 3, "tbsp"), ("ginger", 10, "g"), ("rice", 250, "g")],
    ),
    (
        "Stuffed bell peppers", "Dinner", "Bell peppers filled with herbed rice, tomatoes, and black beans.",
        "Halve and deseed peppers. Mix cooked rice with black beans, tomatoes, cumin, and herbs. Fill peppers and bake covered at 190 C for 30 minutes.",
        50, 4, [("bell pepper", 4, "pieces"), ("rice", 200, "g"), ("black beans", 200, "g"), ("tomato", 2, "pieces"), ("cumin", 1, "tsp")],
    ),
    (
        "Crispy tofu rice bowls", "Dinner", "Golden tofu with rice, crunchy vegetables, and sesame dressing.",
        "Press and cube tofu, then pan-fry until crisp. Serve over rice with sliced cucumber and carrot. Drizzle with soy sauce and sesame oil.",
        35, 2, [("tofu", 300, "g"), ("rice", 180, "g"), ("cucumber", 1, "piece"), ("carrot", 1, "piece"), ("soy sauce", 2, "tbsp")],
    ),
    (
        "One-pan lemon herb chicken", "Dinner", "Juicy chicken thighs roasted with potatoes, lemon, and herbs.",
        "Toss potatoes with olive oil and herbs in a baking dish. Add seasoned chicken thighs and lemon wedges. Roast at 200 C until the chicken is cooked and potatoes are golden.",
        55, 4, [("chicken thighs", 4, "pieces"), ("potato", 600, "g"), ("lemon", 1, "piece"), ("olive oil", 2, "tbsp"), ("thyme", 5, "g")],
    ),
    (
        "Miso glazed eggplant", "Dinner", "Tender roasted eggplant brushed with a savory-sweet miso glaze.",
        "Halve eggplants and score the flesh. Brush with miso, honey, soy sauce, and sesame oil. Roast at 200 C until soft and caramelized; finish with spring onion.",
        40, 2, [("eggplant", 2, "pieces"), ("miso paste", 2, "tbsp"), ("honey", 1, "tbsp"), ("soy sauce", 1, "tbsp"), ("sesame oil", 1, "tsp")],
    ),
    (
        "Garlic shrimp linguine", "Dinner", "Linguine with quick-cooked shrimp, garlic, parsley, and lemon.",
        "Cook linguine until al dente. Gently saute garlic in olive oil, add shrimp, and cook until pink. Toss with pasta, lemon juice, parsley, and pasta water.",
        25, 3, [("linguine", 250, "g"), ("shrimp", 300, "g"), ("garlic", 3, "cloves"), ("parsley", 15, "g"), ("lemon", 1, "piece")],
    ),
    (
        "Roasted sweet potato tacos", "Dinner", "Smoky sweet potato tacos with black beans and lime crema.",
        "Roast cubed sweet potato with smoked paprika until tender. Warm black beans and tortillas. Fill tortillas and top with yogurt mixed with lime juice.",
        35, 4, [("sweet potato", 500, "g"), ("black beans", 240, "g"), ("tortillas", 8, "pieces"), ("yogurt", 100, "g"), ("lime", 1, "piece")],
    ),
    (
        "Greek village salad", "Salad", "A crisp cucumber and tomato salad with olives and creamy feta.",
        "Cut tomatoes, cucumber, and red onion into bite-sized pieces. Add olives and feta, dress with olive oil and oregano, and serve immediately.",
        15, 4, [("tomato", 3, "pieces"), ("cucumber", 1, "piece"), ("feta", 150, "g"), ("olives", 80, "g"), ("red onion", 0.5, "piece")],
    ),
    (
        "Quinoa tabbouleh", "Salad", "A fresh parsley and mint salad with fluffy quinoa and lemon.",
        "Cook quinoa and cool completely. Finely chop parsley, mint, tomato, and cucumber. Toss with quinoa, lemon juice, and olive oil.",
        30, 4, [("quinoa", 180, "g"), ("parsley", 40, "g"), ("mint", 10, "g"), ("tomato", 2, "pieces"), ("lemon", 1, "piece")],
    ),
    (
        "Strawberry spinach salad", "Salad", "Baby spinach, ripe strawberries, toasted almonds, and balsamic dressing.",
        "Toast almonds in a dry pan. Arrange spinach and sliced strawberries in a bowl. Add almonds and feta, then drizzle with balsamic vinegar and olive oil.",
        15, 2, [("spinach", 100, "g"), ("strawberries", 180, "g"), ("almonds", 30, "g"), ("feta", 60, "g"), ("balsamic vinegar", 1, "tbsp")],
    ),
    (
        "Roasted beetroot and orange salad", "Salad", "Earthy roasted beetroot paired with citrus and peppery greens.",
        "Roast wrapped beetroot until tender, cool, and slice. Arrange with orange segments and arugula. Dress with olive oil and orange juice.",
        60, 4, [("beetroot", 500, "g"), ("orange", 2, "pieces"), ("arugula", 60, "g"), ("olive oil", 2, "tbsp")],
    ),
    (
        "Classic banana bread", "Dessert", "Moist banana bread with a golden crust and a hint of vanilla.",
        "Mash ripe bananas and mix with melted butter, sugar, egg, and vanilla. Fold in flour and baking soda. Bake in a loaf tin at 175 C for about 50 minutes.",
        65, 8, [("banana", 3, "pieces"), ("flour", 220, "g"), ("butter", 90, "g"), ("sugar", 100, "g"), ("egg", 1, "piece")],
    ),
    (
        "Dark chocolate pots de creme", "Dessert", "Rich individual chocolate puddings with a silky texture.",
        "Warm cream until steaming. Pour over chopped chocolate and stir until smooth. Whisk in egg yolks and sugar, pour into small dishes, and bake in a water bath until just set.",
        40, 4, [("dark chocolate", 150, "g"), ("cream", 300, "ml"), ("egg yolk", 4, "pieces"), ("sugar", 40, "g")],
    ),
    (
        "Blueberry lemon muffins", "Dessert", "Soft muffins filled with blueberries and bright lemon zest.",
        "Whisk flour, sugar, and baking powder. Fold in milk, egg, melted butter, lemon zest, and blueberries. Divide into muffin cups and bake at 190 C until golden.",
        35, 12, [("flour", 250, "g"), ("blueberries", 150, "g"), ("milk", 180, "ml"), ("egg", 1, "piece"), ("lemon", 1, "piece")],
    ),
    (
        "Vanilla rice pudding", "Dessert", "Creamy stovetop rice pudding scented with real vanilla.",
        "Simmer rice, milk, sugar, and vanilla over low heat, stirring often, until the rice is soft and the mixture is creamy. Serve warm or chilled.",
        40, 4, [("short-grain rice", 150, "g"), ("milk", 800, "ml"), ("sugar", 50, "g"), ("vanilla extract", 1, "tsp")],
    ),
    (
        "Peach and almond crumble", "Dessert", "Juicy baked peaches under a crisp oat and almond topping.",
        "Slice peaches into a baking dish. Rub flour, oats, butter, brown sugar, and almonds together until crumbly. Scatter over fruit and bake at 180 C until bubbling.",
        45, 6, [("peach", 5, "pieces"), ("rolled oats", 80, "g"), ("flour", 100, "g"), ("butter", 75, "g"), ("almonds", 40, "g")],
    ),
]


COOKS = [
    ("Maya Petrov", "Home cook who loves seasonal produce and simple family meals.", "Mediterranean cooking"),
    ("Daniel Brooks", "Weekend baker and enthusiast for comforting soups and breads.", "Baking and soups"),
    ("Sofia Marin", "A curious cook inspired by bright flavors from around the world.", "Vegetarian dishes"),
    ("Liam Carter", "Grill and skillet specialist focused on quick, satisfying dinners.", "Weeknight dinners"),
    ("Nina Georgieva", "Dessert maker who enjoys sharing reliable, approachable recipes.", "Desserts"),
]


class Command(BaseCommand):
    help = "Create or update a collection of recipes and related demo records."

    def handle(self, *args, **options):
        for name, bio, specialty in COOKS:
            Cook.objects.update_or_create(
                display_name=name,
                defaults={"bio": bio, "specialty": specialty},
            )

        cooks = list(Cook.objects.filter(display_name__in=[cook[0] for cook in COOKS]).order_by("display_name"))
        for index, (title, category_name, description, instructions, preparation_time, servings, ingredients) in enumerate(RECIPES):
            category, _ = Category.objects.get_or_create(name=category_name)
            recipe, _ = Recipe.objects.update_or_create(
                title=title,
                defaults={
                    "description": description,
                    "instructions": instructions,
                    "preparation_time": preparation_time,
                    "servings": servings,
                    "category": category,
                },
            )

            for ingredient_name, quantity, unit in ingredients:
                ingredient, _ = Ingredient.objects.get_or_create(
                    name=ingredient_name,
                    defaults={"unit": unit},
                )
                RecipeIngredient.objects.update_or_create(
                    recipe=recipe,
                    ingredient=ingredient,
                    defaults={"quantity": quantity, "unit": unit},
                )

            cook = cooks[index % len(cooks)]
            Review.objects.update_or_create(
                recipe=recipe,
                cook=cook,
                defaults={
                    "rating": 4 + (len(title) % 2),
                    "comment": f"{cook.display_name.split()[0]}: A dependable recipe with clear steps and delicious results.",
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Demo data ready: {Recipe.objects.count()} recipes, "
                f"{Category.objects.count()} categories, {Ingredient.objects.count()} ingredients, "
                f"{Cook.objects.count()} cooks, and {Review.objects.count()} reviews."
            )
        )

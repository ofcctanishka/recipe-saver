from django.shortcuts import render, redirect
from .models import Recipe
def index(request):
    return render(request, 'index.html')
def add_recipe(request):
    recipe_name = request.GET.get("name", "")
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        ingredients = request.POST.get("ingredients")
        process = request.POST.get("process")
        Recipe.objects.create(
            name=recipe_name,
            ingredients=ingredients,
            process=process
        )
        return redirect("/saved/")
    return render(request, "add_recipe.html", {
        "recipe_name": recipe_name
    })
def saved(request):
    recipes = Recipe.objects.all()
    return render(request, "saved.html", {
        "recipes": recipes
    })
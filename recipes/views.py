from django.shortcuts import render, get_list_or_404, get_object_or_404
from recipes.models import Recipe
from django.http import Http404
from utils.recipes.factory import make_recipe
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    )

    if not recipes:
        raise Http404()

    context = {
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
                 f'Recipes',
    }

    return render(request, 'recipes/pages/category.html', context)


def recipe(request, id):
    recipe = get_object_or_404(
        Recipe,
        pk=id,
        is_published=True,
    )

    context = {
        'recipe': recipe,
        'title': f'{recipe.title} - Recipe | Recipes',
    }

    return render(request, 'recipes/pages/recipe-view.html', context)

def search(request):
    return render(request, 'recipes/pages/search.html', context={})


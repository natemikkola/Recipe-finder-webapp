from django.shortcuts import render
import requests

apikey = "UvzfXqqUAxAV04hFbeoWVUhybchxUvgU"

def home(request):
    query = request.GET.get('query')
    url = f'https://api.apilayer.com/spoonacular/recipes/complexSearch?query={query}&diet=none&addRecipeInformation=True&intolerances=none&apikey={apikey}'
    response = requests.get(url)
    data = response.json()
    results = data["results"]
    

    context = {
        'results': results
        
    }
    
    return render(request, 'home.html', context)

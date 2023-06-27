import requests

def search_recipes(app_id, app_key):
    url = "https://api.edamam.com/search"

    ingredients = [input("Enter the ingredients you have at your disposal(separated by commas):")]

    params = {
        "q": ",".join(ingredients),
        "app_id": app_id,
        "app_key": app_key,
        "to": 5  
    }

    
    response = requests.get(url, params=params)
    data = response.json()

    #print(data)

    if response.status_code == 200:
        hits = data["hits"]
        if hits:
            for hit in hits:
                recipe = hit["recipe"]
                recipe_name = recipe["label"]
                recipe_url = recipe["url"]
                print(f"Recipe: {recipe_name}")
                print(f"URL: {recipe_url}")
                print("\n")
        else:
            print("No recipes found.")
    else:
        print(f"Error: Unable to fetch recipes. Status code: {response.status_code}")

# Example usage
app_id = "bd853ae1"
app_key = "8c82c5e3565f991053475e31185e39d0	"
#ingredients = ["Salmon", "Rice"]

search_recipes(app_id, app_key)


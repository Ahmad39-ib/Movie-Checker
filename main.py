import requests


def check_movie(title):
    api_key = "22064610"
    url =f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
    response = requests.get(url)
    # print(dir(response))
    
    if response.status_code != 200:
        return None  
    data = response.json()
    if data.get("Response") == "True":
        return{ 
            "Title": data.get("Title"),
            "Year": data.get("Year"),
            "Genre": data.get("Genre"),
            "plot": data.get("Plot"),
            "Director": data.get("Director"),
            "Released": data.get("Released"),
            "adventure": data.get("Genre"),
            "writer": data.get("Writer"),
            "actors": data.get("Actors")
        }
    else:
        return None    
    

def run():
    print("movie checker")
    title = input("Enter a movie title:").title()
    result = check_movie(title)
    # print(result)
    
    if result:    
        print(f"Title: {result['Title']}")
        print(f"Year: {result['Year']}")
        print(f"Genre: {result['Genre']}")
        print(f"Plot: {result['plot']}")
        print(f"Director: {result['Director']}")
        print(f"Released: {result['Released']}")
        print(f"Adventure: {result['adventure']}")
        print(f"Writer: {result['writer']}")
        print(f"Actors: {result['actors']}")
    else:
        print("Movie not found.")
          
    
    
run()    

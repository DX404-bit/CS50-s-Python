import json
import requests

while True:
    search_term = input("Name of the artist or band: ")
    if search_term.strip():
        break
    else:
        pass

    
while True:
    try:
        desired_results = int(input("How many tracks do you want? "))
        if desired_results > 0:
            break
        else:
            pass
    except ValueError:
        print("Please insert a valueable number for the amount of tracks ")
    


# o limite por pedido (ajutaremos no offset)
results_per_request = desired_results


# Cria uma lista (a set) que vai guardar os nomes das musicas e prevenir duplicas
seen_tracks = set()

# Cria uma lista para armazenar musicas unicas
unique_tracks = []

# offset inicial e limite para o pedido
offset = 0

while len(unique_tracks) < desired_results:
    # Manda pesquisar na itunes com o offset
    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit={results_per_request}&offset= {offset}&term={search_term}")

# Garante que o resultado foi bem sucedido
    if response.status_code != 200:
        print(f"Error: Unable to fetch data (status code {response.status_code})")
        break

    o = response.json()

# Vai dar loop pelos resultados e cuidar das copias
    for result in o["results"]:
        track_name = result["trackName"]
        track_id = result["trackId"]

# Olha se o nome da musica ja esta na seen_tracks
        if track_name not in seen_tracks:
            seen_tracks.add(track_name)
            unique_tracks.append((track_name, track_id)) # Adiciona uma musica unica para a lista

# Para uma vez que pegarmos todos os resultados unicos (nesse caso o usuario que escolhe)
        if len(unique_tracks) >= desired_results:
            break

# Incrementa o offset pra o proximo pedido (pra pegar a proxima lista de resultados)
    offset += results_per_request


for track_name, track_id in unique_tracks:
    print(f"{track_name}: {track_id}")
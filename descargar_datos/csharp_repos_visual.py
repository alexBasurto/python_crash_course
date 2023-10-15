import requests

from plotly.graph_objs import Bar
from plotly import offline

# Hace una llamada a la API y guarda la respuesta.
url = 'https://api.github.com/search/repositories?q=language:csharp+stars:>=1000&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Procesa los resultados.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br>{description}"
    labels.append(label)

# Hace la visualización.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker':{
        'color': 'rgb(254, 92, 92)',
        'line': {'width': 1.5, 'color': 'rgb(189, 62, 62p)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred C# Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
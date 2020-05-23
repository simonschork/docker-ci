import urllib.request, json


with urllib.request.urlopen(
    "http://127.0.0.1:5000/weincheckerapp/api/v1.0/weine"
) as url:
    weine = json.loads(url.read().decode())
    name_eins = weine["weine"][0]["name"]
    rating_eins = weine["weine"][0]["rating"]
    name_zwei = weine["weine"][1]["name"]
    rating_zwei = weine["weine"][1]["rating"]

    print("Der Wein %s wurd mit %d Sternen bewertet." % (name_eins, rating_eins))
    print("Der Wein %s wurd mit %d Sternen bewertet." % (name_zwei, rating_zwei))

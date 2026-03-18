# Problem 4: Nested Data Extraction

data = {
    "users": [
        {"id": 1, "name": "John", "posts": [{"title": 'Hello'}, {"title": "World"}]},
        {"id": 2, "name": "Jane", "posts": [{"title": 'Python'}, {"title": "Rocks"}]}
    ]
}

titles = []
for user in data["users"]:
    for post in user["posts"]:
        titles.append(post["title"])

print(titles)
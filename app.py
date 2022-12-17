import requests
response = requests.get("https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_1280.jpg")
with open("C:/Users/IT/download/cat1.png", "wb") as f:
  f.write(response.content)
  
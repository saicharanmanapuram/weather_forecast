import requests
city=input("Enter the City")
print('Displaying Weather Report For :'+city)
url='https://wttr.in/{}'.format(city)
res=requests.get(url)
print(res.text)

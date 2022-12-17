import requests
import bs4
url=requests.get('https://www.olx.com.eg/vehicles/cars-for-sale/')
src=url.content
name=[]
price=[]
year=[]
locations=[]
data=[]
#print(url.status_code)
#print(src)
soup=bs4.BeautifulSoup(src,"html.parser")
car_name=soup.findAll("div",{"class":"a5112ca8"})
#print(car_name)
car_price=soup.findAll("div",{"class":"_52497c97"})
#print(car_price)
model=soup.findAll("span",{"class":"c47715cd"})
#print(model)
location=soup.findAll("span",{"class":"_424bf2a8"})
#print(location)
publish_date=soup.findAll("span",{"class":"_2e28a695"})
#print(publish_date)
for i in range(len(car_name)):
    name.append(car_name[i].text)
    price.append(car_price[i].text)
    year.append(model[i].text)
    locations.append(location[i].text)
    data.append(publish_date[i].text)
#print(name,year,price,)
for name,year,price,locations,data in zip(name,year,price,locations,data):
    print("{}  : Car_model is{}:  The price is  {}: الموقع={} :publish_date= {}".format(name,year,price,locations,data))

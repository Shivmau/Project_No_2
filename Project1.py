import requests

api_key = "ff5627c3cf97fc3954a1d8e33f9d3992"
user_input = input("Enter your city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}"


url_response=requests.get(url)


if url_response.status_code == 200:
        
        a=url_response.json()
        temp=(a['main']['temp'])
        newtemp=(temp)-273.15
        temp1=format(newtemp,".2f")
        print("the tempature in", user_input, "is" , str(temp1)+"°C")
else:
        print(f"Error: Received status code {url_response.status_code}")





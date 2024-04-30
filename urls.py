import requests

# product_id = int(input("id: "))
# product_name = input("product: ")

url = f"http://127.0.0.1:8000"

response = requests.get(url)

print(response.json())
import os
import requests

# === Настройки ===
UNSPLASH_API_KEY = "eH04hunae89ht5Zyhg_mzppjvorlHM977uOpb18HSI8"
save_dir = "/storage/emulated/0/Download/country_photos"
os.makedirs(save_dir, exist_ok=True)

# === Ввод от пользователя ===
country = input("Введите название страны на английском: ").strip()
if not country:
    print("Ошибка: не указана страна")
    exit()

# === Поиск фото через Unsplash API ===
url = "https://api.unsplash.com/search/photos "
headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
params = {
    "query": f"{country} country",
    "per_page": 1
}

try:
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if data.get("results"):
        photo_url = data["results"][0]["urls"]["regular"]
        img_data = requests.get(photo_url).content

        filename = f"{country.replace(' ', '_')}.jpg"
        filepath = os.path.join(save_dir, filename)

        with open(filepath, "wb") as handler:
            handler.write(img_data)

        print(f"\nФото успешно сохранено:\n{filepath}")
    else:
        print("Не удалось найти фото.")
        print("Ответ сервера:", data)

except Exception as e:
    print(f"Произошла ошибка: {e}")
import os
import requests

PAGE_ID = os.getenv("FACEBOOK_PAGE_ID")
ACCESS_TOKEN = os.getenv("FACEBOOK_PAGE_TOKEN")

def publish_post(message):
    if not PAGE_ID or not ACCESS_TOKEN:
        print("Facebook settings are missing")
        return

    url = f"https://graph.facebook.com/{PAGE_ID}/feed"

    response = requests.post(
        url,
        data={
            "message": message,
            "access_token": ACCESS_TOKEN
        }
    )

    print(response.json())


if __name__ == "__main__":
    print("🇲🇦 Morocco Fans Bot is ready!")

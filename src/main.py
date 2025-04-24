import flet as ft
import pyperclip
import requests
import keyboard
import threading

#  Replace this with your own Janice API Key | https://github.com/E-351/janice
API_KEY = "YOur_API_KEY_HERE"

def process_price_command(content):
    try:
        api_url = "https://janice.e-351.com/api/rest/v2/appraisal"
        params = {
            "market": "2",
            "persist": "true",
            "compactize": "true",
            "pricePercentage": "1"
        }
        headers = {
            "accept": "application/json",
            "X-ApiKey": API_KEY,
            "Content-Type": "text/plain"
        }

        response = requests.post(api_url, params=params, headers=headers, data=content)

        if response.status_code == 200:
            data = response.json()
            return {
                "sell": data["immediatePrices"]["totalSellPrice"],
                "buy": data["immediatePrices"]["totalBuyPrice"],
                "volume": data["totalVolume"],
                "url": f"https://janice.e-351.com/a/{data['code']}"
            }
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def setup_hotkey(update_fields):
    def on_ctrl_c():
        content = pyperclip.paste()
        result = process_price_command(content)
        if result:
            update_fields(result)

    keyboard.add_hotkey(
        'ctrl+c',
        on_ctrl_c,
        suppress=False,
        trigger_on_release=True
    )

def main(page: ft.Page):
    page.title = "CopyPasta"
    #Page setup
    page.window.width = 300
    page.window.height = 300
    page.window.resizable = False
    page.window.maximizable = False
    page.window.minimizable = False
    page.window.always_on_top = True

    # UI elements
    sell_value_input = ft.TextField(label="Sell Value", read_only=True , value="N/A")
    buy_value_input = ft.TextField(label="Buy Value", read_only=True, value="N/A")
    volume_input = ft.TextField(label="Volume", read_only=True, value="N/A")
    janice_link = ft.TextButton("View on Janice", url="https://janice.e-351.com/")

    def update_fields(result):
        sell_value_input.value = f"{result['sell']:,} ISK"
        buy_value_input.value = f"{result['buy']:,} ISK"
        volume_input.value = f"{result['volume']:,} M3"
        janice_link.url = result.get("url", janice_link.url)
        page.update()

    # Start hotkey listener in a thread so it doesn't block
    threading.Thread(target=setup_hotkey, args=(update_fields,), daemon=True).start()

    # Layout
    page.add(
        ft.Column([
            ft.Row([ft.Text("Janice Link:"), janice_link], alignment="spaceBetween"),
            sell_value_input,
            buy_value_input,
            volume_input
        ], spacing=20)
    )

ft.app(target=main, assets_dir="assets")

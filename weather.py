import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "3d3c932124ec73caaef6fc2e0577d37e"  # 🔑 Replace with your OpenWeatherMap API key

def get_weather():
    city = city_input.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == "404":
            result_label.config(text="❌ City not found!")
            return

        name        = data["name"]
        country     = data["sys"]["country"]
        temp        = data["main"]["temp"]
        description = data["weather"][0]["description"].capitalize()
        wind        = data["wind"]["speed"]

        result = (
            f"📍 {name}, {country}\n"
            f"🌡  Temperature : {temp}°C\n"
            f"☁   Weather     : {description}\n"
            f"💨  Wind Speed  : {wind} m/s"
        )
        result_label.config(text=result)

    except Exception:
        result_label.config(text="⚠ Something went wrong!")


# ── Window setup ──────────────────────────────────────────────
root = tk.Tk()
root.title("Weather App")
root.geometry("380x320")
root.resizable(False, False)
root.configure(bg="#1a1a2e")

# ── Title ─────────────────────────────────────────────────────
title = tk.Label(
    root, text="🌤 Weather App",
    font=("Arial", 20, "bold"),
    bg="#1a1a2e", fg="#74ebd5"
)
title.pack(pady=(24, 8))

# ── Input field ───────────────────────────────────────────────
city_input = tk.Entry(
    root,
    font=("Arial", 14),
    width=22,
    bd=0,
    relief="flat",
    bg="#16213e",
    fg="#ffffff",
    insertbackground="#74ebd5",
    justify="center"
)
city_input.pack(ipady=8, pady=(8, 6))
city_input.insert(0, "Enter city name")
city_input.bind("<FocusIn>",  lambda e: city_input.delete(0, "end") if city_input.get() == "Enter city name" else None)
city_input.bind("<Return>", lambda e: get_weather())   # Press Enter to search

# ── Button ────────────────────────────────────────────────────
btn = tk.Button(
    root, text="Get Weather",
    font=("Arial", 13, "bold"),
    bg="#74ebd5", fg="#1a1a2e",
    activebackground="#55c9b5",
    bd=0, relief="flat",
    padx=16, pady=6,
    cursor="hand2",
    command=get_weather
)
btn.pack(pady=10)

# ── Result label ──────────────────────────────────────────────
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13),
    bg="#1a1a2e", fg="#ffffff",
    justify="left",
    wraplength=320
)
result_label.pack(pady=16, padx=24, anchor="w")

root.mainloop()
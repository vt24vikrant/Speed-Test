import tkinter as tk

import engine

window = tk.Tk()
window.title("Internet Speed Test")
window.geometry("300x200")

title_label = tk.Label(window, text="Internet Speed Test", font=("Arial", 16))
title_label.pack(pady=10)

download_label = tk.Label(window, text="Download Speed: N/A", font=("Arial", 12))
download_label.pack(pady=5)

upload_label = tk.Label(window, text="Upload Speed: N/A", font=("Arial", 12))
upload_label.pack(pady=5)

ping_label = tk.Label(window, text="Ping: N/A", font=("Arial", 12))
ping_label.pack(pady=5)


def run_speed_test():
    engine.run_engine(download_label, upload_label, ping_label)


run_button = tk.Button(window, text="Run Test", command=run_speed_test, font=("Arial", 12))
run_button.pack(pady=10)

window.mainloop()

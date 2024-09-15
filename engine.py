from tkinter import messagebox

import speedtest as st


def run_engine(download_label, upload_label, ping_label):
    try:
        test = st.Speedtest()

        down_speed = test.download()
        down_speed = round(down_speed / 10**6, 2)

        up_speed = test.upload()
        up_speed = round(up_speed / 10**6, 2)

        ping = test.results.ping

        download_label.config(text=f"Download Speed: {down_speed} Mbps")
        upload_label.config(text=f"Upload Speed: {up_speed} Mbps")
        ping_label.config(text=f"Ping: {ping} ms")

    except Exception as e:
        messagebox.showerror("Error", f"Error performing speed test: {e}")

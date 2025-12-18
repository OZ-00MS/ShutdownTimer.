import os
import tkinter as tk
from tkinter import messagebox

def schedule_shutdown(minutes):
    seconds = minutes * 60
    os.system(f"shutdown /s /t {seconds}")
    messagebox.showinfo("Shutdown Scheduled", f"Your PC will shut down in {minutes} minutes.")

def cancel_shutdown():
    os.system("shutdown /a")
    messagebox.showinfo("Cancelled", "Scheduled shutdown has been cancelled.")

def create_gui():
    root = tk.Tk()
    root.title("Shutdown Timer")
    root.geometry("400x450")
    root.configure(bg="#1e1e2f")
    root.resizable(False, False)

    title = tk.Label(root, text="🕒 Shutdown Timer", font=("Helvetica", 20, "bold"),
                     fg="#ffffff", bg="#1e1e2f")
    title.pack(pady=(15, 5))

    subtitle = tk.Label(root, text="Select a time to shut down your PC:",
                        font=("Helvetica", 12), fg="#bbbbbb", bg="#1e1e2f")
    subtitle.pack(pady=(0, 10))

    frame = tk.Frame(root, bg="#1e1e2f")
    frame.pack(pady=10)

    button_style = {
        "font": ("Helvetica", 14),
        "bg": "#2d89ef",
        "fg": "white",
        "activebackground": "#1e5abf",
        "width": 15,
        "height": 2,
        "bd": 0
    }

    times = [5, 10, 15, 20, 30, 40]
    for i, t in enumerate(times):
        btn = tk.Button(frame, text=f"{t} Minutes", command=lambda t=t: schedule_shutdown(t), **button_style)
        btn.grid(row=i // 2, column=i % 2, padx=10, pady=6)

    cancel_btn = tk.Button(root, text="Cancel Shutdown", command=cancel_shutdown,
                           font=("Helvetica", 14), bg="#e81123", fg="white",
                           activebackground="#a80000", width=20, height=2, bd=0)
    cancel_btn.pack(pady=15)

    footer = tk.Label(root, text="with OZ ❤️ in Python", font=("Helvetica", 10),
                      fg="#888888", bg="#1e1e2f")
    footer.pack(side="bottom", pady=5)

    root.mainloop()

if __name__ == "__main__":
    create_gui()

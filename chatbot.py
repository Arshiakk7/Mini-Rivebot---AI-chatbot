# import tkinter as tk
# from rivescript import RiveScript

# # Load RiveScript brain
# bot = RiveScript()
# bot.load_file("brain.rive")
# bot.sort_replies()

# # Create GUI window
# root = tk.Tk()
# root.title("Mini RiveBot 🤖")
# root.geometry("400x500")

# # Chat window
# chat_window = tk.Text(root, bd=1, bg="black", fg="white", font=("Arial", 12))
# chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# chat_window.config(state=tk.DISABLED)

# # User input
# user_input = tk.Entry(root, bd=1, bg="white", fg="black", font=("Arial", 12))
# user_input.pack(padx=10, pady=10, fill=tk.X)
# user_input.focus()

# # Function to handle sending message
# def send_message(event=None):
#     msg = user_input.get()
#     if msg.strip() == "":
#         return
#     chat_window.config(state=tk.NORMAL)
#     chat_window.insert(tk.END, f"You: {msg}\n")
    
#     if msg.lower() == "quit":
#         chat_window.insert(tk.END, "Bot: Goodbye! 👋\n")
#         root.after(500, root.destroy)
#         return

#     reply = bot.reply("localuser", msg)
#     chat_window.insert(tk.END, f"Bot: {reply}\n")
#     chat_window.config(state=tk.DISABLED)
#     chat_window.see(tk.END)
#     user_input.delete(0, tk.END)

# # Bind Enter key to send message
# user_input.bind("<Return>", send_message)

# # Send button
# send_button = tk.Button(root, text="Send", command=send_message, bg="lightblue", fg="black")
# send_button.pack(pady=5)

# root.mainloop()

# import tkinter as tk
# from rivescript import RiveScript

# # Load RiveScript brain
# bot = RiveScript()
# bot.load_file("brain.rive")
# bot.sort_replies()

# # Create GUI window
# root = tk.Tk()
# root.title("Mini RiveBot 🤖")
# root.geometry("400x500")
# root.configure(bg="lightgreen")  # window background

# # Chat window
# chat_window = tk.Text(
#     root,
#     bd=1,
#     bg="lightgreen",   # ✅ changed here
#     fg="black",
#     font=("Arial", 12)
# )
# chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
# chat_window.config(state=tk.DISABLED)

# # User input (UNCHANGED - white)
# user_input = tk.Entry(
#     root,
#     bd=1,
#     bg="white",   # ✅ stays white
#     fg="black",
#     font=("Arial", 12)
# )
# user_input.pack(padx=10, pady=10, fill=tk.X)
# user_input.focus()

# # Function to handle sending message
# def send_message(event=None):
#     msg = user_input.get()
#     if msg.strip() == "":
#         return

#     chat_window.config(state=tk.NORMAL)
#     chat_window.insert(tk.END, f"You: {msg}\n")
    
#     if msg.lower() == "quit":
#         chat_window.insert(tk.END, "Bot: Goodbye! 👋\n")
#         root.after(500, root.destroy)
#         return

#     reply = bot.reply("localuser", msg)
#     chat_window.insert(tk.END, f"Bot: {reply}\n")
#     chat_window.config(state=tk.DISABLED)
#     chat_window.see(tk.END)
#     user_input.delete(0, tk.END)

# # Bind Enter key
# user_input.bind("<Return>", send_message)

# # Send button
# send_button = tk.Button(
#     root,
#     text="Send",
#     command=send_message,
#     bg="lightblue",
#     fg="black"
# )
# send_button.pack(pady=5)

# root.mainloop()

import tkinter as tk
from rivescript import RiveScript

# Load RiveScript brain
bot = RiveScript()
bot.load_file("brain.rive")
bot.sort_replies()

# Create GUI window
root = tk.Tk()
root.title("Mini RiveBot 🤖")
root.geometry("400x500")
root.configure(bg="lightgreen")  # ✅ background

# Chat window (WHITE)
chat_window = tk.Text(
    root,
    bd=1,
    bg="white",   # ✅ output white
    fg="black",
    font=("Arial", 12)
)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.config(state=tk.DISABLED)

# User input (WHITE)
user_input = tk.Entry(
    root,
    bd=1,
    bg="white",   # ✅ input white
    fg="black",
    font=("Arial", 12)
)
user_input.pack(padx=10, pady=5, fill=tk.X)
user_input.focus()

# Save chat
def save_chat(text):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        file.write(text + "\n")

# Send message
def send_message(event=None):
    msg = user_input.get()
    if msg.strip() == "":
        return

    chat_window.config(state=tk.NORMAL)

    chat_window.insert(tk.END, f"You: {msg}\n")
    save_chat(f"You: {msg}")

    if msg.lower() == "quit":
        chat_window.insert(tk.END, "Bot: Goodbye! 👋\n")
        save_chat("Bot: Goodbye! 👋")
        root.after(500, root.destroy)
        return

    reply = bot.reply("localuser", msg)
    chat_window.insert(tk.END, f"Bot: {reply}\n")
    save_chat(f"Bot: {reply}")

    chat_window.config(state=tk.DISABLED)
    chat_window.see(tk.END)
    user_input.delete(0, tk.END)

# Clear chat function
def clear_chat():
    chat_window.config(state=tk.NORMAL)
    chat_window.delete(1.0, tk.END)
    chat_window.config(state=tk.DISABLED)

# Bind Enter key
user_input.bind("<Return>", send_message)

# Button frame (IMPORTANT: give space + fill)
button_frame = tk.Frame(root, bg="lightgreen")
button_frame.pack(pady=10, fill=tk.X)

# Send button
send_button = tk.Button(
    button_frame,
    text="Send",
    command=send_message,
    bg="lightblue",
    fg="black",
    font=("Arial", 11, "bold"),
    height=1,
    width=12
)
send_button.pack(side=tk.LEFT, padx=20)

# Clear button
clear_button = tk.Button(
    button_frame,
    text="Clear Chat",
    command=clear_chat,
    bg="white",
    fg="black",
    font=("Arial", 11, "bold"),
    height=1,
    width=12
)
clear_button.pack(side=tk.RIGHT, padx=20)
root.mainloop()
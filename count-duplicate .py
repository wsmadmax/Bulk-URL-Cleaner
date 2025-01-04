import tkinter as tk
from tkinter import filedialog

def count_duplicate_sentences(file_path):
    sentences = []
    duplicate_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            sentence = line.strip()
            if sentence in sentences:
                duplicate_count += 1
            else:
                sentences.append(sentence)

    return duplicate_count

def browse_file():
    file_path = filedialog.askopenfilename()
    duplicate_count = count_duplicate_sentences(file_path)
    status_label.config(text=f"Number of duplicate sentences: {duplicate_count}")

# Create the GUI window
window = tk.Tk()
window.title("Count Duplicate Sentences")
window.geometry("300x100")

# Create the Upload button
upload_button = tk.Button(window, text="Upload File", command=browse_file)
upload_button.pack(pady=20)

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()

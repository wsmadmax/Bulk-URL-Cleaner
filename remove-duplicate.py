import tkinter as tk
from tkinter import filedialog

def remove_duplicates(file_path):
    with open(file_path, 'r') as file:
        sentences = file.readlines()

    unique_sentences = list(set(sentences))
    modified_sentence = ''.join(unique_sentences)

    with open(file_path, 'w') as file:
        file.write(modified_sentence)

def browse_file():
    file_path = filedialog.askopenfilename()
    remove_duplicates(file_path)
    status_label.config(text="Duplicates removed successfully!")

# Create the GUI window
window = tk.Tk()
window.title("Remove Duplicate Sentences")
window.geometry("300x100")

# Create the Upload button
upload_button = tk.Button(window, text="Upload File", command=browse_file)
upload_button.pack(pady=20)

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()

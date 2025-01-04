import tkinter as tk
from tkinter import filedialog

def remove_duplicate_sentences(input_files, output_file):
    unique_sentences = set()

    for file_path in input_files:
        with open(file_path, 'r') as file:
            for line in file:
                sentence = line.strip()
                if sentence not in unique_sentences:
                    unique_sentences.add(sentence)

    with open(output_file, 'w') as file:
        for sentence in unique_sentences:
            file.write(sentence + '\n')

def browse_files():
    input_files = filedialog.askopenfilenames()
    if input_files:
        output_file = filedialog.asksaveasfilename(defaultextension=".txt")
        remove_duplicate_sentences(input_files, output_file)
        status_label.config(text="Duplicate sentences removed and saved successfully!")

# Create the GUI window
window = tk.Tk()
window.title("Remove Duplicate Sentences")
window.geometry("300x100")

# Create the Upload button
upload_button = tk.Button(window, text="Upload Files", command=browse_files)
upload_button.pack(pady=20)

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()

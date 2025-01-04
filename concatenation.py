import tkinter as tk
from tkinter import filedialog

def combine_files(output_file, input_files):
    with open(output_file, 'w') as output:
        for file_path in input_files:
            with open(file_path, 'r') as file:
                output.write(file.read())

def browse_files():
    input_files = filedialog.askopenfilenames()
    if input_files:
        output_file = filedialog.asksaveasfilename(defaultextension=".txt")
        combine_files(output_file, input_files)
        status_label.config(text="Files combined successfully!")

# Create the GUI window
window = tk.Tk()
window.title("Combine Files")
window.geometry("300x100")

# Create the Upload button
upload_button = tk.Button(window, text="Upload Files", command=browse_files)
upload_button.pack(pady=20)

# Create the status label
status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI event loop
window.mainloop()

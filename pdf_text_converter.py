import os
from tkinter import *
from tkinter import filedialog, messagebox
import customtkinter

def convert(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None, f"File '{input_file}' not found."
    except Exception as e:
        return None, f"An error occurred while reading the file: {e}"

    result = []

    for line in lines:
        line = line.strip()
        if line:  # Check if the line is not empty
            if line[-1] in ".!?":
                result.append(line + "\n")
            else:
                result.append(line)

    # Join the transcript lines into a single string
    result_text = ' '.join(result)
    return result_text, "Conversion Successful"

def save_result_as_file(base_name, transcript_path, transcript):
    file_name = os.path.join(transcript_path, f"{base_name}_converted.txt")
    if file_name:
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(transcript)
            return f"Transcript saved as {file_name}"
        except Exception as e:
            return f"An error occurred while saving the file: {e}"

def open_file_dialog():
    input_file = filedialog.askopenfilename(title="Open .txt File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    transcript_path = os.path.dirname(input_file)
    if input_file:
        print(input_file)
        transcript, message = convert(input_file)
        if transcript is not None:
            result_message = save_result_as_file(base_name, transcript_path, transcript)
            messagebox.showinfo("Conversion Result:", message + "\n" + result_message)
        else:
            messagebox.showerror("Conversion Error:", message)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("300x400")
app.title('PDF txt Converter')

# Use the customtkinter button
open_bt = customtkinter.CTkButton(app, text="Open .txt File", command=open_file_dialog)
open_bt.place(relx=0.5, rely=0.5, anchor=CENTER)

app.mainloop()
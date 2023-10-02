import os
from tkinter import *
from tkinter import filedialog, messagebox
import customtkinter

def srt_to_transcript(input_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return None, f"File '{input_file}' not found."
    except Exception as e:
        return None, f"An error occurred while reading the file: {e}"

    transcript = []

    for line in lines:
        line = line.strip()
        line = line.replace(">>", "")
        if line.isdigit() or '-->' in line:  # Skip subtitle numbers and timestamps
            continue
        elif line:  # Check if the line is not empty
            if line[-1] in ".!?":
                transcript.append(line + "\n")
            else:
                transcript.append(line)

    # Join the transcript lines into a single string
    transcript_text = ' '.join(transcript)
    return transcript_text, "Conversion Successful"

def save_transcript_as_txt(base_name, transcript_path, transcript):
    file_name = os.path.join(transcript_path, f"{base_name}.txt")
    if file_name:
        try:
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(transcript)
            return f"Transcript saved as {file_name}"
        except Exception as e:
            return f"An error occurred while saving the file: {e}"

def open_file_dialog():
    input_file = filedialog.askopenfilename(title="Open .srt File", filetypes=[("SRT files", "*.srt"), ("All files", "*.*")])
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    transcript_path = os.path.dirname(input_file)
    if input_file:
        print(input_file)
        transcript, message = srt_to_transcript(input_file)
        if transcript is not None:
            result_message = save_transcript_as_txt(base_name, transcript_path, transcript)
            messagebox.showinfo("Conversion Result:", message + "\n" + result_message)
        else:
            messagebox.showerror("Conversion Error:", message)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("300x400")
app.title('SRT to Transcript Converter')

# Use the customtkinter button
open_bt = customtkinter.CTkButton(app, text="Open .srt File", command=open_file_dialog)
open_bt.place(relx=0.5, rely=0.5, anchor=CENTER)

app.mainloop()
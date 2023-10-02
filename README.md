# Text File Generator

Text File Generator is a Python program that simplifies the conversion of text extracted directly from various file formats, such as PDF files and SRT files, into easily readable text files.

## Features

### pdf_text_converter.py

- **File Text Extraction:** Converts text extracted directly from PDF files into easily readable text (TXT) files.
- **Text Formatting:** Formats text by removing empty lines and ensuring proper sentence endings.
- **Intuitive GUI:** Provides a graphical user interface for easy file selection and conversion.

### srt_converter.py

- **SRT to Transcript:** Converts subtitle files (SRT) into a transcript in text (TXT) format.
- **Text Cleanup:** Removes subtitle numbering and timestamps, ensuring a clean transcript.
- **Intuitive GUI:** Includes a user-friendly graphical interface for selecting and converting SRT files.

## Usage

### pdf_text_converter.py

1. **Installation:** Clone this repository to your local machine.

    ```bash
    git clone https://github.com/alex-roh/Text-File-Generator.git 
    ```

2. **Dependencies:** Install the necessary dependencies by running:
            
    ```bash
    pip install -r requirements.txt
    ```

3. **Execution:** Run the program using the following command:

    ```bash
    python pdf_text_converter.py
    ```

4. **Usage:** Click the "Open .txt File" button in the graphical interface to select a text file for conversion. The program will format the text and save it as a TXT file.

### srt_converter.py

1. **Installation:** Clone this repository to your local machine if you haven't already.

    ```bash
    git clone https://github.com/alex-roh/Text-File-Generator.git  
    ```
    
2. **Dependencies:** Install the necessary dependencies by running:
            
    ```bash
    pip install -r requirements.txt
    ```

3. **Execution:** Run the program using the following command:

    ```bash
    python srt_converter.py
    ```


4. **Usage:** Click the "Open .srt File" button in the graphical interface to select an SRT subtitle file for conversion. The program will generate a clean transcript in TXT format.

## Contribution

Contributions to this project are welcome! If you have ideas for improvements or new features, please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.



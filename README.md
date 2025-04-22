# CVS Splitter and Email Enhancer

This tool is designed to help you:
- **Split large CSV files** into **smaller individual CSV files**.
- **Analyze and enhance emails** for phishing by extracting key information such as sender/receiver details, IP addresses, and links from CSV files containing email data.

---

## Why I Created This Tool

I created this tool because I found there was no easy solution to:
- Split **large CSV files** into smaller, more manageable chunks.
- Extract and analyze **email details** to detect potential phishing attacks.

Now, with this tool, you can:
- Split a large CSV file into smaller individual files based on row count.
- Automatically extract relevant email data to aid in phishing email analysis.

---

## Requirements

To run this tool, you need to have **Python** installed on your Windows machine.

### 1. Install Python:
- Download and install **Python 3.x** from [here](https://www.python.org/downloads/).
- Make sure to check **"Add Python to PATH"** during the installation process.

### 2. Install Required Libraries:
- Open **Command Prompt** and run the following command to install the required libraries:
    ```bash
    pip install tkinter requests
    ```

---

## How to Use the Tool

### Step 1: Download the Code

1. Download the **`split_csv_gui.py`** file directly from this repository [here](https://github.com/Iamfazi1/CVS-Splitter-and-Email-Enhancer/blob/main/split_csv_gui.py).

### Step 2: Run the Tool

1. After downloading the file, simply **double-click** on `split_csv_gui.py`.
2. The tool will automatically launch a **GUI** window.
   
### Features:

- **CSV Splitter**: 
  - Allows you to select a large CSV file and **split** it into **smaller individual CSV files**. 
  - You can specify the number of rows per file, and the tool will generate separate CSV files accordingly.
  
- **Email Enhancer**: 
  - Select a CSV file containing email data for analysis. 
  - The tool will automatically extract important email details, including sender/receiver info, IP addresses, and links to help identify potential phishing threats.

---

## Enjoy!

This tool was built to make it easy for you to manage large CSV files and analyze emails for phishing attempts. Just download, run, and start using it immediately!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

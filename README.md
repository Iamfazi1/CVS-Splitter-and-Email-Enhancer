# CVS Splitter and Email Enhancer

This Python tool comes with a **GUI** that provides:
1. **CVS Splitter**: Split large CVS files into smaller, more manageable chunks.
2. **Email Enhancer**: Analyze emails to extract key artifacts such as sender/receiver info, IP addresses, and links to detect phishing attempts.

## Features
- **CVS Splitter**: Easily split large CSV files into smaller parts.
- **Email Enhancer**: Analyze emails for potential phishing attempts with easy-to-read output.

## Requirements
- Python 3.x
- Required Python libraries:
  - `tkinter` (for the GUI)
  - `email` (for email parsing)
  - `re` (for regex operations)
  - `requests` (for link validation)

## Installation and Setup

1. **Download the Code**:
   - First, clone the repository or download the ZIP file:
     - **Clone**: 
       ```bash
       git clone https://github.com/YOUR_USERNAME/CVS-Splitter-and-Email-Enhancer.git
       cd CVS-Splitter-and-Email-Enhancer
       ```
     - **Download ZIP**: [Download ZIP](https://github.com/YOUR_USERNAME/CVS-Splitter-and-Email-Enhancer/archive/refs/heads/main.zip)

2. **Install Dependencies**:
   - Make sure you have Python 3.x installed on your computer.
   - Install the required Python libraries using `pip`:
     ```bash
     pip install tkinter requests
     ```

3. **Run the Application**:
   - Navigate to the folder where the script is located.
   - Double-click on `app.py` or run it using Python:
     ```bash
     python app.py
     ```

   The GUI will open up, and you can choose either the **CVS Splitter** or **Email Enhancer** functionality from the interface.

## Usage

1. **CVS Splitter**:
   - Click on the **Split CVS File** button.
   - Choose the large CSV file you want to split.
   - Set the number of rows per file.
   - Click **Split** to create smaller CSV files.

2. **Email Enhancer**:
   - Click on the **Analyze Email** button.
   - Select the email file you want to analyze.
   - The tool will process the email and extract important details like sender/receiver info, IP addresses, and links.
   
   The results will be displayed in the application window for easy review.

## Enjoy!
Just run the `app.py` file, and you're ready to use the **CVS Splitter** and **Email Enhancer** tools via a friendly GUI interface.

## Contributing

Feel free to fork the repository, make improvements, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# README

## WhatsApp Group Presence Report Bot

The WhatsApp Group Presence Report Bot is a web-based application that allows users to upload WhatsApp chat files and generate detailed monthly presence reports. It helps track group activity by analyzing who joined or left the group over time.

### Features
- Upload WhatsApp chat files in `.txt` format.
- Parse chat files to extract presence events (e.g., "joined" or "left").
- Generate monthly reports summarizing group activity.
- View reports in a user-friendly web interface.
### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to `http://127.0.0.1:5000`.

### Usage
1. On the main page, upload a WhatsApp chat file in `.txt` format.
2. The bot will process the file and generate monthly presence reports.
3. View the reports directly on the web interface.

### Notes
- Ensure the chat file is exported in text format from WhatsApp.
- Only `.txt` files are supported for upload.
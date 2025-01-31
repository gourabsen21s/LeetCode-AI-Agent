```markdown
# AI Agent for LeetCode Solver

This project is an AI-powered agent that automates the process of solving problems on LeetCode. The agent logs in to a user's LeetCode account, navigates to problems, and submits solutions sequentially. The process is displayed live to the user via a web interface. 

## Features
- User can input their LeetCode credentials (username and password) on the website.
- Once credentials are provided, the AI agent will:
  - Log in to LeetCode.
  - Navigate to problem-solving sections.
  - Automatically attempt to solve problems sequentially.
  - Submit solutions and check if test cases pass.
- Real-time updates and status messages are displayed to the user during the entire process.
- Built using Flask for the backend, Node.js as the server, and Selenium for browser automation.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript (Axios for API calls)
- **Backend**: Python (Flask, Selenium)
- **Server**: Node.js (Express.js)
- **Web Automation**: Selenium, WebDriver, ChromeDriver, PyAutoGUI (optional for some tasks)

## Setup and Installation

### Prerequisites
Ensure the following are installed on your machine:
- **Python 3.x**
- **Node.js** and **npm**
- **Chrome WebDriver** (automatically installed with `webdriver_manager`)

### Backend Setup (Flask + Selenium)

1. Clone this repository to your local machine:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask backend:
   ```bash
   python app.py
   ```

   This will start the Flask server at `http://localhost:1000/`.

### Frontend Setup (HTML + JavaScript)

1. Navigate to the frontend folder:
   ```bash
   cd frontend
   ```

2. Open the `index.html` file in your web browser.

### Server Setup (Node.js)

1. Install the required Node.js dependencies:
   ```bash
   npm install
   ```

2. Run the server:
   ```bash
   node server.js
   ```

   The Node.js server will run at `http://localhost:3000/` and will communicate with the Flask API.

## How It Works

1. When the user visits the web interface, they will be prompted to input their LeetCode credentials (username and password).
2. Upon submission, the credentials are sent to the Node.js server using Axios.
3. The Node.js server forwards the credentials to the Flask backend via an API call.
4. The Flask backend uses Selenium to log into LeetCode, navigate the site, and solve problems.
5. During the automation process, the frontend displays the current status of the operation in real time.
6. The Flask backend interacts with the browser, and the AI agent solves problems sequentially.

## Known Issues
- CAPTCHA challenges or verification screens might cause issues with the automation process.
- The system may be fragile if the layout or DOM structure of LeetCode changes, as PyAutoGUI relies on specific coordinates.

## Future Improvements
- Adding CAPTCHA-solving mechanisms or AI-based verification.
- Making the system more robust against UI changes.
- Storing progress and data in a database for better tracking of solved problems.

## License
This project is currently **under development**. No license has been defined yet.

---

If you encounter any issues or would like to contribute to the project, feel free to submit an issue or pull request.
```

### Notes:
- This README includes instructions for setup and installation.
- It clearly explains the project's features, tech stack, setup process, and limitations.
- The **"Under Development"** notice is mentioned under the license section.

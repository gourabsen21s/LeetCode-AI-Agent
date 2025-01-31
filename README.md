# 🚀 AI Agent - LeetCode Solver 🤖

This project allows you to automate solving LeetCode problems using a custom AI agent. You can pass your LeetCode cookies, and the AI will start solving problems one by one automatically. The process is visible to the user in real-time!

## ⚙️ Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Axios)
- **Backend**: Flask (Python)
- **Automation**: Selenium WebDriver
- **API**: Node.js (Express.js)
- **Others**: WebDriver Manager, CORS

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/gourabsen21s/leetcode-ai-agent.git
cd leetcode-ai-agent
```

### 2. Backend Setup (Python with Flask)

#### Requirements:
- Python 3.x
- Install dependencies with:

```bash
pip install -r requirements.txt
```

#### Running Flask Server:

```bash
python app.py
```

Your Flask server will start running on `http://localhost:1000`.

### 3. Frontend Setup (Node.js + Express)

#### Requirements:
- Node.js & npm

#### Install dependencies:

```bash
npm install
```

#### Running Node.js Server:

```bash
node server.js
```

Your Node.js server will be running on `http://localhost:3000`.

---

## 🖥️ How to Use

1. **Open the Web Interface**:
   - Navigate to `http://localhost:3000` in your browser.

2. **Log in to LeetCode**:
   - Open your browser's Developer Tools (`F12` or `Ctrl+Shift+I`).
   - Go to the **Application** tab and find cookies for `leetcode.com`.
   - Copy the entire cookie JSON data.

3. **Submit Cookie JSON**:
   - Paste the copied cookie JSON into the input field labeled **LeetCode Cookies (JSON)** on the web page.
   - Click **Start Solving Problems** to initiate the AI automation.

4. **Automation Starts**:
   - The AI agent will start solving problems on LeetCode.
   - You can view the progress in real-time on the same page.

---

## 💡 Project Flow

1. **Frontend**:
   - Collects LeetCode cookies (in JSON format) from the user.
   - Sends the cookies to the backend (`server.js`).

2. **Node.js Backend**:
   - Receives the cookies from the frontend and forwards them to the Flask server (`app.py`).
   
3. **Flask Backend**:
   - Uses Selenium WebDriver to automate the login process on LeetCode using the provided cookies.
   - Starts solving problems on LeetCode one by one, submitting solutions and checking test cases.

4. **Real-time Updates**:
   - The user can view the status of the automation in real-time on the frontend page.

---

## 📜 Project Structure

```
/leetcode-ai-agent
│
├── /frontend
│   ├── index.html        # HTML front-end
│   ├── app.js            # JavaScript for handling form submission and API requests
│   └── styles.css        # CSS for styling the page
│
├── /backend
│   ├── app.py            # Flask backend for handling automation
│   └── requirements.txt  # Python dependencies
│
├── /nodejs-server
│   ├── server.js         # Express.js server for relaying requests to Flask
└── README.md             # Project documentation
```

---

## 🛠️ Troubleshooting

If you encounter issues, make sure:
- The backend (`app.py`) is running on port 1000.
- The frontend (`server.js`) is running on port 3000.
- Cookies are correctly copied in JSON format and provided via the web interface.

---

## 🤝 Contributing

Feel free to fork this repository, create an issue, or submit a pull request if you'd like to contribute to the project!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

👨‍💻 Happy coding and automating! 🎉


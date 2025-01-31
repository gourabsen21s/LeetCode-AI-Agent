from flask import Flask, request, jsonify
from flask_cors import CORS
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = Flask(__name__)
CORS(app)

@app.route('/start', methods=['POST'])
def start_automation():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    try:
        chrome_options = Options()

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get('https://leetcode.com/accounts/login/')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_login"))
        )
        driver.find_element(By.ID, 'id_login').send_keys(username)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_password"))
        )
        driver.find_element(By.ID, 'id_password').send_keys(password)

        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']"))
            ).click()
        except Exception as e:
            print("Error clicking the checkbox:", e)
            return jsonify({"message": "Error clicking the checkbox. Please try again."}), 500

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Sign in"]'))
        ).click()

        time.sleep(5)

        if driver.current_url == 'https://leetcode.com/':
            return jsonify({"message": "Successfully logged in and starting automation."})
        else:
            return jsonify({"message": "Login failed. Please check your credentials."}), 400

    except Exception as e:
        print("Error during automation:", e)
        return jsonify({"message": "An error occurred during automation."}), 500
    finally:
        driver.quit()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=1000)

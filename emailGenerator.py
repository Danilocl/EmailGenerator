from flask import Flask, jsonify
import json
import random
import string

app = Flask(__name__)

def generate_random_username(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_email(domain):
    username = generate_random_username()
    return f"{username}@{domain}"

def generate_keyword_email(keyword, domain):
    username = keyword + '_' + generate_random_username(length=6)
    return f"{username}@{domain}"

ALLOWED_DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com"]

@app.route('/api/random_email/<domain>', methods=['GET'])
def get_random_email(domain):
    if domain not in ALLOWED_DOMAINS:
        message = {
            "message": "Please choose one of the following options :",
            "options": ALLOWED_DOMAINS
        }
        return json.dumps(message, ensure_ascii=False), 400
    email = generate_random_email(domain)
    return jsonify({"email": email})

@app.route('/api/keyword_email/<keyword>/<domain>', methods=['GET'])
def get_keyword_email(keyword, domain):
    if domain not in ALLOWED_DOMAINS:
        message = {
            "message": "Please choose one of the following options:",
            "options": ALLOWED_DOMAINS
        }
        return json.dumps(message, ensure_ascii=False), 400
    email = generate_keyword_email(keyword, domain)
    return jsonify({"email": email})

if __name__ == '__main__':
    app.run(debug=True)

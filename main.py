import requests
from database import init_db
from sql_solver import get_final_sql_query

def main():
    init_db()

    # Step 1: Generate Webhook
    payload = {
        "name": "John Doe",
        "regNo": "REG12347",
        "email": "john@example.com"
    }
    res = requests.post(
        "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON", 
        json=payload
    )
    res.raise_for_status()
    data = res.json()
    webhook_url = data["webhook"]
    token = data["accessToken"]

    # Step 2: Prepare SQL query
    final_query = get_final_sql_query()

    # Step 3: Submit Solution
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    body = {"finalQuery": final_query}
    response = requests.post(webhook_url, headers=headers, json=body)
    print("Submission Response:", response.status_code, response.text)

if __name__ == "__main__":
    main()
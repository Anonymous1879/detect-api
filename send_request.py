import requests

def main():
    url = "http://127.0.0.1:8000/api/detect/"
    headers = {"Content-Type": "application/json"}

    # Get user input
    text = input("Enter text to be analyzed: ")
    data = {"text": text}

    try:
        # Send POST request to Django API
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP error responses
        print("Response from API:", response.json())
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    main()

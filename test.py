import requests

URL = "http://127.0.0.1:5000/categorize"

def test_success():
    r = requests.post(URL, json={"title": "Organize Desk"})
    data = r.json()
    assert r.status_code == 200
    assert data["status"] == "success"
    assert "category" in data
    print("Success test passed")

def test_missing_title():
    r = requests.post(URL, json={})
    data = r.json()
    assert r.status_code == 400
    assert data["status"] == "error"
    print("Missing title test passed")

def main():
    r1 = requests.post(URL, json={"title": "Organize Desk"})
    print(r1.status_code)
    print(r1.json())

    r2 = requests.post(URL, json={})
    print(r2.status_code)
    print(r2.json())

if __name__ == "__main__":
    main()
    test_success()
    test_missing_title()
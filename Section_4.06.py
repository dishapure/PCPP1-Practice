import requests

# Base URL for testing (fake REST API)
BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

# 1. GET request - fetch data
def get_post(post_id):
    res = requests.get(f"{BASE_URL}/{post_id}")
    print("GET Status:", res.status_code)       # 200 means success
    print("GET Data:", res.json())               # Print JSON response

# 2. POST request - create new data
def create_post():
    data = {
        "title": "PCPP",
        "body": "REST client example",
        "userId": 1
    }
    res = requests.post(BASE_URL, json=data)
    print("POST Status:", res.status_code)      # 201 means created
    print("POST Response:", res.json())

# 3. PUT request - update existing data
def update_post(post_id):
    updated_data = {
        "id": post_id,
        "title": "PCPP Updated",
        "body": "Updated REST client",
        "userId": 1
    }
    res = requests.put(f"{BASE_URL}/{post_id}", json=updated_data)
    print("PUT Status:", res.status_code)       # 200 means OK
    print("PUT Response:", res.json())

# 4. DELETE request - remove data
def delete_post(post_id):
    res = requests.delete(f"{BASE_URL}/{post_id}")
    print("DELETE Status:", res.status_code)    # 200 or 204 means deleted

# Testing all methods:
if __name__ == "__main__":
    print("---- GET ----")
    get_post(1)

    print("\n---- POST ----")
    create_post()

    print("\n---- PUT ----")
    update_post(1)

    print("\n---- DELETE ----")
    delete_post(1)

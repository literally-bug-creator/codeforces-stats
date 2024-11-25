import requests


def get_user_submissions(handle):
    response = requests.get(f"https://codeforces.com/api/user.status?handle={handle}")
    if response.status_code == 200:
        return response.json()
    else:
        print("Пользователь не найден")
        return None

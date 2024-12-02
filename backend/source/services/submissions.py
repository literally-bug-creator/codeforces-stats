import requests
from datetime import datetime, timezone
from backend.source.models.submit import Submit
import aiohttp
import asyncio

def json_to_list(submissions_json):
    submissions = []
    for submission in submissions_json:
        if submission['verdict'] == "OK":
            submit_time = submission['creationTimeSeconds']
            submit_date = datetime.fromtimestamp(submit_time, timezone.utc).date()
            submit = Submit(
                time=submit_date,
                rating=submission['problem'].get('rating', None),
                tags=submission['problem']['tags']
            )

            submissions.append(submit)

    return submissions


async def get_user_submissions(nickname):
    url = f"https://codeforces.com/api/user.status?handle={nickname}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                submissions_json = await response.json()
                return json_to_list(submissions_json['result'])
            else:
                print("Пользователь не найден")
                return None

from datetime import datetime, timezone
from backend.source.models.Submit import Submit
import aiohttp


async def json_to_list(submissions_json):
    submissions = []
    for submission in submissions_json:
        verdict = "OK" if submission["verdict"] == "OK" else "NOT_OK"
        submit_time = submission['creationTimeSeconds']
        submit_date = datetime.fromtimestamp(submit_time, timezone.utc).date()
        submit = Submit(
            problemset_name=submission['problem']['problemsetName'],
            verdict = verdict,
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
                return await json_to_list(submissions_json['result'])
            else:
                print("Пользователь не найден")
                return None

from fastapi import FastAPI

app = FastAPI(title="Codeforces Statistic API")


@app.get()
async def get(): ...

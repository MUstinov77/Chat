from fastapi import FastAPI

from chat.api.chats import chat_router

app = FastAPI()
app.include_router(chat_router)

@app.get("/")
async def main():
    return {"message": "Hello World"}
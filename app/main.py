from fastapi import FastAPI


# entry point
app = FastAPI()

app.include_router(user_router)
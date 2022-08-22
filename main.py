import uvicorn
from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static/templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    n = 1
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json({'id': n, 'message': data.get('message')})
        n += 1


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)

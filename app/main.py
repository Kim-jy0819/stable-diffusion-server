from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request, Response
from fastapi.responses import HTMLResponse
import uvicorn
from models import StableDiffusion # , SM
import json

SD = StableDiffusion()
app = FastAPI()

@app.get('/ping')
async def ping():
    return 'Ping test success'   

@app.get('/txt2img')
async def inference(request: Request):
    global SD
    request_body = await request.body()
    body = eval(request_body)
    text = body['text']
    image = SD.txt2img(text)

    return # Response(content=image, media_type="image/png")

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8888, reload=True)
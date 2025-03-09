# pip install "fastapi[standard]"
from fastapi import FastAPI
from gpiozero import LED


app = FastAPI()
led = LED(13)


@app.post("/led/toggle")
def toggle_led(on: bool):
    if on:
        led.on()
    else:
        led.off()

    return {"status": on}

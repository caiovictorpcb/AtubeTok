import PySimpleGUI as sg
from TikTokApi import TikTokApi

def baixar(url, nomearquivo):
    api = TikTokApi.get_instance()
    video = api.get_video_by_url(video_url=url)
    with open(nomearquivo + ".mp4", "wb") as f:
        f.write(video)

layout = [
    [sg.Text("URL:"), sg.InputText()],
    [sg.Text("NOME ARQUIVO:"), sg.InputText()],
    [sg.Button("BAIXAR")]
    ]

window = sg.Window("AtubeTok", layout=layout, icon="xesquedele.ico")

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "BAIXAR" and values:
        baixar(url = values[0], nomearquivo=values[1])
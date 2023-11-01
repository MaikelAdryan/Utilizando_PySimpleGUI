import PySimpleGUI as sg

# sg.theme_previewer() # Exibe todos os temas do pysimplegui
sg.theme('DarkPurple2')
layout = [
  [sg.Text('Calcular horário de saída', text_color='white')],
  [sg.Button('Clique em mim')]
]

window = sg.Window('Minha Janela', layout)

while True:
  event, values = window.read()
  if event == sg.WINDOW_CLOSED:
    break
  if event == 'Clique em mim':
    sg.popup('Botão Clicado')

window.close()

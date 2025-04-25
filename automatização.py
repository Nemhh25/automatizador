import pyautogui
import time
import pandas
import keyboard

# pyautogui -> fazer automações com python
# pyautogui.click -> clicar em algum lugar
# pyautogui.write -> escrever algo
# pyautogui.press -> pressionar uma tecla
# pyautogui.hotkey -> pressionar várias teclas ao mesmo tempo 

pyautogui.PAUSE = 0.3  # Pausa de 0.3 segundos entre os coMOLO000251    Logitech    TETO0008014   Toshiba Televisao   14  800.0   192.0   nanmandos

# Passo 1: Entrar no sistema da empresa: https://dlp. hashtagtreinamentos.com/python/intensivao/login
# Passo 1.1: Abrir o navegador

pyautogui.press('win')  # Abre o menu iniciar

pyautogui.write('chrome')  # Escreve "chrome"

pyautogui.press('enter')  # Abre o navegador

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')  # Escreve o link

pyautogui.press('enter')  # Pressiona Enter para acessar o link


time.sleep(1)  # Espera 5 segundos para o site carregar


# Passo 2: Fazer login

pyautogui.click(x= 829, y = 408)  # Clica no campo de login

pyautogui.write("nelsondossantos739@gmail.com")  # Escreve o login

pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

pyautogui.write("123456")  # Escreve a senha

pyautogui.press('enter')  # Pressiona Enter para fazer login

time.sleep(2) # Espera 2 segundos para o sistema carregar


# Passo 3: Importar a base de dados
tabela = pandas.read_csv(r'C:\Users\Nelso\OneDrive\Documentos\PY\maratona\produtos.csv')  # Lê o arquivo CSV
print(tabela)  # Imprime a tabela no console

# Passo 4: Cadastrar um produto

for linha in tabela.index:  # Para cada linha da tabela
   


    codigo = tabela.loc[linha, "codigo"]  # Código do produto

    marca = tabela.loc[linha, "marca"]  # Marca do produto

    tipo = tabela.loc[linha, "tipo"]  # Tipo do produto

    categoria = tabela.loc[linha, "categoria"]  # Categoria do produto

    preco_unitario = tabela.loc[linha, "preco_unitario"]  # Preço unitário do produto

    custo = tabela.loc[linha, "custo"]  # Custo do produto

    obs = tabela.loc[linha, "obs"]  # Observação do produto

    pyautogui.click(x=777, y=294)  # Clica no campo do código do produto

    pyautogui.write(str(codigo))  # Escreve o código do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    pyautogui.write(str(marca))  # Escreve a marca do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    pyautogui.write(str(tipo))  # Escreve o tipo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    pyautogui.write(str(categoria))  # Escreve a categoria do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    pyautogui.write(str(preco_unitario))  # Escreve o preço unitário do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo

    pyautogui.write(str(custo))  # Escreve o custo do produto
    pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
            
    if str(obs).lower() != "nan":  # Verifica se o valor de obs é diferente de "NaN"
        pyautogui.write(str(obs))  # Escreve a observação do produto
        pyautogui.press('tab')  # Pressiona Tab para ir para o próximo campo
    else:
        pyautogui.press('tab')  # Apenas pula o campo se obs for "NaN"
    pyautogui.press('enter')  # Pressiona Enter para cadastrar o produto


  

    pyautogui.scroll(10000)  # Rola a tela para cima para cadastrar outros produtos




# Passo 5: Repetir para todos os produtos








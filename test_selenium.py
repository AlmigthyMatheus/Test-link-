import cv2
import pytesseract
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from unidecode import unidecode  # Biblioteca para normalizar texto

# Caminho do Tesseract (ajuste se necessário)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Mensagens que indicam que o código é inválido em vários idiomas
mensagens_invalidas = [
    "código de presente inválido",  # Português
    "gift code is invalid",  # Inglês
    "el código de regalo no es válido",  # Espanhol
    "le code cadeau est invalide",  # Francês
    "der geschenkkode ist ungültig",  # Alemão
    "il codice regalo non è valido",  # Italiano
    "de cadeaucode is ongeldig",  # Holandês
    "подарочный код недействителен",  # Russo
    "礼品码无效",  # Chinês (Simplificado)
    "ギフトコードは無効です"  # Japonês
]

# Normaliza as mensagens inválidas removendo acentos
mensagens_invalidas_normalizadas = [unidecode(mensagem.lower()) for mensagem in mensagens_invalidas]

# Caminho dos arquivos
caminho_arquivo = 'C:/Users/patat/Downloads/GeradorDeNitro-main/GeradorDeNitro-main/validar.txt'
caminho_saida = 'C:/Users/patat/Downloads/GeradorDeNitro-main/GeradorDeNitro-main/validos.txt'

# Limpa o arquivo de saída
with open(caminho_saida, 'w') as f:
    f.write("")

# Cria uma única instância do Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def verificar_link(link):
    """Verifica se o link é válido e retorna True se válido, False caso contrário."""
    try:
        driver.get(link)  # Acessa o link

        # Aguarda até que o conteúdo da página esteja presente
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Captura a tela da página
        driver.save_screenshot('screenshot.png')

        # Usa o OpenCV para carregar a imagem e o Tesseract para reconhecer texto
        img = cv2.imread('screenshot.png')
        text = pytesseract.image_to_string(img)

        # Normaliza o texto reconhecido
        text_normalizado = unidecode(text.lower())

        # Debug: Imprime o texto reconhecido
        print(f"Texto reconhecido: {text_normalizado}")

        # Verifica se qualquer mensagem inválida está presente no texto reconhecido
        is_valid = not any(mensagem in text_normalizado for mensagem in mensagens_invalidas_normalizadas)
        return link, is_valid

    except Exception as e:
        print(f"Erro ao acessar o link {link}: {e}")
        return link, False


# Lê os links do arquivo
with open(caminho_arquivo, 'r') as file:
    links = file.readlines()

# Verifica cada link
for link in links:
    link = link.strip()  # Remove espaços em branco
    print(f"Verificando o link: {link}")
    link, is_valid = verificar_link(link)

    if is_valid:
        with open(caminho_saida, 'a') as output_file:
            output_file.write(f"{link}\n")  # Escreve o link válido no arquivo
    else:
        print(f"Link inválido: {link}")

driver.quit()  # Fecha o navegador ao final

print("Verificação concluída. Links válidos foram salvos em 'validos.txt'.")

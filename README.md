Aqui está a versão atualizada do `README.md`, sem incluir o caminho do seu diretório pessoal:

---

# 🎁 Verificador de Códigos de Presente Discord Nitro

Este projeto é uma ferramenta automatizada desenvolvida em Python que verifica a validade de links de presentes do **Discord Nitro**. A aplicação acessa os links, captura o conteúdo da página e determina se o código é válido ou inválido com base nas mensagens exibidas.

## 🚀 Funcionalidades

- 🔍 **Verificação automática** de múltiplos links de Discord Nitro.
- 📸 **Captura de tela** das páginas acessadas e reconhecimento de texto usando OCR.
- 🌍 Suporte para **múltiplos idiomas** ao verificar mensagens de erro de códigos inválidos.
- 💾 **Salvamento automático** dos links válidos em um arquivo `.txt`.
- ♻️ Limpeza automática do arquivo de saída a cada execução.

## 🛠️ Tecnologias Usadas

- **Python**: Linguagem de programação usada para automação.
- **Selenium**: Para navegar e interagir com as páginas da web.
- **Tesseract OCR**: Para reconhecimento óptico de caracteres nas imagens das páginas.
- **OpenCV**: Biblioteca para captura e manipulação de imagens.
- **unidecode**: Para normalizar o texto, removendo acentuação e caracteres especiais.

## 🔧 Pré-requisitos

Antes de começar, certifique-se de ter os seguintes componentes instalados:

- 🐍 **Python 3.7+** instalado.
- 📥 **Tesseract OCR**:
   - Baixe e instale o [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
   - Adicione o caminho do Tesseract ao código (veja a seção [Configuração](#configuração-do-tesseract)).
- 🌐 **Google Chrome** e **ChromeDriver**:
   - Instale a versão correspondente do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## 🛠️ Instalação

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seuusuario/discord-nitro-verifier.git
   ```

2. **Instale as dependências**:

   Execute o comando para instalar as bibliotecas necessárias:

   ```bash
   pip install -r requirements.txt
   ```

   Ou instale manualmente:

   ```bash
   pip install selenium opencv-python pytesseract unidecode webdriver-manager
   ```

3. **Configuração do Tesseract**:

   - Instale o [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
   - No código, ajuste o caminho da instalação do Tesseract:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
     ```

## 📝 Uso

1. **Adicione os links para verificação** no arquivo `validar.txt`, que deve ser colocado na pasta onde você configurou o projeto.

2. **Execute o script**:

   Para iniciar a verificação, rode o seguinte comando:

   ```bash
   python main.py
   ```

3. **Resultados**:

   - O arquivo `validos.txt` será criado automaticamente na pasta do projeto e conterá todos os links válidos.
   - O progresso será exibido no console, indicando os links que foram considerados inválidos.

## ⚙️ Como Funciona

1. O Selenium abre os links do arquivo de entrada.
2. O OpenCV captura uma imagem da página acessada.
3. O Tesseract OCR extrai o texto da imagem.
4. O código compara o texto com uma lista de mensagens que indicam código inválido, em vários idiomas.
5. Se o código for considerado válido, o link é salvo no arquivo `validos.txt`.

## 📝 Exemplo de Código

Aqui está um exemplo simplificado da lógica principal:

```python
driver.get(link)
driver.save_screenshot('screenshot.png')
img = cv2.imread('screenshot.png')
text = pytesseract.image_to_string(img)
text_normalizado = unidecode(text.lower())

# Verifica se o link é inválido
if any(mensagem in text_normalizado for mensagem in mensagens_invalidas_normalizadas):
    print(f"Link inválido: {link}")
else:
    with open(caminho_saida, 'a') as output_file:
        output_file.write(f"{link}\n")
```

## 💡 Customizações e Melhorias

- **Performance**: Aumente a velocidade ajustando os tempos de espera ou otimizando a captura de telas.
- **Suporte a Novos Idiomas**: Adicione novas mensagens de código inválido em mais idiomas.
- **Interface Gráfica (GUI)**: Considere adicionar uma interface gráfica para facilitar o uso.

## ❗ Problemas Conhecidos

- O Selenium pode apresentar lentidão se abrir muitos links consecutivos. Para evitar isso, execute o script com lotes menores de links ou ajuste o tempo de espera entre verificações.

## 🛠️ Contribuições

Contribuições são sempre bem-vindas! Abra *issues* para relatar problemas ou envie *pull requests* para melhorias e novas funcionalidades.

---

Esse `README.md` agora não contém referências diretas ao seu diretório pessoal e ainda mantém um formato claro e bem organizado.

from bs4 import BeautifulSoup
import requests
import os
from zipfile import ZipFile

#Link do Site para extrair os PDF's
linkURL = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

#Funcao para baixar os pdfs
def download_pdf(filename_download, link_url):
    #Requisicao
    request = requests.get(link_url)
    #Abro o arquivo para baixar os PDFs
    with open(filename_download, 'wb') as f:
        f.write(request.content)

#Requisicao GET
response = requests.get(linkURL)
soup = BeautifulSoup(response.text, 'html.parser')

#Lista dos links dos PDFS
links_pdf = []
#Buscar os links da página
for link in soup.find_all('a'):
    href = link.get('href')
    #Adicionar a lista apenas os links de Anexo I e II
    if href and ('Anexo I' in link.text or 'Anexo II' in link.text) and href.endswith('.pdf'):
        links_pdf.append(href)

#Criando o repositorio
os.makedirs('anexos_pdfs', exist_ok=True)

#Baixar os arquivos no repositorio
for link in links_pdf:
    #Separando o nome do arquivo do link
    filename = os.path.join('anexos_pdfs', link.split('/')[-1])
    download_pdf(filename, link)

#Zipando os arquivos baixados
with ZipFile('anexos_pdfs.zip', 'w') as zipf:
    for pdf_file in os.listdir('anexos_pdfs'):
        zipf.write(os.path.join('anexos_pdfs', pdf_file), pdf_file)

print('Arquivos baixados e zipados com sucesso!')

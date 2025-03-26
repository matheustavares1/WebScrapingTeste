# Web Scraping - Atualização do Rol de Procedimentos

Este projeto realiza o **web scraping** do site da ANS (Agência Nacional de Saúde Suplementar) para baixar os **Anexos I e II** em formato **PDF**, compactá-los em um arquivo ZIP e armazená-los localmente.

## Funcionalidades

- Acessa o site: [Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
- Realiza o download dos **Anexos I e II** em PDF.
- Compacta os arquivos PDF baixados em um arquivo **ZIP**.

## Tecnologias Utilizadas

- **Python**
- **BeautifulSoup** (para fazer o parsing do HTML e extrair links)
- **Requests** (para fazer requisições HTTP)
- **Zipfile** (para compactar os arquivos em formato ZIP)

## Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o código, certifique-se de ter o **Python** instalado. Você pode baixar a versão mais recente do Python em: [python.org](https://www.python.org/downloads/).

Além disso, instale as dependências necessárias:

```bash
pip install requests beautifulsoup4


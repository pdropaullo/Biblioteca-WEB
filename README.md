# Biblioteca WEB

Este é um projeto web desenvolvido em Python com o framework Django para fazer o gerenciamento de uma biblioteca.  
Foi desenvolvido durante a disciplina de Desenvolvimento para Web, sob a orientação do Professor Wildson Caio Felipe.   

## Funcionalidades

- Cadastrar, Pesquisar, Editar e Excluir Mídias

## Requisitos

- Python
- Django

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/pdropaullo/Biblioteca-WEB.git
```
2. Acesse o diretório do projeto:
```bash
cd Biblioteca-WEB
```
3. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
```
```bash
.\venv\Scripts\activate
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```
5. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```
6. Inicie o servidor:
```bash
python manage.py runserver
```
7. Acesse o aplicativo no seu navegador em:
```bash
http://127.0.0.1:8000/
```

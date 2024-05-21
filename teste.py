import base64

with open('amazon.csv','rb') as file:
    file_content = file.read()

encoded_content = base64.b64decode(file_content)

data = {
    'message': 'Adicionando um novo arquivo',
    'content': encoded_content.decode("utf-8")
}
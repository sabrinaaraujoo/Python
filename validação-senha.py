senhaCadastrada = "aluno"
usuario = "jean"

login = input("Escolha um nome de login: ") #lendo no formato str
while login != usuario:
    login = input("Seu usuário é inválido. Digite novamente: ")
        
senha = input("Escolha uma senha: ") #lendo no formato str
while senha != senhaCadastrada:
    senha = input("Sua senha é inválida. Digite novamente: ")
    
print("Login realizado com sucesso!")

class exercicios:
    def __init__(self, nome, idade, sexo, status, alunos, notas):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.status = status
        self.alunos = alunos
        self.notas = notas
        
    def ex1(self):
        print("Nome: ", self.nome, "\nIdade: ", self.idade, "\nSexo: ", self.sexo, "\nStatus: ", self.status)
    
    def ex2(self):
        alunos = ["Gabriel", ""]
        
usuário = exercicios("Gabriel", 18, "M", True)
usuário.ex1
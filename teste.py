import sqlite3

def conectar():
    return sqlite3.connect('escola.db')

def criar_tabela():
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        curso TEXT)
    ''')

    conexão.commit()
    conexão.close()

def inserir(nome, idade, curso):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('INSERT INTO alunos(nome, idade, curso) VALUES(?,?,?)', (nome, idade, curso))
    conexão.commit()
    conexão.close()

def listar():
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('SELECT * FROM alunos')
    for linha in cursor.fetchall():
        print(linha)
    conexão.close()

def atualizar(id, nome, idade, curso):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('UPDATE alunos SET nome=?, idade=?, curso=? Where id=?',  (nome, idade, curso, id))
    conexão.commit()
    conexão.close()

def excluir(id):
    conexão = conectar()
    cursor = conexão.cursor()
    cursor.execute('DELETE FROM alunos WHERE id=?', (id,))
    conexão.commit()
    conexão.close()

criar_tabela()

while True:
    print('\n------MENU------')
    print('1 - Inserir aluno')
    print('2 - Listar alunos')
    print('3 - Atualizar')
    print('4 - Excluir aluno')
    print('0 - Sair')

    opção = input('Faça sua escolha: ')

    if opção == '1':
        nome = input('Nome: ')
        idade = int(input('Idade: '))
        curso = input('Curso: ')
        inserir(nome, idade, curso)

    elif opção == '2':
        listar()
    elif opção == '3':
        id = int(input('ID do aluno: '))
        nome = input('Novo nome: ')
        idade = int(input('Nova idade'))
        curso = input('Novo curso: ')
        atualizar(id, nome, idade, curso)
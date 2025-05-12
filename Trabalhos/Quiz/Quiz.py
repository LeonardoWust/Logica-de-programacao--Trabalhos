print("Bem-vindo ao teste de afinidade com áreas de TI!!!")

dev_software = 0
area_produtos = 0
area_qualidade = 0

def int_validador(resposta):
    while True:
        valor = input(resposta)
        try:
            valor = int(valor)
            if 1 <= valor <=5:
                return valor
            else:
                print("Este numero não está entre 1 e 5")
        except ValueError:
            print("O valor deve ser numero inteiro")

perguntas_dev_software = [
    "Gosto de programar e resolver problemas com código.",
    "Tenho interesse em criar aplicativos e sites.",
    "Gosto de aprender novas linguagens de programação.",
    "Prefiro trabalhar com lógica e estruturação de código.",
    "Tenho paciência para depurar erros e otimizar código."
]

perguntas_area_produtos = [
    "Gosto de pensar na experiência do usuário ao usar um sistema.",
    "Tenho interesse em pesquisa de mercado e comportamento do usuário.",
    "Me interesso por criar soluções inovadoras e intuitivas.",
    "Gosto de trabalhar com design, wireframes ou prototipagem.",
    "Quero entender e definir estratégias para melhorar produtos digitais."
]

perguntas_area_qualidade = [
    "Gosto de testar e garantir que sistemas funcionem corretamente.",
    "Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos.",
    "Acredito que testes automatizados ajudam a evitar falhas em sistemas.",
    "Gosto de seguir padrões e documentar processos para garantir qualidade.",
    "Quero trabalhar garantindo que um software funcione bem para todos os usuários."
]

# Coletar respostas para cada área
print("Responda às perguntas sobre Desenvolvimento de Software:")
d1 = int_validador(perguntas_dev_software[0] + "(1 a 5): ")
d2 = int_validador(perguntas_dev_software[1] + "(1 a 5): ")
d3 = int_validador(perguntas_dev_software[2] + "(1 a 5): ")
d4 = int_validador(perguntas_dev_software[3] + "(1 a 5): ")
d5 = int_validador(perguntas_dev_software[4] + "(1 a 5): ")
dev_software = d1 + d2 + d3 + d4 + d5

print("Responda às perguntas sobre Área de Produtos:")
p1 = int_validador(perguntas_area_produtos[0] + "(1 a 5): ")
p2 = int_validador(perguntas_area_produtos[1] + "(1 a 5): ")
p3 = int_validador(perguntas_area_produtos[2] + "(1 a 5): ")
p4 = int_validador(perguntas_area_produtos[3] + "(1 a 5): ")
p5 = int_validador(perguntas_area_produtos[4] + "(1 a 5): ")
area_produtos = p1 + p2 + p3 + p4 + p5

print("Responda às perguntas sobre Área de Qualidade:")
q1 = int_validador(perguntas_area_qualidade[0] + "(1 a 5): ")
q2 = int_validador(perguntas_area_qualidade[1] + "(1 a 5): ")
q3 = int_validador(perguntas_area_qualidade[2] + "(1 a 5): ")
q4 = int_validador(perguntas_area_qualidade[3] + "(1 a 5): ")
q5 = int_validador(perguntas_area_qualidade[4] + "(1 a 5): ")
area_qualidade = q1 + q2 + q3 + q4 + q5

# Determinar a maior Pontuação
maior_pontuacao = max(dev_software, area_produtos, area_qualidade)
print("Resultados")
print("Desenvolvimento de Software", dev_software, "pontos")
print("Área de Produtos", area_produtos, "pontos")
print("Área de Qualidade", area_qualidade, "pontos")

if dev_software == maior_pontuacao and area_produtos == maior_pontuacao and area_qualidade == maior_pontuacao:
    print("Áreas recomendadas: Desenvolvimento de Software, Área de Produtos e Área de Qualidade")
elif dev_software == maior_pontuacao and area_produtos == maior_pontuacao:
    print("Áreas recomendadas: Desenvolvimento de Software e Área de Produtos")
elif dev_software == maior_pontuacao and area_qualidade == maior_pontuacao:
    print("Áreas recomendadas: Desenvolvimento de Software e Área de Qualidade")
elif area_produtos == maior_pontuacao and area_qualidade == maior_pontuacao:
    print("Áreas recomendadas: Área de Produtos e Área de Qualidade")
elif dev_software == maior_pontuacao:
    print("Áreas recomendada: Desenvolvimento de Software")
elif area_produtos == maior_pontuacao:
    print("Áreas recomendada: Área de Produtos")
elif area_qualidade == maior_pontuacao:
    print("Áreas recomendada: Área de Qualidade")

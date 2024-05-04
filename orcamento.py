projeto = input("Digite o nome do seu projeto: ")
hora_prevista = input("Digite a quantidade de horas prevista: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo de conclusão do projeto: ")
valor_total = int(float(valor_hora)) * int(float(hora_prevista))

from fpdf import FPDF
pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial") 
pdf.image("boleto.png", x=0, y=0)

pdf.text(115, 130, projeto)
pdf.text(115, 144, hora_prevista)
pdf.text(115, 157, valor_hora)
pdf.text(115, 170, prazo)
pdf.text(115, 182, str(valor_total))




pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")
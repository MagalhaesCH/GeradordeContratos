import json

def carregar_dados(arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)
    return dados

def carregar_template(arquivo_template):
    with open(arquivo_template, 'r') as f:
        template = f.read()
    return template

def gerar_contrato(template, dados):
    contrato = template.format(**dados)
    return contrato

def salvar_contrato(contrato, arquivo_saida):
    with open(arquivo_saida, 'w') as f:
        f.write(contrato)

def main():
    dados = carregar_dados('dados_contrato.json')
    template = carregar_template('minuta_contrato.txt')
    contrato = gerar_contrato(template, dados)
    salvar_contrato(contrato, 'contrato_final.txt')
    print("Contrato gerado com sucesso!")

if __name__ == "__main__":
    main()

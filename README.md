t# GeradordeContratos
Gerador automático de contratos a partir  de uma minuta padrão.


Vamos criar um programa em Python que gera automaticamente contratos a partir de uma minuta. Esse programa irá ler um template de contrato e substituirá os placeholders com informações fornecidas pelo usuário ou armazenadas em um arquivo JSON.

#### Estrutura do Projeto

1. **Minuta do Contrato (Template)**
2. **Arquivo de Configuração (JSON)**
3. **Programa Principal (Python)**

#### 1. Minuta do Contrato

Primeiro, precisamos de um arquivo de template para o contrato. Esse arquivo conterá placeholders no formato `{variavel}` que serão substituídos pelo nosso programa.

**minuta_contrato.txt**
```
CONTRATO DE PRESTAÇÃO DE SERVIÇOS

CONTRATANTE: {contratante}, com endereço em {endereco_contratante}, inscrito no CNPJ sob o nº {cnpj_contratante}.

CONTRATADO: {contratado}, com endereço em {endereco_contratado}, inscrito no CPF sob o nº {cpf_contratado}.

As partes acima identificadas têm entre si justo e acordado o presente Contrato de Prestação de Serviços, que se regerá pelas cláusulas seguintes e pelas condições descritas no presente.

CLÁUSULA PRIMEIRA – DO OBJETO DO CONTRATO
O presente contrato tem como objeto a prestação dos serviços de {descricao_servicos}.

CLÁUSULA SEGUNDA – DO PRAZO
O prazo para a prestação dos serviços será de {prazo_servicos}, com início em {data_inicio} e término em {data_termino}.

CLÁUSULA TERCEIRA – DO PREÇO E DAS CONDIÇÕES DE PAGAMENTO
Pelos serviços prestados, a CONTRATANTE pagará ao CONTRATADO a quantia de {valor_servicos}, em {forma_pagamento}.

E, por estarem assim justos e contratados, assinam o presente contrato em duas vias de igual teor.

_________________________________________
CONTRATANTE: {contratante}

_________________________________________
CONTRATADO: {contratado}
```

#### 2. Arquivo de Configuração

Em seguida, criaremos um arquivo JSON que conterá os dados a serem substituídos na minuta.

**dados_contrato.json**
```json
{
    "contratante": "Empresa XYZ Ltda",
    "endereco_contratante": "Rua das Flores, 123, São Paulo, SP",
    "cnpj_contratante": "12.345.678/0001-99",
    "contratado": "João da Silva",
    "endereco_contratado": "Av. Brasil, 456, Rio de Janeiro, RJ",
    "cpf_contratado": "123.456.789-00",
    "descricao_servicos": "consultoria em tecnologia da informação",
    "prazo_servicos": "6 meses",
    "data_inicio": "01/06/2024",
    "data_termino": "30/11/2024",
    "valor_servicos": "R$ 50.000,00",
    "forma_pagamento": "em parcelas mensais"
}
```
Arquivo carregado no projeto
### Explicação do Código

1. **carregar_dados**: Função que lê os dados do arquivo JSON e retorna um dicionário com os valores.
2. **carregar_template**: Função que lê o template do contrato a partir de um arquivo de texto.
3. **gerar_contrato**: Função que substitui os placeholders no template com os dados fornecidos.
4. **salvar_contrato**: Função que salva o contrato gerado em um arquivo de saída.
5. **main**: Função principal que coordena a execução das outras funções.

### Execução do Programa

Para executar o programa, basta garantir que os arquivos `dados_contrato.json`, `minuta_contrato.txt`, e `gerador_contratos.py` estejam no mesmo diretório e executar o script Python:

Após a execução, um arquivo chamado `contrato_final.txt` será gerado com o contrato completo.

### Conclusão

Este gerador automático de contratos é uma ferramenta simples mas poderosa para automatizar a criação de contratos a partir de uma minuta. Pode ser expandido para incluir mais funcionalidades, como a leitura de múltiplos templates, entrada de dados via interface gráfica ou linha de comando, e validações adicionais para os dados de entrada.

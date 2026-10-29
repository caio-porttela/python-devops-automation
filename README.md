# Python DevOps Automation

Projeto prático de automação com Python, desenvolvido para aplicar conceitos 
fundamentais de **DevOps, monitoramento, análise de logs e testes automatizados**.

O objetivo é criar uma ferramenta simples para inspecionar o ambiente de execução, 
acompanhar a utilização de disco e identificar eventos relevantes em arquivos de log.

## Objetivos

- Consultar informações do ambiente de execução.
- Monitorar o uso do espaço em disco.
- Gerar registros de monitoramento com níveis de severidade.
- Analisar logs e identificar mensagens de erro e aviso.
- Validar o comportamento da aplicação com testes automatizados.

## Tecnologias

- **Python 3** — lógica e automação.
- **psutil** — biblioteca incluída nas dependências do projeto para tarefas de 
monitoramento.
- **pytest** — execução de testes automatizados.
- **logging** — registro de eventos da aplicação.
- **Git e GitHub** — versionamento e documentação.

## Funcionalidades

### 1. Verificação do ambiente

O script `main.py` apresenta informações sobre o sistema operacional, a versão do 
Python, o diretório atual e a data e hora da execução.

### 2. Monitoramento de disco

O programa verifica o espaço total, utilizado e livre em disco.

- Utilização abaixo de 80%: registra uma mensagem informativa (`INFO`).
- Utilização igual ou acima de 80%: gera um alerta (`WARNING`).

O limite pode ser ajustado por parâmetro na função de monitoramento.

### 3. Registro de eventos

A aplicação utiliza o módulo `logging` para registrar eventos com data, hora e nível 
de severidade.

Os registros são gravados em `logs/monitoramento.log`. Esse arquivo é gerado durante a 
execução e excluído do versionamento pelo `.gitignore`.

### 4. Análise de logs

O script `analisar_logs.py` lê um arquivo de log e contabiliza mensagens classificadas 
como `INFO`, `WARNING` e `ERROR`.

As mensagens de erro encontradas são exibidas no terminal. Também há tratamento para 
arquivos inexistentes.

### 5. Testes automatizados

Os testes utilizam `pytest` para validar a análise de logs e o comportamento do 
monitoramento de disco em diferentes cenários, incluindo a utilização exatamente no 
limite de alerta.

**Status atual:** 5 testes automatizados passaram.

## Estrutura do projeto

```text
python-devops-automation/
├── logs/
│   └── app.log
├── tests/
│   ├── test_analisar_logs.py
│   └── test_monitoramento_disco.py
├── .gitignore
├── analisar_logs.py
├── main.py
├── README.md
└── requirements.txt
```

O arquivo `logs/monitoramento.log` é criado durante a execução e não precisa ser 
versionado.

## Como executar

### 1. Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 3. Executar o monitoramento

```bash
python main.py
```

### 4. Analisar os logs

```bash
python analisar_logs.py
```

Para analisar outro arquivo:

```bash
python analisar_logs.py caminho/do/arquivo.log
```

### 5. Executar os testes

```bash
python -m pytest -v
```

## Aprendizados

Este projeto faz parte da minha jornada de estudos em **DevOps, Cloud Engineering e 
Cloud Security**.

Durante o desenvolvimento, são praticados conceitos de automação com Python, 
monitoramento de recursos, registro de eventos, tratamento de erros, testes 
automatizados e controle de versão.

A proposta é evoluir a ferramenta gradualmente, priorizando fundamentos técnicos, 
código testável e documentação clara.

## Próximas melhorias

- Expandir os testes automatizados.
- Melhorar os relatórios de monitoramento.
- Integrar verificações adicionais do ambiente.
- Explorar pipelines de integração contínua com GitHub Actions.

---

**Status:** projeto de aprendizado em desenvolvimento.

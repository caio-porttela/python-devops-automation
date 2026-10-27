# Python DevOps Automation

Projeto prático desenvolvido para estudar Python aplicado a tarefas de automação, monitoramento e análise de logs.

## Objetivos

- Consultar informações do ambiente de execução.
- Monitorar a utilização do espaço em disco.
- Analisar arquivos de log.
- Identificar mensagens de erro e aviso.
- Validar o comportamento do código com testes automatizados.

## Tecnologias

- Python
- psutil
- pytest
- Git e GitHub

## Funcionalidades

### 1. Verificação do ambiente

O script `main.py` apresenta informações sobre o sistema operacional, a versão do Python, o diretório atual e a data e hora da execução.

Também verifica o espaço em disco e apresenta um alerta quando a utilização atinge 90%.

### 2. Análise de logs

O script `analisar_logs.py` lê um arquivo de log e contabiliza mensagens classificadas como `INFO`, `WARNING` e `ERROR`.

As mensagens de erro encontradas são exibidas no terminal.

### 3. Testes automatizados

O projeto utiliza pytest para verificar a contagem das mensagens de log e o comportamento esperado quando o arquivo não existe.

## Estrutura do projeto

```text
python-devops-automation/
├── logs/
│   └── app.log
├── tests/
│   └── test_analisar_logs.py
├── .gitignore
├── analisar_logs.py
├── main.py
├── README.md
└── requirements.txt
```

## Como executar

### 1. Criar e ativar um ambiente virtual

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

### 5. Executar os testes

```bash
python -m pytest -v
```

## Aprendizados

Este projeto faz parte da minha jornada de estudos em DevOps e Cloud Engineering, com foco em automação, monitoramento, análise de logs e testes automatizados.

O objetivo é evoluir gradualmente a ferramenta e documentar os conhecimentos adquiridos durante o desenvolvimento.

---

**Status:** projeto de aprendizado em desenvolvimento.
import platform
import os
import shutil
import logging
from datetime import datetime


LIMITE_DISCO = 80
DIRETORIO_LOGS = "logs"
ARQUIVO_LOG = os.path.join(DIRETORIO_LOGS, "monitoramento.log")


os.makedirs(DIRETORIO_LOGS, exist_ok=True)

logging.basicConfig(
    filename=ARQUIVO_LOG,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True,
)


def verificar_ambiente():
    print("=" * 45)
    print("       PYTHON DEVOPS AUTOMATION")
    print("=" * 45)
    print(f"Sistema operacional: {platform.system()}")
    print(f"Versão do sistema: {platform.release()}")
    print(f"Versão do Python: {platform.python_version()}")
    print(f"Diretório atual: {os.getcwd()}")
    print(f"Data e hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")


def verificar_disco(limite_alerta=LIMITE_DISCO):
    caminho = os.path.abspath(os.sep)
    total, usado, livre = shutil.disk_usage(caminho)

    total_gb = total / (1024 ** 3)
    usado_gb = usado / (1024 ** 3)
    livre_gb = livre / (1024 ** 3)
    percentual_usado = (usado / total) * 100

    print("\n--- MONITORAMENTO DE DISCO ---")
    print(f"Espaço total: {total_gb:.2f} GB")
    print(f"Espaço utilizado: {usado_gb:.2f} GB")
    print(f"Espaço livre: {livre_gb:.2f} GB")
    print(f"Utilização: {percentual_usado:.1f}%")
    print(f"Limite de alerta: {limite_alerta}%")

    if percentual_usado >= limite_alerta:
        mensagem = (
            f"Utilização do disco atingiu o limite: "
            f"{percentual_usado:.1f}%"
        )
        print(f"ALERTA: {mensagem}")
        logging.warning(mensagem)
    else:
        mensagem = f"Disco com utilização de {percentual_usado:.1f}%"
        print("STATUS: utilização de disco dentro do limite.")
        logging.info(mensagem)

    return percentual_usado


def main():
    verificar_ambiente()
    verificar_disco()
    print(f"\nRegistro salvo em: {ARQUIVO_LOG}")
    print("\nVerificação concluída!")


if __name__ == "__main__":
    main()

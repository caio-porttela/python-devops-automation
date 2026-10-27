import platform
import os
import shutil
from datetime import datetime


def verificar_ambiente():
    print("=" * 45)
    print("       PYTHON DEVOPS AUTOMATION")
    print("=" * 45)

    print(f"Sistema operacional: {platform.system()}")
    print(f"Versão do sistema: {platform.release()}")
    print(f"Versão do Python: {platform.python_version()}")
    print(f"Diretório atual: {os.getcwd()}")
    print(f"Data e hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")


def verificar_disco():
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

    if percentual_usado >= 90:
        print("ALERTA: utilização de disco igual ou superior a 90%!")
    else:
        print("STATUS: utilização de disco abaixo de 90%.")


def main():
    verificar_ambiente()
    verificar_disco()
    print("\nVerificação concluída!")


if __name__ == "__main__":
    main()
from pathlib import Path


def analisar_logs(caminho="logs/app.log"):
    arquivo = Path(caminho)

    if not arquivo.exists():
        print("ERRO: arquivo de log não encontrado.")
        return

    linhas = arquivo.read_text(encoding="utf-8").splitlines()

    erros = []
    avisos = 0
    informacoes = 0

    for linha in linhas:
        if "ERROR" in linha:
            erros.append(linha)
        elif "WARNING" in linha:
            avisos += 1
        elif "INFO" in linha:
            informacoes += 1

    print("=" * 45)
    print("         ANALISADOR DE LOGS")
    print("=" * 45)
    print(f"Total de linhas: {len(linhas)}")
    print(f"Informações (INFO): {informacoes}")
    print(f"Avisos (WARNING): {avisos}")
    print(f"Erros (ERROR): {len(erros)}")

    if erros:
        print("\n--- ERROS ENCONTRADOS ---")
        for erro in erros:
            print(erro)
    else:
        print("\nNenhum erro encontrado.")

    print("\nAnálise concluída!")


if __name__ == "__main__":
    analisar_logs()
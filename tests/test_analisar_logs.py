from analisar_logs import analisar_logs


def test_analisar_logs_identifica_erros(tmp_path, capsys):
    arquivo = tmp_path / "app.log"

    arquivo.write_text(
        "INFO Aplicação iniciada\n"
        "ERROR Falha no banco de dados\n"
        "WARNING Tempo de resposta elevado\n"
        "ERROR Falha na requisição\n",
        encoding="utf-8",
    )

    analisar_logs(arquivo)

    resultado = capsys.readouterr().out

    assert "Total de linhas: 4" in resultado
    assert "Informações (INFO): 1" in resultado
    assert "Avisos (WARNING): 1" in resultado
    assert "Erros (ERROR): 2" in resultado
    assert "ERROR Falha no banco de dados" in resultado


def test_analisar_logs_arquivo_inexistente(tmp_path, capsys):
    arquivo = tmp_path / "inexistente.log"

    analisar_logs(arquivo)

    resultado = capsys.readouterr().out

    assert "arquivo de log não encontrado" in resultado
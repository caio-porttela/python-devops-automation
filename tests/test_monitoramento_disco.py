import main


def test_disco_abaixo_do_limite(monkeypatch, capsys):
    monkeypatch.setattr(
        main.shutil,
        "disk_usage",
        lambda caminho: (100, 26, 74)
    )

    percentual = main.verificar_disco()

    saida = capsys.readouterr().out

    assert percentual == 26
    assert "dentro do limite" in saida


def test_disco_acima_do_limite(monkeypatch, capsys):
    monkeypatch.setattr(
        main.shutil,
        "disk_usage",
        lambda caminho: (100, 90, 10)
    )

    percentual = main.verificar_disco()

    saida = capsys.readouterr().out

    assert percentual == 90
    assert "ALERTA" in saida


def test_disco_exatamente_no_limite(monkeypatch, capsys):
    monkeypatch.setattr(
        main.shutil,
        "disk_usage",
        lambda caminho: (100, 80, 20)
    )

    percentual = main.verificar_disco()

    saida = capsys.readouterr().out

    assert percentual == 80
    assert "ALERTA" in saida

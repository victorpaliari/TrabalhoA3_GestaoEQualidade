import sys
import pathlib

SRC = pathlib.Path(__file__).resolve().parents[1] / "hamburgueria" / "src"
sys.path.append(str(SRC))

import main as app  # noqa: E402


def test_calcular_total_carrinho_vazio():
    assert app.calcular_total([]) == 0.0


def test_calcular_total_itens_simples():
    cart = [(1, 2), (4, 3)]  # 2x HB (2*12) + 3x Batata (3*8)
    assert app.calcular_total(cart) == 48.0


def test_resumo_por_item_agrupa_repetidos():
    cart = [(1, 1), (1, 2), (5, 1)]
    resumo = app.resumo_por_item(cart)
    assert resumo[1]["qtd"] == 3
    assert resumo[5]["qtd"] == 1
    assert resumo[1]["subtotal"] == 3 * app.MENU[1]["price"]

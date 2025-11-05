from typing import Dict, List, Tuple

MENU: Dict[int, Dict[str, float]] = {
    1: {"name": "Hambúrguer Simples", "price": 12.0},
    2: {"name": "Cheeseburguer", "price": 14.0},
    3: {"name": "X-Bacon", "price": 16.0},
    4: {"name": "Batata Frita", "price": 8.0},
    5: {"name": "Refrigerante", "price": 6.0},
}

Cart = List[Tuple[int, int]]  # (id_item, quantidade)


def mostrar_cardapio() -> None:
    print("Bem-vindo à Hamburgueria!")
    print("CARDÁPIO:")
    for i in sorted(MENU.keys()):
        item = MENU[i]
        print(f"{i} - {item['name']} - R${item['price']:.2f}")
    print("999 - Finalizar pedido")


def ler_opcao() -> int:
    try:
        return int(input("Digite o número do item (999 para sair): "))
    except ValueError:
        print("Entrada inválida.")
        return -1


def ler_quantidade() -> int:
    try:
        q = int(input("Quantidade: "))
        return q
    except ValueError:
        print("Quantidade inválida.")
        return -1


def adicionar_ao_carrinho(cart: Cart, item_id: int, qtd: int) -> None:
    cart.append((item_id, qtd))


def calcular_total(cart: Cart) -> float:
    total = 0.0
    for item_id, qtd in cart:
        total += MENU[item_id]["price"] * qtd
    return total


def resumo_por_item(cart: Cart) -> Dict[int, Dict[str, float]]:
    """Consolida quantidades e subtotais por item."""
    resumo: Dict[int, Dict[str, float]] = {}
    for item_id, qtd in cart:
        if item_id not in resumo:
            resumo[item_id] = {"qtd": 0, "subtotal": 0.0}
        resumo[item_id]["qtd"] += qtd
        resumo[item_id]["subtotal"] += MENU[item_id]["price"] * qtd
    return resumo


def main() -> None:
    cart: Cart = []
    mostrar_cardapio()

    while True:
        opcao = ler_opcao()
        if opcao == 999:
            print("Finalizando pedido...")
            break
        if opcao not in MENU:
            print("Item inválido.")
            continue

        qtd = ler_quantidade()
        if qtd <= 0:
            print("Quantidade deve ser maior que zero.")
            continue

        adicionar_ao_carrinho(cart, opcao, qtd)
        print(f"✓ Adicionado: {qtd}x {MENU[opcao]['name']}")

    print("\nResumo do pedido:")
    resumo = resumo_por_item(cart)
    for item_id in sorted(resumo.keys()):
        name = MENU[item_id]["name"]
        qtd = int(resumo[item_id]["qtd"])
        subtotal = resumo[item_id]["subtotal"]
        print(f"{name}: {qtd} - R$ {subtotal:.2f}")

    total = calcular_total(cart)
    print(f"TOTAL: R$ {total:.2f}")

    try:
        p = float(input("Valor pago: R$ "))
        if p >= total:
            print(f"Troco: R$ {p - total:.2f}")
        else:
            print("Valor insuficiente. Pedido cancelado.")
    except ValueError:
        print("Valor pago inválido. Pedido cancelado.")


if __name__ == "__main__":
    main()

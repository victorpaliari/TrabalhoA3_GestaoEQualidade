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
    print("🍔 Bem-vindo à Hamburgueria!")
    print("\nCARDÁPIO:")
    for i in sorted(MENU.keys()):
        item = MENU[i]
        print(f"{i} - {item['name']} - R${item['price']:.2f}")
    print("999 - Finalizar pedido")


def ler_opcao() -> int:
    try:
        return int(input("\nDigite o número do item (999 para sair): "))
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número do cardápio.")
        return -1


def ler_quantidade() -> int:
    try:
        q = int(input("Quantidade: "))
        if q <= 0:
            print("⚠️ A quantidade deve ser maior que zero.")
            return -1
        return q
    except ValueError:
        print("⚠️ Quantidade inválida.")
        return -1


def adicionar_ao_carrinho(cart: Cart, item_id: int, qtd: int) -> None:
    cart.append((item_id, qtd))
    print(f"✅ Adicionado: {qtd}x {MENU[item_id]['name']}")


def calcular_total(cart: Cart) -> float:
    return sum(MENU[item_id]["price"] * qtd for item_id, qtd in cart)


def resumo_por_item(cart: Cart) -> Dict[int, Dict[str, float]]:
    resumo: Dict[int, Dict[str, float]] = {}
    for item_id, qtd in cart:
        if item_id not in resumo:
            resumo[item_id] = {"qtd": 0, "subtotal": 0.0}
        resumo[item_id]["qtd"] += qtd
        resumo[item_id]["subtotal"] += MENU[item_id]["price"] * qtd
    return resumo


def confirmar_finalizacao() -> bool:
    resposta = input("Deseja realmente finalizar o pedido? (s/n): ").strip().lower()
    return resposta == "s"


def main() -> None:
    cart: Cart = []
    mostrar_cardapio()

    while True:
        opcao = ler_opcao()
        if opcao == 999:
            if confirmar_finalizacao():
                print("🧾 Finalizando pedido...")
                break
            else:
                continue

        if opcao not in MENU:
            print("⚠️ Item inválido. Escolha um número do cardápio.")
            continue

        qtd = ler_quantidade()
        if qtd <= 0:
            continue

        adicionar_ao_carrinho(cart, opcao, qtd)

    if not cart:
        print("\nNenhum item foi adicionado ao pedido. Até logo! 👋")
        return

    print("\nResumo do pedido:")
    resumo = resumo_por_item(cart)
    for item_id, dados in resumo.items():
        print(f"{MENU[item_id]['name']}: {dados['qtd']}x - R${dados['subtotal']:.2f}")

    total = calcular_total(cart)
    print(f"\nTOTAL: R${total:.2f}")

    try:
        p = float(input("Valor pago: R$ "))
        if p >= total:
            print(f"Troco: R${p - total:.2f}")
            print("🍟 Pedido finalizado com sucesso! Obrigado pela preferência!")
        else:
            print("💸 Valor insuficiente. Pedido cancelado.")
    except ValueError:
        print("⚠️ Valor inválido. Pedido cancelado.")


if __name__ == "__main__":
    main()

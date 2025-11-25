import pandas as pd
import os
from decimal import Decimal
from typing import Dict, List, Tuple

arquivo_csv = "catalogo.csv"

Cart = List[Tuple[int, int]]  # (id_item, quantidade)


def leitura_csv() -> pd.DataFrame:
    if not os.path.exists(arquivo_csv):
        df = pd.DataFrame(columns=["id", "produto", "valor"])
        df.to_csv(arquivo_csv, index=False)
        print("Catálogo criado com sucesso!")
    else:
        df = pd.read_csv(arquivo_csv)
        print("Catálogo carregado com sucesso!")
    return df


def verificação(usuario: str, senha: str) -> bool:
    return usuario == "ADM" and senha == "Senha"


def escolha():
    df = leitura_csv()
    tipo_usuario = input("Digite 1 para cliente e 2 para administrador: ")

    if tipo_usuario == "1":
        print(" Bem-vindo, cliente!")
        fluxo_cliente(df)
    elif tipo_usuario == "2":
        print("Bem-vindo, administrador")
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite a senha do administrador: ")
        if verificação(usuario, senha):
            print("Acesso autorizado")
            adicionar_item(df)
        else:
            print("Usuário ou senha incorretos")
    else:
        print(" Digite uma opção válida")


def adicionar_item(df: pd.DataFrame):
    while True:
        produto = input("Digite o Produto que deseja adicionar ou 'sair' para encerrar: ")
        if produto.lower() == "sair":
            break
        try:
            valor = Decimal(input("Digite o Valor do Produto: "))
        except:
            print("Valor inválido, tente novamente.")
            continue

        novo_id = 1 if df.empty else df["id"].max() + 1

        novo_item = pd.DataFrame([{
            "id": novo_id,
            "produto": produto,
            "valor": float(valor)
        }])

        df = pd.concat([df, novo_item], ignore_index=True)
        df.to_csv(arquivo_csv, index=False)

        print(f"{produto} adicionado(a) com sucesso com ID {novo_id}!")


def mostrar_cardapio(df: pd.DataFrame) -> None:
    print("\nCARDÁPIO:")
    for _, row in df.iterrows():
        print(f"{row['id']} - {row['produto']} - R${row['valor']:.2f}")
    print("sair - Finalizar pedido")


def ler_opcao() -> str:
    return input("\nDigite o número do item (ou 'sair' para finalizar): ").strip()


def ler_quantidade() -> int:
    try:
        q = int(input("Quantidade: "))
        if q <= 0:
            print("A quantidade deve ser maior que zero.")
            return -1
        return q
    except ValueError:
        print("Quantidade inválida.")
        return -1


def adicionar_ao_carrinho(cart: Cart, item_id: int, qtd: int, df: pd.DataFrame) -> None:
    cart.append((item_id, qtd))
    produto = df.loc[df["id"] == item_id, "produto"].values[0]
    print(f"Adicionado: {qtd}x {produto}")


def calcular_total(cart: Cart, df: pd.DataFrame) -> float:
    total = 0.0
    for item_id, qtd in cart:
        valor = df.loc[df["id"] == item_id, "valor"].values[0]
        total += valor * qtd
    return total


def resumo_por_item(cart: Cart, df: pd.DataFrame) -> Dict[int, Dict[str, float]]:
    resumo: Dict[int, Dict[str, float]] = {}
    for item_id, qtd in cart:
        valor = df.loc[df["id"] == item_id, "valor"].values[0]
        if item_id not in resumo:
            resumo[item_id] = {"qtd": 0, "subtotal": 0.0}
        resumo[item_id]["qtd"] += qtd
        resumo[item_id]["subtotal"] += valor * qtd
    return resumo


def confirmar_finalizacao() -> bool:
    resposta = input("Deseja realmente finalizar o pedido? (s/n): ").strip().lower()
    return resposta == "s"


def fluxo_cliente(df: pd.DataFrame):
    cart: Cart = []
    mostrar_cardapio(df)

    while True:
        opcao = ler_opcao()
        if opcao.lower() == "sair":
            if confirmar_finalizacao():
                print("Finalizando pedido...")
                break
            else:
                continue

        if not opcao.isdigit() or int(opcao) not in df["id"].values:
            print("Item inválido. Escolha um número do cardápio.")
            continue

        item_id = int(opcao)
        qtd = ler_quantidade()
        if qtd <= 0:
            continue

        adicionar_ao_carrinho(cart, item_id, qtd, df)

    if not cart:
        print("\nNenhum item foi adicionado ao pedido. Até logo! ")
        return

    print("\nResumo do pedido:")
    resumo = resumo_por_item(cart, df)
    for item_id, dados in resumo.items():
        produto = df.loc[df["id"] == item_id, "produto"].values[0]
        print(f"{produto}: {dados['qtd']}x - R${dados['subtotal']:.2f}")

    total = calcular_total(cart, df)
    print(f"\nTOTAL: R${total:.2f}")

    try:
        p = float(input("Valor pago: R$ "))
        if p >= total:
            print(f"Troco: R${p - total:.2f}")
            print(" Pedido finalizado com sucesso! Obrigado pela preferência!")
        else:
            print("Valor insuficiente. Pedido cancelado.")
    except ValueError:
        print("Valor inválido. Pedido cancelado.")


if __name__ == "__main__":
    escolha()

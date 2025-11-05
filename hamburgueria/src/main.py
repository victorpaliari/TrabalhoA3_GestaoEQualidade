print("Bem-vindo à Hamburgueria!")
print("CARDÁPIO:")
print("1 - Hambúrguer Simples - R$12")
print("2 - Cheeseburguer - R$14")
print("3 - X-Bacon - R$16")
print("4 - Batata Frita - R$8")
print("5 - Refrigerante - R$6")

a = 0

# listas separadas (quantidades e subtotais)
hb_qtd, hb_tot = [], []
ch_qtd, ch_tot = [], []
xb_qtd, xb_tot = [], []
bt_qtd, bt_tot = [], []
rf_qtd, rf_tot = [], []

while a != 999:
    try:
        a = int(input("Digite o número do item (999 para sair): "))
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue

    if a == 1:
        q = int(input("Quantos hambúrgueres simples? "))
        hb_qtd.append(q)
        hb_tot.append(12 * q)
    elif a == 2:
        q = int(input("Quantos cheeseburgueres? "))
        ch_qtd.append(q)
        ch_tot.append(14 * q)
    elif a == 3:
        q = int(input("Quantos X-Bacon? "))
        xb_qtd.append(q)
        xb_tot.append(16 * q)
    elif a == 4:
        q = int(input("Quantas batatas fritas? "))
        bt_qtd.append(q)
        bt_tot.append(8 * q)
    elif a == 5:
        q = int(input("Quantos refrigerantes? "))
        rf_qtd.append(q)
        rf_tot.append(6 * q)
    elif a == 999:
        print("Finalizando pedido...")
    else:
        print("Item inválido")

print("Resumo do pedido:")
print("Hambúrguer Simples:", sum(hb_qtd), " - R$", sum(hb_tot))
print("Cheeseburguer:", sum(ch_qtd), " - R$", sum(ch_tot))
print("X-Bacon:", sum(xb_qtd), " - R$", sum(xb_tot))
print("Batata Frita:", sum(bt_qtd), " - R$", sum(bt_tot))
print("Refrigerante:", sum(rf_qtd), " - R$", sum(rf_tot))

total = sum(hb_tot) + sum(ch_tot) + sum(xb_tot) + sum(bt_tot) + sum(rf_tot)
print("TOTAL: R$", total)

try:
    p = float(input("Valor pago: R$"))
    if p >= total:
        print("Troco: R$", round(p - total, 2))
    else:
        print("Valor insuficiente. Pedido cancelado.")
except ValueError:
    print("Valor pago inválido. Pedido cancelado.")

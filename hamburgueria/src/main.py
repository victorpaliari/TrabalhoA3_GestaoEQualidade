print("Bem-vindo à Hamburgueria!")
print("CARDÁPIO:")
print("1 - Hambúrguer Simples - R$12")
print("2 - Cheeseburguer - R$14")
print("3 - X-Bacon - R$16")
print("4 - Batata Frita - R$8")
print("5 - Refrigerante - R$6")

b, c, d, e, f, g = [], [], [], [], [], []
a = 0

while a != 999:
    try:
        a = int(input("Digite o número do item (999 para sair): "))
    except ValueError:
        print("Digite um número válido.")
        continue

    if a == 1:
        q = int(input("Quantos hambúrgueres simples? "))
        b.append(q)
        c.append(12 * q)
    elif a == 2:
        q = int(input("Quantos cheeseburgueres? "))
        d.append(q)
        e.append(14 * q)
    elif a == 3:
        q = int(input("Quantos X-Bacon? "))
        f.append(q)
        g.append(16 * q)
    elif a == 4:
        q = int(input("Quantas batatas fritas? "))
        b.append(q)
        c.append(8 * q)
    elif a == 5:
        q = int(input("Quantos refrigerantes? "))
        d.append(q)
        e.append(6 * q)
    elif a == 999:
        print("Finalizando pedido...")
    else:
        print("Item inválido")

print("\nResumo do pedido:")
print("Hambúrguer Simples:", sum(b), "- R$", sum(c))
print("Cheeseburguer:", sum(d), "- R$", sum(e))
print("X-Bacon:", sum(f), "- R$", sum(g))

total = sum(c) + sum(e) + sum(g)
print("TOTAL: R$", total)

try:
    p = float(input("Valor pago: R$"))
    if p >= total:
        print("Troco: R$", round(p - total, 2))
    else:
        print("Valor insuficiente. Pedido cancelado.")
except ValueError:
    print("Valor inválido.")

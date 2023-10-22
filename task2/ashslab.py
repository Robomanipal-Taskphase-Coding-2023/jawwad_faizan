inv = {}

while True:
    op = input("Oper (ADD/DELETE/EXIT): ").strip().upper()

    if op == "EXIT":
        break
    elif op == "ADD":
        itnm, qty = input("Name and qty to add: ").split()
        qty = int(qty)
        if itnm in inv:
            inv[itnm] += qty
            print(f"UPDATED {itnm}")
        else:
            inv[itnm] = qty
            print(f"ADDED {itnm}")
    elif op == "DELETE":
        itnm, qty = input("Name and qty to delete: ").split()
        qty = int(qty)
        if itnm in inv:
            if inv[itnm] < qty:
                print(f"{itnm} could not be DELETED")
            else:
                inv[itnm] -= qty
                print(f"DELETED {itnm}")
        else:
            print(f"{itnm} does not exist")
    else:
        print("Invalid oper. Use ADD, DELETE, or EXIT.")

print("Inventory:")
for it, qty in inv.items():
    print(f"{it}: {qty}")

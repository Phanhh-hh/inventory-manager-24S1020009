# Danh sach san pham toan cuc
products = []

# Feature 1: Them san pham
def add_product(name, price, quantity):
    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }
    products.append(product)
    print(">> Da them san pham thanh cong!")

# Feature 2: Xem ton kho
def view_inventory():
    if not products:
        print(">> Kho hang dang trong!")
        return
    print("\n=== DANH SACH SAN PHAM ===")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product['name']} - Gia: {product['price']} - So luong: {product['qty']}")

# Feature 3: Canh bao het hang
def check_low_stock():
    low_stock_items = [p for p in products if p['qty'] < 5]
    if not low_stock_items:
        print(">> Tat ca san pham con du so luong.")
        return
    print("\n=== CANH BAO HET HANG ===")
    for i, product in enumerate(low_stock_items, start=1):
        print(f"{i}. {product['name']} - So luong: {product['qty']} (can nhap them!)")

# Ham main
def main():
    while True:
        print("\n=== INVENTORY MANAGER ===")
        print("1. Xem danh sach san pham")
        print("2. Them san pham")
        print("3. Xoa san pham")
        print("4. Kiem tra san pham sap het")
        print("5. Thoat")

        choice = input("Chon chuc nang: ")

        if choice == "1":
            view_inventory()
        elif choice == "2":
            name = input("Nhap ten san pham: ")
            price = int(input("Nhap gia san pham: "))
            quantity = int(input("Nhap so luong: "))
            add_product(name, price, quantity)
        elif choice == "3":
            print(">> Chuc nang xoa san pham (se lam sau)")
        elif choice == "4":
            check_low_stock()
        elif choice == "5":
            print("Thoat chuong trinh...")
            break
        else:
            print("Lua chon khong hop le.")

if __name__ == "__main__":
    main()

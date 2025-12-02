# Danh sach san pham toan cuc
products = []

def add_product(name, price, quantity):
    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }
    products.append(product)
    print(">> Da them san pham thanh cong!")
def view_inventory():
    if not products:
        print(">> Kho hang dang trong!")
        return
    print("\n=== DANH SACH SAN PHAM ===")
    for i, product in enumerate(products, start=1):
        print(f"{i}. {product['name']} - Gia: {product['price']} - So luong: {product['qty']}")

def main():
    while True:
        print("=== INVENTORY MANAGER ===")
        print("1. Xem danh sach san pham")
        print("2. Them san pham")
        print("3. Xoa san pham")
        print("4. Thoat")

        choice = input("Chon chuc nang: ")

        if choice == "1":
            view_inventory()


        elif choice == "2":
            # Nhap thong tin san pham
            name = input("Nhap ten san pham: ")
            price = int(input("Nhap gia san pham: "))
            quantity = int(input("Nhap so luong: "))
            add_product(name, price, quantity)

        elif choice == "3":
            print(">> Chuc nang xoa san pham (se lam sau)")

        elif choice == "4":
            print("Thoat chuong trinh...")
            break

        else:
            print("Lua chon khong hop le.")

if __name__ == "__main__":
    main()

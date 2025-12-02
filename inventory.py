# Danh sách sản phẩm toàn cục
products = []

def main():
    while True:
        print("\n=== INVENTORY MANAGER ===")
        print("1. Xem danh sách sản phẩm")
        print("2. Thêm sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            print(">> Chức năng xem danh sách (sẽ làm sau)")
        elif choice == "2":
            print(">> Chức năng thêm sản phẩm (sẽ làm sau)")
        elif choice == "3":
            print(">> Chức năng xóa sản phẩm (sẽ làm sau)")
        elif choice == "4":
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

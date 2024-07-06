def write_supplier(suppliers):
    suppliers_file = open("supplier.txt", "w")
    for supplier in suppliers:
        suppliers_file.writelines(f"Supplier: {suppliers[0]}")
        suppliers_file.writelines(f"Supplier code: {suppliers[1]}")
        suppliers_file.writelines(f"Supplier code: {suppliers[2]}")
        suppliers_file.writelines(f"Stock: {suppliers[3]}")
        suppliers_file.writelines()
    suppliers_file.close()


def latest_suppliers():
    suppliers = []
    supplier_info = []
    supplier_file = open("supplier.txt", "r")
    lines = supplier_file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("Supplier:"):
            supplier = line.split(":")[1].strip()
            supplier_info.append(supplier)
        if line.startswith("Supplier code:"):
            supplier = line.split(":")[1].strip()
            supplier_info.append(supplier)
        if line.startswith("Tel.No:"):
            supplier = line.split(":")[1].strip()
            supplier_info.append(supplier)
        if line.startswith("Address:"):
            supplier = line.split(":")[1].strip()
            supplier_info.append(supplier)
            suppliers.append(supplier_info)
            supplier_info = []
    return suppliers
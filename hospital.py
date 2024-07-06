def write_hospital(hospitals):
    hospital_file = open("hospital.txt", "w")
    for hospital in hospitals:
        hospital_file.writelines(f"hospital: {hospitals[0]}")
        hospital_file.writelines(f"hospital code: {hospitals[1]}")
        hospital_file.writelines(f"hospital code: {hospitals[2]}")
        hospital_file.writelines(f"Stock: {hospitals[3]}")
        hospital_file.writelines()
    hospital_file.close()


def latest_hospitals():
    hospitals = []
    hospital_info = []
    hospital_file = open("hospital.txt", "r")
    lines = hospital_file.readlines()
    for line in lines:
        line = line.strip()
        if line.startswith("Hospital:"):
            hospital = line.split(":")[1].strip()
            hospital_info.append(hospital)
        if line.startswith("Hospital code:"):
            hospital = line.split(":")[1].strip()
            hospital_info.append(hospital)
        if line.startswith("Tel.No:"):
            hospital = line.split(":")[1].strip()
            hospital_info.append(hospital)
        if line.startswith("Address:"):
            hospital = line.split(":")[1].strip()
            hospital_info.append(hospital)
            hospitals.append(hospital_info)
            hospital_info = []
    return hospitals
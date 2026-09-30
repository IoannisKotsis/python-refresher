def add_visit(patient, visit):
    new_dict = patient.copy()
    new_dict["visits"]=patient["visits"][:]
    new_dict["visits"].append(visit)
    return new_dict

anna = {"id": 7, "name": "Anna", "visits": ["2026-01-10"]}
add_visit(anna, "2026-08-01")


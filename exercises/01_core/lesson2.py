def register(patient_id, registry=None):
    if registry is None:
        registry = []
    registry.append(patient_id)
    return registry
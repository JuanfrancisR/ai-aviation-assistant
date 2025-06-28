# Simulated parser for demonstration
def load_manual(query):
    sample_pages = [
        {"page": "Page 1", "snippet": "ATA 28-20-00 Fuel Pressure Sensor Removal"},
        {"page": "Page 2", "snippet": "ATA 32-30-00 Nose Gear Installation"},
    ]
    return [p for p in sample_pages if query.lower() in p['snippet'].lower()]

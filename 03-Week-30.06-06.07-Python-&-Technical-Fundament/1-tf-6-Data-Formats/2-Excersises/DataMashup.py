import json
import csv
from io import StringIO

# Source 1: JSON string
products_json_str = """
[
  {"id": "prod001", "name": "Wireless Mouse"},
  {"id": "prod002", "name": "USB Keyboard"},
  {"id": "prod003", "name": "24-inch Monitor"},
  {"id": "prod004", "name": "Webcam HD"}
]
"""

# Source 2: CSV string
inventory_csv_str = """ProductID,Quantity,Warehouse
prod001,55,Main
prod003,12,West Wing
prod002,78,Main
prod004,30,Annex
"""

# 1. Parse JSON string
products = json.loads(products_json_str)

# 2. Parse CSV string
inventory = []
csv_reader = csv.DictReader(StringIO(inventory_csv_str))
for row in csv_reader:
    # Ensure Quantity is integer
    row["Quantity"] = int(row["Quantity"])
    inventory.append(row)

# 3. Combine data
combined = []
for product in products:
    # Find matching inventory entry
    match = next((item for item in inventory if item["ProductID"] == product["id"]), None)
    if match:
        combined.append({
            "id": product["id"],
            "name": product["name"],
            "quantity": match["Quantity"],
            "warehouse": match["Warehouse"]
        })

# 4. Convert to JSON
output_json_str = json.dumps(combined, indent=2)

# 5. Print result
print(output_json_str)

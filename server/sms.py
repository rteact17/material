def send_sms(customer_name, vehicle_number, material, quantity):
    message = f"Vehicle: {vehicle_number}, Material: {material}, Qty: {quantity}"
    print(f"Sending SMS to {customer_name}: {message}")
    # Send via SMS API

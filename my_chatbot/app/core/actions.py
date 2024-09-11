def execute_action(action_type, parameters):
    """
    Execute a specified action based on the action type and parameters.

    Args:
        action_type (str): The type of action to execute (e.g., 'create_order', 'cancel_order').
        parameters (dict): A dictionary of parameters required for the action.

    Returns:
        str: A message indicating the result of the action.
    """
    if action_type == "create_order":
        # Implement logic to create an order
        order_id = parameters.get("order_id", "12345")
        return f"Order {order_id} has been created successfully."
    
    elif action_type == "cancel_order":
        # Implement logic to cancel an order
        order_id = parameters.get("order_id", "12345")
        return f"Order {order_id} has been cancelled successfully."
    
    elif action_type == "collect_payment":
        # Implement logic to collect payment
        payment_link = parameters.get("payment_link", "http://example.com/pay")
        return f"Payment can be made via the following link: {payment_link}"
    
    elif action_type == "view_invoice":
        # Implement logic to view an invoice
        invoice_id = parameters.get("invoice_id", "INV123")
        return f"Invoice {invoice_id} details are displayed here."
    
    else:
        return "Action not recognized."
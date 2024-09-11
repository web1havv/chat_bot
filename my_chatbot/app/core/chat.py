from transformers import pipeline

# Load a smaller language model for efficiency
def load_model():
    return pipeline('text-generation', model='distilgpt2')

# Instantiate the model
model = load_model()

def generate_response(query):
    """
    Generate a response from the chatbot using the language model.
    
    Args:
        query (str): The user's query.
    
    Returns:
        str: The chatbot's response.
    """
    # Generate a response using the model
    response = model(query, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']
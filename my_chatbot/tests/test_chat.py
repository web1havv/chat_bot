from app.core.chat import generate_response

def test_generate_response():
    # Test with a simple query
    query = "Hello, how are you?"
    response = generate_response(query)
    
    # Ensure the response is a non-empty string
    assert isinstance(response, str)
    assert len(response) > 0

    # Test with another query
    query = "What is the capital of France?"
    response = generate_response(query)
    
    # Ensure the response is a non-empty string
    assert isinstance(response, str)
    assert len(response) > 0
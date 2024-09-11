from transformers import pipeline

def load_model():
    """
    Load a language model for generating text responses.
    
    Returns:
        transformers.pipelines.Pipeline: A text-generation pipeline.
    """
    # Load a smaller, efficient model for text generation
    return pipeline('text-generation', model='distilgpt2')

# Instantiate the model
model = load_model()
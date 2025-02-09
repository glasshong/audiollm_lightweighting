from .salmonn_gemma2 import SALMONN_gemma2

def load_model_gemma2(config):
    return SALMONN_gemma2.from_config(config)
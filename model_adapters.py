"""Model adapters for different LLM frameworks."""

import torch
from typing import Optional, Dict, Any

class UnslothAdapter:
    """Adapter for Unsloth-optimized models."""
    
    def __init__(self, model_name: str, config: Dict[str, Any]):
        self.model_name = model_name
        self.config = config
        self.model = None
        self.tokenizer = None
    
    def load_model(self):
        """Load Unsloth model."""
        try:
            from unsloth import FastLanguageModel
            
            self.model, self.tokenizer = FastLanguageModel.from_pretrained(
                model_name=self.config["model_name"],
                max_seq_length=self.config.get("max_seq_length", 2048),
                dtype=None,
                load_in_4bit=self.config.get("load_in_4bit", True),
            )
            
            # Enable native 2x faster inference
            FastLanguageModel.for_inference(self.model)
            
        except ImportError:
            raise ImportError("Unsloth not installed. Install with: pip install unsloth")
    
    def generate(self, prompt: str, temperature: float, max_new_tokens: int) -> str:
        """Generate response using Unsloth model."""
        
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=2048
        )
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )
        
        # Decode only the new tokens
        response = self.tokenizer.decode(
            outputs[0][inputs.input_ids.shape[1]:], 
            skip_special_tokens=True
        )
        
        return response.strip()

# Add other adapters as needed (OpenAI API, Hugging Face, etc.) 
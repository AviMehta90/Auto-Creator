from dataclasses import dataclass

@dataclass
class PromptRequest:
    prompt: str

@dataclass
class GenerationResponse:
    caption: str
    image_url: str


# diffusion
from torch import autocast
from diffusers import StableDiffusionPipeline

class StableDiffusion:
    def __init__(self, model_id = "CompVis/stable-diffusion-v1-4"):
        self.device = "cuda"
        self.model = StableDiffusionPipeline.from_pretrained(model_id, use_auth_token=True).to(self.device)
    
    def txt2img(self, prompt:str):
        # generate image
        with autocast("cuda"):
            image = self.model(prompt, guidance_scale=7.5).images[0]  
            
        return image
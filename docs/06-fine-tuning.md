# Fine Tuning a Text-to-Image Model

## Intro
Fine-tuning is the process of adding new layers to an existing model to get it to perform better on a give task.

## Steps

1. Find an existing model

[HuggingFace Text-to-Image Models](https://huggingface.co/models?pipeline_tag=text-to-image&sort=downloads)

2. Download the model to your local computer

3. Create a set of images you want to use to fine-tune the model

4. Add new layers to the network and train their weights using these images

## Waifu Diffusion

Waifu-diffusion is a latent text-to-image diffusion model that has been conditioned on high-quality anime images through fine-tuning. The image dataset for fine tuning was 56k images chosesen from the [Danbooru](https://danbooru.donmai.us/) image database.

[Waifu-diffusion](https://huggingface.co/hakurei/waifu-diffusion)

## Sample Code

```py
import gradio as gr
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# our new model ID
model_id = "hakurei/waifu-diffusion"
# use this only if you have a GPU from NVIDIA
device = "cuda"

# we create a new pipeline with our model id using a 16-bit floating point representation
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, revision='fp16')
pipe = pipe.to(device)


block = gr.Blocks(css=".container { max-width: 800px; margin: auto; }")

num_samples = 2

def infer(prompt):
    with autocast("cuda"):
        images = pipe([prompt] * num_samples, guidance_scale=7.5)["sample"]

    return images


with block as demo:
    gr.Markdown("<h1><center>Waifu Diffusion</center></h1>")
    gr.Markdown(
        "waifu-diffusion is a latent text-to-image diffusion model that has been conditioned on high-quality anime images through fine-tuning."
    )
    with gr.Group():
        with gr.Box():
            with gr.Row().style(mobile_collapse=False, equal_height=True):

                text = gr.Textbox(
                    label="Enter your prompt", show_label=False, max_lines=1
                ).style(
                    border=(True, False, True, True),
                    rounded=(True, False, False, True),
                    container=False,
                )
                btn = gr.Button("Run").style(
                    margin=False,
                    rounded=(False, True, True, False),
                )
               
        gallery = gr.Gallery(label="Generated images", show_label=False).style(
            grid=[2], height="auto"
        )
        text.submit(infer, inputs=[text], outputs=gallery)
        btn.click(infer, inputs=[text], outputs=gallery)

    gr.Markdown(
        """___
   <p style='text-align: center'>
   Created by https://huggingface.co/hakurei
   <br/>
   </p>"""
    )


demo.launch(debug=True)
```
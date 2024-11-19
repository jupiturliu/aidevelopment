# Install necessary libraries with:
# pip install diffusers transformers torch streamlit

import streamlit as st
from huggingface_hub import login
from diffusers import StableDiffusionPipeline
import torch
import os
import certifi

def generate_image(prompt, resolution=(512, 512), output_path="output.png", use_gpu=False):
    # Login to Hugging Face
    login("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")    

     # Set SSL certificate path
    os.environ['SSL_CERT_FILE'] = certifi.where()
    
    # Load the pre-trained Stable Diffusion model with local caching
    model_id = "stabilityai/stable-diffusion-2-1"
    cache_dir = os.path.expanduser("~/.cache/stable_diffusion")

    # Determine the appropriate torch_dtype based on the device
    if use_gpu and torch.cuda.is_available():
        torch_dtype = torch.float16
    else:
        torch_dtype = torch.float32
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch_dtype, cache_dir=cache_dir)
    
    # Use GPU if available and selected
    if use_gpu and torch.cuda.is_available():
        pipe = pipe.to("cuda")
    else:
        pipe = pipe.to("cpu")

    # Enable attention slicing to reduce memory usage
    pipe.enable_attention_slicing()
    #pipe.enable_sequential_cpu_offload()

    # Generate the image based on the prompt with specified resolution
    image = pipe(prompt, height=resolution[1], width=resolution[0], num_inference_steps=15).images[0]  # Reduce the number of inference steps for faster generation

    # Save the generated image
    image.save(output_path)
    return output_path

# Streamlit web app
st.title("Stable Diffusion Image Generator")
prompt = st.text_input("Enter a prompt to generate an image:")

# Image resolution input
resolution_options = {"Very Low (256x256)": (256, 256), "Low (512x512)": (512, 512), "Medium (768x768)": (768, 768)}
resolution_label = st.selectbox("Select image resolution:", list(resolution_options.keys()))
resolution = resolution_options[resolution_label]
# GPU support input
use_gpu = st.checkbox("Use GPU (if available)")
x
# Check if GPU is available and inform the user
if use_gpu:
    if torch.cuda.is_available():
        st.success("GPU is available and will be used for image generation.")
    else:
        st.warning("GPU is not available. Falling back to CPU.")
else:
    st.info("Using CPU for image generation.")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            output_path = generate_image(prompt, resolution, use_gpu=use_gpu)
        st.image(output_path, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a prompt to generate an image.")
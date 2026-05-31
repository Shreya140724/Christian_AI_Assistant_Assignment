import os
import time
import torch

from diffusers import StableDiffusionPipeline


MODEL_NAME = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)

pipe = pipe.to("cpu")


def generate_image(prompt):

    os.makedirs(
        "generated_images",
        exist_ok=True
    )

    image = pipe(
        prompt,
        num_inference_steps=20
    ).images[0]

    filename = (
        str(int(time.time()))
        + ".png"
    )

    image_path = os.path.join(
        "generated_images",
        filename
    )

    image.save(image_path)

    return image_path


if __name__ == "__main__":

    path = generate_image(
        "Jesus walking on water"
    )

    print(path)
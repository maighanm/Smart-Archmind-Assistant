from flask import Flask, request, jsonify, send_from_directory
import torch
from diffusers import DiffusionPipeline

app = Flask(__name__)

print("Loading SDXL pipeline...")

base_model = "stabilityai/stable-diffusion-xl-base-1.0"
pipe = DiffusionPipeline.from_pretrained(
    base_model,
    torch_dtype=torch.float16,
    variant="fp16"
).to("cuda")

lora_path = "/content/drive/MyDrive/floorplan_lora/pytorch_lora_weights.safetensors"
pipe.load_lora_weights(lora_path)

print("Pipeline loaded with LoRA.")

@app.route("/", methods=["GET"])
def home():
    return "SDXL LoRA API is running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    prompt = data.get("prompt")
    width = int(data.get("width", 1024))
    height = int(data.get("height", 1024))

    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    # Run SDXL + LoRA
    image = pipe(
        prompt=prompt,
        width=width,
        height=height,
        num_inference_steps=30,
    ).images[0]

    filename = "generated.png"
    image.save(filename)

    # Make the file accessible via ngrok
    public_url = request.host_url + filename

    return jsonify({
        "message": "Image generated successfully",
        "url": public_url
    })

@app.route('/<path:filename>', methods=['GET'])
def serve_file(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

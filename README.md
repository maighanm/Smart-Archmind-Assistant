# 🌈 Hues.AI — Text-to-Floorplan Generator

A system that turns simple words into fully realized architectural floorplans — where imagination quietly hardens into structure. ✨🏠

<p align="center"> 
  <img src="HEADER_IMAGE_LINK_HERE" alt="Hues.AI Header" width="600"/> 
</p>

---

## 🌐 Live Demo

Experience Hues.AI instantly through my hosted demo:  

🔗 [https://mai2026-sdxl-lora-floorplan.hf.space](https://mai2026-sdxl-lora-floorplan.hf.space)  

This Hugging Face Space runs my fine-tuned model with GPU acceleration and allows me (or anyone) to generate floorplans without installing anything. 🚀💻

---

## 📸 Screenshots

### 🏠 Home Interface
A simple, elegant interface for entering design descriptions. Hues.AI interprets my text and begins assembling the architectural structure. ✍️✨

### 🔍 Chatbot Interaction
A conversational assistant that helps refine room requirements, adjust features, and explore different layout possibilities. 🤖💬

### 💬 Recommendation Results
The system generates refined suggestions — improved layouts, smarter connections, and alternative interior arrangements. 🏘️📐

*(Add actual image files later.)*

---

## 📽️ Ad Video

🎥 **Watch the Ad Video**  
A conceptual teaser showcasing Hues.AI’s capabilities. 🎬✨  

🧠 The entire ad was generated using AI tools — matching my project’s creative philosophy. 🎨🤯

---

## 📘 Project Overview

Hues.AI transforms natural-language descriptions into architectural floorplans.  
Powered by Stable Diffusion XL (SDXL) with LoRA fine-tuning, my model learns structural patterns such as:  

- 🛋️ Room distribution  
- 🚪 Spatial flow  
- 📐 Interior layout conventions  
- 🏛️ Consistent architectural geometry  

The project offers:  

✅ A refined model trained on **my curated dataset**  
✅ A Flask-based API for programmatic generation  
✅ A Hugging Face Space demo  
✅ Google Colab GPU deployment  
✅ Clear dataset and training pipeline documentation  

---

## ⭐ Key Features

- 📝 Generate architectural floorplans from pure text  
- 🧩 LoRA-enhanced SDXL for domain-specific accuracy  
- 🌐 Public Hugging Face Space deployment  
- 🔌 Flask inference API (local + Colab)  
- 📦 Clean dataset for reproducible training  
- 📑 JSON-ready structure for future post-processing  
- 🖼️ Supports high-resolution 1024×1024 output  

---

## 🧩 Model Artifacts (`model/` folder)

My `model/` folder currently contains:  

1️⃣ `pytorch_lora_weights.safetensors`  
- My fine-tuned LoRA weights — this file injects architectural knowledge into SDXL.  

2️⃣ `config.json`
```json
{
  "base_model_name_or_path": "stabilityai/stable-diffusion-xl-base-1.0"
}

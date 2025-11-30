# 🌈 Hues.AI — Text-to-Floorplan Generator

A system that turns simple words into fully realized architectural floorplans — where imagination quietly hardens into structure. ✨🏠

<p align="center"> 
  <img src="HEADER_IMAGE_LINK_HERE" alt="Hues.AI Header" width="600"/> 
</p>

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

## 🌐 Live Demo

Experience Hues.AI instantly through my hosted demo:  

🔗 [https://mai2026-sdxl-lora-floorplan.hf.space](https://mai2026-sdxl-lora-floorplan.hf.space)  

This Hugging Face Space runs my fine-tuned model and allows me (or anyone) to generate floorplans without installing anything. 🚀💻

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
```
---

This indicates:  
⚡ The LoRA is built on top of SDXL Base 1.0  
⚡ No additional LoRA-specific metadata exists  
⚡ Loading is straightforward and compatible with the Diffusers pipeline  

---

## 🗂️ Repository Structure
```
.
├── model/
│   ├── pytorch_lora_weights.safetensors
│   └── config.json
├── notebooks/
│   └── (training & preprocessing notebooks)
├── app.py
├── floor_plan_model.py
├── requirements.txt
└── README.md
```
---

## 🧬 Dataset

My cleaned, structured training dataset is available here:  

📦 [Google Drive link](https://drive.google.com/file/d/1InObuWPKeTRwpHoSfgDOerTb-OcIAP-4/view?usp=drivesdk)  

Includes:  
- 🖼️ Floorplan images  
- 📝 Normalized captions  
- ✔️ Quality-filtered samples  
- ⚡ Preprocessing aligned to SDXL  

---

## 🧠 Training Summary

- **Model:** SDXL Base 1.0  
- **Training:** LoRA fine-tuning  
- **Rank:** 4–32 (depending on experiment)  
- **Learning Rate:** 1e-4 to 5e-4  
- **Batch Size:** 4–32  
- **GPU:** T4 / A100  
- **Objective:** Structural accuracy + clear interior layout lines 💪📐  

---

## 🔧 Technologies Used

- 🖼️ Stable Diffusion XL  
- 🧩 LoRA fine-tuning  
- 🤗 HuggingFace Diffusers  
- 🐍 Flask  
- ☁️ Google Colab  
- 🔗 ngrok  
- 🌐 Hugging Face Spaces  
- 💻 Python 3.x  

---

## 🚀 Running the Project

### Option 1 — Local Execution (with `python app.py`)

1️⃣ **Install dependencies** 

```bash
pip install -r requirements.txt
```

2️⃣ **Place the LoRA weights**  
Ensure the file is located at:  

```bash
model/pytorch_lora_weights.safetensors
``` 

3️⃣ **Update the path in app.py**  
```bash
lora_path = "model/pytorch_lora_weights.safetensors"  
```

4️⃣ **Run the server**  
```bash
python app.py  
```
## Local server: http://localhost:5000 🌐


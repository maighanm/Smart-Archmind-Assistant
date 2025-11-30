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
```bash
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

**Local server: http://localhost:5000**🌐

### Option 2 — Google Colab GPU Deployment (Primary Method)

1️⃣ **Open my notebook**
2️⃣ **Install requirements**
3️⃣ **Load SDXL + LoRA**
4️⃣ **Start Flask:**
```python
app.run(host="0.0.0.0", port=5000)
```
5️⃣ **Expose via ngrok:**
```python
from pyngrok import ngrok
ngrok.connect(5000)
```
** Use the ngrok URL for inference. 🚀🔗**
---
## 🔌 API Endpoints

### GET `/`

Checks the server status.

**Response:**

```arduino
SDXL LoRA API is running!
```

---

### POST `/generate`

Generates an image based on the given prompt.

**JSON Input:**

```json
{
  "prompt": "5 bedrooms, 2 living rooms, 1 kitchen, 3 bathrooms",
  "width": 1024,
  "height": 1024
}
```
**Output:**

```json
{
  "message": "Image generated successfully",
  "url": "http://<host>/generated.png"
}
```
## 🔭 Future Enhancements

- 🏷️ Auto room labeling  
- 📐 Room coordinate extraction (JSON)  
- 🖌️ SVG floorplan export  
- 🏢 Multi-floor support  
- 🧩 Constraint-aware generation  
- 🌐 UI expansion on HuggingFace  

---

## 👥 Team Members

- **Mai Abd Elghany Abd Elhalim Ghanm** — Team Leader 🏆  
- **Kenzy Khaled Mahmoud Tawfiq** 💡  
- **Sara Mostafa Ahmed Ali** ✨  

---

## 🌟 Final Reflection

Hues.AI is a bridge between imagination and form 🏗️ — a tool that lets words condense into walls, spaces, and paths.  
It stands at the edge where language becomes structure, and ideas become places we can inhabit 🌈.


# 🏠 Smart Archmind Assistant

An **AI-powered application** that automatically generates **2D architectural floorplans** from **textual descriptions**.  
Simply describe your desired layout — for example,  
> “A two-bedroom apartment with one kitchen and a balcony”  
and Smart Archmind Assistant will generate a corresponding **2D floorplan** that you can visualize, edit, and export. ✨

---

## 🚀 Project Overview

The **Smart Archmind Assistant** integrates **Natural Language Processing (NLP)** 🧠 and **Computer Vision (CV)** 👁️‍🗨️ to bridge the gap between imagination and architecture.  
It enables architects, engineers, and homeowners to quickly visualize ideas through **automated floorplan generation**. 🏗️

### 🎯 Objectives
- 🏡 Simplify the early design phase in architecture and civil engineering.  
- ⏱️ Reduce time and effort in conceptual layout creation.  
- 🤖 Explore how NLP and AI models can assist in architectural design workflows.

---

## ⚙️ Key Features

| 🌟 Feature | 📋 Description |
|-------------|----------------|
| 🧠 **Text-to-Floorplan Generator** | Converts user-written descriptions into structured room layouts. |
| 🏷️ **Room Labeling & Arrangement** | Automatically detects and labels rooms (e.g., kitchen, bedroom, bathroom). |
| 🎨 **Interactive Editor** | Allows users to adjust room sizes, labels, and arrangements through drag-and-drop tools. |
| 💡 **AI Suggestions** | Provides design improvement tips based on total area and layout balance. |
| 📚 **Knowledge Hub (optional)** | Central hub for articles, updates, and AI-in-architecture research. |

---

## 🧩 Tech Stack

| 🛠️ Purpose | 💻 Tools / Libraries | 🧾 Description |
|--------------|--------------------|----------------|
| **Data Handling** | Python 🐍, Pandas, NumPy | Manage and preprocess floorplan datasets. |
| **Text Processing (Input)** | NLTK, spaCy, 🤗 Hugging Face Transformers | Understand and process user textual inputs. |
| **Model Training / Inference** | PyTorch 🔥 / TensorFlow 🧩 | Train or fine-tune layout generation models. |
| **Layout Generation** | Diffusion Models, VAEs, GANs (e.g., Stable Diffusion, LayoutGAN) 🏗️ | Generate realistic floorplan images or spatial maps. |
| **API Framework** | FastAPI ⚡ / Flask 🧱 | Serve the AI model through a RESTful API. |
| **Storage / Database** | Firebase Firestore 🔥, MongoDB 🍃, PostgreSQL 🐘 | Store user data and generated layouts. |
| **Cloud Hosting** | Google Cloud ☁️, AWS 🪣, Render 🚀 | Host backend and deploy trained models. |

---

## 📦 Dataset Sources

The system uses a combination of publicly available **floorplan datasets** for training and evaluation 📊:

1. 🏠 [bankole/floor-plans-dataset](https://huggingface.co/datasets/bankole/floor-plans-dataset)  
2. 🏘️ [jprve/FloorPlansV2](https://huggingface.co/datasets/jprve/FloorPlansV2)  
3. 🏢 [FahadIqbal5188/floorplan-SDXL](https://huggingface.co/datasets/FahadIqbal5188/floorplan-SDXL)  
4. 🏡 [HamzaWajid1/FloorPlans970Dataset](https://huggingface.co/datasets/HamzaWajid1/FloorPlans970Dataset)  
5. 🏗️ [Ali-Hasan-Khan/mergred-200-labelled-floorplan-properly](https://huggingface.co/datasets/Ali-Hasan-Khan/mergred-200-labelled-floorplan-properly)  
6. 🏙️ [johnmaj/floorplans](https://huggingface.co/datasets/johnmaj/floorplans)  
7. 📐 [johnmaj/floorplan_masks](https://huggingface.co/datasets/johnmaj/floorplan_masks)

---

## 🧠 Machine Learning Pipeline

1. 🗂️ **Data Collection:** Retrieve floorplan datasets from Hugging Face.  
2. 🧹 **Data Cleaning:** Remove duplicates, standardize formats, and ensure consistent labeling.  
3. ⚙️ **Feature Engineering:** Extract spatial, textual, and visual features for model input.  
4. 🤖 **Model Training:** Train AI models (e.g., GANs, diffusion-based) to map text → floorplan.  
5. 🔌 **Inference API:** Expose model endpoints using FastAPI for frontend integration.  
6. 📱 **Frontend Integration:** Connect to a Flutter mobile app for user interaction.

---

## 📱 Final Deliverable

A **mobile application** 📲 that allows users to:
- 📝 Enter textual descriptions.  
- 🏠 View automatically generated 2D floorplans.  
- ✏️ Edit and customize layouts.  
- 💾 Save or export the final design.

---

## 🗓️ Project Timeline

| 📅 Week | 🧾 Deliverables | 👥 Team Roles |
|----------|----------------|---------------|
| **1–2** | Define project scope & explore datasets | All members search for datasets 🔍 |
| **3–4** | Collect & clean datasets | All members clean datasets 🧹 |
| **5–6** | Continue cleaning, begin feature engineering | All members handle cleaning + feature extraction ⚙️ |
| **7–8** | Apply **NLP techniques** for text cleaning, extraction, and preprocessing; begin **model training** | All members work on text preprocessing 🧠 and start AI model training 🤖 |

---

## 👥 Project Team

| 👩‍💻 Name | 🧭 Role |
|------------|---------|
| **Mai Abd Elghany Abd Elhalim Ghanm** | Team Leader 👑 |
| **Sara Mostafa Ahmed Ali** | Team Member 💻 |
| **Kenzy Khaled Mahmoud Tawfiq** | Team Member 🧩 |
| **Menna El Sayed** | Team Member 🧩 |
| **Mariam Safwat Ibrahim Elewa** | Team Member 🧩 |

🔗 **GitHub Repository:** [Smart Archmind Assistant](https://github.com/maighanm/Smart-Archmind-Assistant.git)

---

## 🌐 Future Enhancements

- 🧱 Add **3D visualization** for generated layouts.  
- 🎙️ Integrate **voice-based input** for layout descriptions.  
- 🧮 Implement **reinforcement learning** for optimized space utilization.  
- 💻 Develop a **web-based version** alongside the mobile app.

---

## 📄 License

📜 This project is licensed under the **MIT License** – feel free to use, modify, and distribute.

---

## 💬 Acknowledgments

We would like to thank:
- 🎓 Our instructor **Aya Hesham** for her continuous guidance and support. 💐
- 🤝 Open-source contributors for datasets and libraries.  
- 🧠 The Hugging Face community for providing rich dataset resources.

---

> 💡 **Smart Archmind Assistant** — *Transforming words into architectural visions.* 🏗️  
> ✍️ *README created with ❤️ by **Mai Ghanm***

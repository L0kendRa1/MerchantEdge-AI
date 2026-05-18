# 📦 MerchantEdge AI

**Gemma 4 Good Hackathon Submission** **Track:** Digital Equity  

MerchantEdge AI is a 100% offline, privacy-first business intelligence hub built to empower local e-commerce entrepreneurs. By leveraging the highly optimized **Gemma 4 E4B** edge model, it provides enterprise-grade AI tools without requiring internet access or risking sensitive storefront data on public cloud servers.

---

### 🚀 The Problem
Small-scale entrepreneurs and local sellers often lack the enterprise tools needed to scale in the digital economy. Current cloud-based AI solutions present two massive roadblocks:
1. **The Connectivity Gap:** In many regions, poor Wi-Fi means lost productivity. 
2. **The Privacy Risk:** Uploading sensitive business strategies, KYC documents, or financial metrics to public servers poses a major security risk.

### 💡 The Solution
MerchantEdge AI brings frontier intelligence directly to the user's local device. It costs zero dollars in API fees, operates with zero network latency, and guarantees absolute data privacy. 

Whether a user is managing a local storefront, drafting product descriptions for brands like Urbanora, or strategizing digital income streams (like monetizing Lofi beats channels via Pinterest), MerchantEdge handles it all off the grid.

---

### ✨ Core Workflows
1. **📝 E-commerce Product Copywriter:** Instantly generates conversion-focused, SEO-optimized product descriptions based on simple feature inputs.
2. **📌 Strategic Content Planner:** Acts as a high-level digital marketing strategist, mapping out multi-day content calendars to drive traffic.
3. **📚 Offline Academic Tutor:** A dedicated workspace that breaks down complex subjects (like Ratio Analysis or mathematics) step-by-step for offline studying without web distractions.

---

### 🛠️ Technical Architecture
* **AI Model:** `google/gemma-4-e4b` (Optimized for edge-device reasoning)
* **Backend Inference:** LM Studio (Local Server environment)
* **Frontend UI:** Streamlit (For a clean, desktop-native application interface)
* **Integration:** Official OpenAI Python SDK (routing traffic exclusively through local `127.0.0.1` loopback)

---

### 💻 How to Run Locally

If you would like to test MerchantEdge AI on your own machine:

**1. Set up LM Studio**
* Download and install [LM Studio](https://lmstudio.ai/).
* Search for and download the `google/gemma-4-e4b` model.
* Go to the **Local Server** tab, ensure the host is set to `127.0.0.1` (Port `1234`), and click **Start Server**.
* Ensure the Gemma model is actively loaded into memory.

**2. Set up the Environment**
Clone this repository and install the required dependencies:
```bash
pip install streamlit openai
```
**3. Launch the Application**
Run the Streamlit app strictly on your local network:
` ` `bash
streamlit run app.py --server.address 127.0.0.1
` ` `
The MerchantEdge Hub will automatically open in your default web browser at `http://127.0.0.1:8501`. Feel free to disable your Wi-Fi and test its offline capabilities!

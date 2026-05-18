import streamlit as st
from openai import OpenAI

# Connect directly to LM Studio's local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Set up the page layout
st.set_page_config(page_title="MerchantEdge AI Hub", layout="wide")

st.title("📦 MerchantEdge AI Hub")
st.caption("Powered locally by Gemma 4 via LM Studio • Completely Offline & Private")

# Sidebar configuration
with st.sidebar:
    st.header("System Settings")
    st.info("🔄 Connected to local Gemma 4 model via LM Studio.")
    st.warning("🔒 No data leaves this device. Ideal for private storefront management.")

# Create the distinct workflow workspaces using Tabs
tab1, tab2, tab3 = st.tabs(["📝 E-commerce Copywriter", "📌 Pinterest Planner", "📚 Offline Academic Tutor"])

# --- WORKFLOW 1: PRODUCT COPYWRITER ---
with tab1:
    st.subheader("Generate SEO-Optimized Product Descriptions")
    
    prod_name = st.text_input("Product Title", placeholder="e.g., Premium Leather Minimalist Wallet")
    keywords = st.text_input("Key Features / Materials", placeholder="e.g., full-grain leather, RFID blocking, slim cardholder")
    tone = st.selectbox("Brand Tone", ["Luxury & Sophisticated", "Casual & Trendy", "Professional & Bold"])
    
    if st.button("Generate Storefront Copy", type="primary"):
        if prod_name and keywords:
            with st.spinner("Analyzing product details locally..."):
                prompt = f"""
                You are an elite e-commerce copywriter. Write a highly compelling, conversion-focused product description for an online storefront.
                Product Title: {prod_name}
                Key Features: {keywords}
                Tone of Voice: {tone}
                
                Provide the output in three distinct parts:
                1. Catchy Hook Sentence.
                2. Engaging 3-sentence description paragraph.
                3. Bulleted list of key technical highlights.
                """
                
                try:
                    # Send the prompt to LM Studio
                    response = client.chat.completions.create(
                        model="local-model", # LM Studio automatically uses whatever model you have loaded!
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7
                    )
                    st.success("Copy Generated Successfully!")
                    st.markdown("---")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error connecting to LM Studio: {e}. Is the Local Server running?")
        else:
            st.error("Please fill in both the Product Title and Key Features.")

# --- WORKFLOW 2: PINTEREST CONTENT PLANNER ---
with tab2:
    st.subheader("Automate Your Pinterest Content Calendar")
    
    business_goal = st.text_input("What is the primary goal of this campaign?", placeholder="e.g., Drive traffic to my handmade decor storefront")
    target_audience = st.text_input("Who is your target audience?", placeholder="e.g., Gen Z college students, DIY home enthusiasts")
    
    if st.button("Generate 5-Day Pin Strategy", type="primary"):
        if business_goal and target_audience:
            with st.spinner("Mapping out content strategy..."):
                prompt = f"""
                You are a digital marketing strategist specializing in Pinterest traffic generation. 
                Create a 5-day content calendar based on the following:
                Goal: {business_goal}
                Target Audience: {target_audience}
                
                For each of the 5 days, provide:
                - Pin Concept / Idea
                - High-converting Pin Title
                - Description optimized with relevant keywords
                - Visual layout suggestion
                """
                
                try:
                    # Send the prompt to LM Studio
                    response = client.chat.completions.create(
                        model="local-model",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7
                    )
                    st.success("Campaign Calendar Built!")
                    st.markdown("---")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error connecting to LM Studio: {e}. Is the Local Server running?")
        else:
            st.error("Please provide both a business goal and a target audience.")

# --- WORKFLOW 3: OFFLINE ACADEMIC TUTOR ---
with tab3:
    st.subheader("Step-by-Step Concept Breakdown")
    
    subject = st.text_input("Subject Area", placeholder="e.g., Class 12th Accounting or Mathematics")
    concept = st.text_input("Concept to Explain", placeholder="e.g., Ratio Analysis formulas or Cash Flow statements")
    grade_level = st.selectbox("Explanation Depth", ["Beginner (Simple terms)", "Intermediate (Standard formulas)", "Advanced (Complex applications)"])
    
    if st.button("Generate Concept Guide", type="primary"):
        if subject and concept:
            with st.spinner("Breaking down the concept locally..."):
                prompt = f"""
                You are an expert, patient academic tutor. Break down the following concept for a student without using external web searches.
                Subject: {subject}
                Concept: {concept}
                Depth: {grade_level}
                
                Provide the output in three distinct parts:
                1. A simple, 2-sentence summary of what this concept actually is.
                2. A step-by-step breakdown of the core rules or formulas needed.
                3. A practical, real-world example of how to solve a problem using it.
                """
                
                try:
                    # Send the prompt to LM Studio
                    response = client.chat.completions.create(
                        model="local-model",
                        messages=[{"role": "user", "content": prompt}],
                        temperature=0.7
                    )
                    st.success("Study Guide Generated!")
                    st.markdown("---")
                    st.write(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error connecting to LM Studio: {e}")
        else:
            st.error("Please provide both a Subject Area and a Concept.")
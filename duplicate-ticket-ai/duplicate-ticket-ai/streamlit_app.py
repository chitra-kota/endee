import streamlit as st
from sentence_transformers import SentenceTransformer
import numpy as np

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load tickets
with open("tickets.txt", "r") as f:
    tickets = [line.strip() for line in f.readlines()]

# Create embeddings
embeddings = model.encode(tickets)

st.title("Smart Duplicate Ticket Detector")

st.write("Enter a support ticket to find a similar existing ticket.")

query = st.text_input("Enter new support ticket")

if query:
    query_vec = model.encode([query])[0]
    similarity = np.dot(embeddings, query_vec)
    best_match = tickets[np.argmax(similarity)]

    st.success(f"Similar existing ticket: {best_match}")

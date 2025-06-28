import streamlit as st
from modules.manual_parser import load_manual
from modules.fault_assistant import diagnose
from modules.cross_ref import cross_reference

st.title("✈️ AI Aviation Maintenance Assistant")

query = st.text_input("Enter a fault, ATA code, or keyword:")

if query:
    results = load_manual(query)
    st.write("### Search Results")
    for r in results:
        st.markdown(f"**{r['page']}**: {r['snippet']}")

    if st.button("Run Fault Diagnosis"):
        response = diagnose(query)
        st.markdown("### Diagnosis")
        st.info(response)

    if st.button("Cross-Reference"):
        xref = cross_reference(query)
        st.markdown("### Cross-References")
        st.json(xref)

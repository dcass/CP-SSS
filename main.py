import streamlit as st

# -----------------------------
# CP-SSS CALCULATOR STREAMLIT APP
# -----------------------------

st.set_page_config(page_title="CP-SSS Calculator", page_icon="🧠", layout="centered")

st.title("🧠 Cincinnati Prehospital Stroke Severity Scale (CP-SSS)")
st.markdown(
    """
This tool calculates the **Cincinnati Prehospital Stroke Severity Scale (CP-SSS / C-STAT)** score.

> **⚠️ Clinical disclaimer:**  
> This app is for **educational and research use only** and is **not** a substitute for professional medical judgment, local protocols, or real-time consultation with a stroke team.
"""
)

st.markdown("### Patient Assessment Inputs")

with st.form("cpsss_form"):
    st.markdown("#### 1. Conjugate Gaze Deviation")
    gaze = st.radio(
        "Is there conjugate gaze deviation (eyes persistently deviated to one side)?",
        ["No", "Yes"],
        help="Equivalent to NIHSS Best Gaze ≥ 1."
    )

    st.markdown("#### 2. Arm Weakness")
    arm_weakness = st.radio(
        "Is there arm weakness (unable to hold one arm up for 10 seconds)?",
        ["No", "Yes"],
        help="Equivalent to NIHSS arm motor ≥ 2 on either side."
    )

    st.markdown("#### 3. Level of Consciousness – Questions")
    loc_questions = st.radio(
        "Does the patient **incorrectly** answer at least one LOC question (e.g., age, month)?",
        ["No – answers both correctly", "Yes – at least one is incorrect"],
        help="Abnormal if NIHSS LOC questions ≥ 1."
    )

    st.markdown("#### 4. Level of Consciousness – Commands")
    loc_commands = st.radio(
        "Does the patient **fail** at least one simple LOC command (e.g., close eyes, open/close hand)?",
        ["No – follows both commands", "Yes – fails at least one"],
        help="Abnormal if NIHSS LOC commands ≥ 1."
    )

    submitted = st.form_submit_button("Calculate CP-SSS Score")

if submitted:
    score = 0

    # 2 points: conjugate gaze deviation
    if gaze == "Yes":
        score += 2

    # 1 point: arm weakness
    if arm_weakness == "Yes":
        score += 1

    # 1 point: abnormal LOC questions
    if loc_questions.startswith("Yes"):
        score += 1

    # 1 point: abnormal LOC commands
    if loc_commands.startswith("Yes"):
        score += 1

    st.markdown("---")
    st.subheader(f"CP-SSS Score: **{score} / 4**")

    # Simple interpretation based on Katz et al. (Stroke 2015)
    # CP-SSS ≥ 2 was highly sensitive for NIHSS ≥ 15 and for LVO prediction.  [oai_citation:1‡PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4442042/)
    if score >= 2:
        severity_text = "High likelihood of **severe stroke (NIHSS ≥ 15)** and **increased probability of large vessel occlusion (LVO).**"
        color = "red"
    elif score == 1:
        severity_text = "Possible stroke; CP-SSS is low but not zero."
        color = "orange"
    else:
        severity_text = "Low CP-SSS score (0) – low likelihood of **severe** stroke, but stroke is **not excluded**."
        color = "green"

    st.markdown(
        f"""
        <div style="padding: 1rem; border-radius: 0.5rem; border: 1px solid #ccc;">
            <strong>Interpretation:</strong><br>
            <span style="color:{color};">{severity_text}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
> **Important:**  
> - CP-SSS is designed to help identify patients who may benefit from direct transport to a **Comprehensive Stroke Center**.  
> - A score ≥ 2 has been shown to have high sensitivity for severe strokes and for large vessel occlusion, but **does not replace imaging or full clinical assessment**.  [oai_citation:2‡PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4442042/)
        """
    )

# Optional: references section
with st.expander("Show references"):
    st.markdown(
        """
- Katz BS, McMullan JT, Sucharew H, et al. **Design and Validation of a Prehospital Scale to Predict Stroke Severity: The Cincinnati Prehospital Stroke Severity Scale.** *Stroke.* 2015;46(6):1508-1512.  [oai_citation:3‡PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4442042/)
- American Heart Association / local stroke protocols as applicable.
        """
    )

import streamlit as st
import random
import re

st.set_page_config(page_title="AI Content Generator", page_icon="✍️", layout="centered")

st.title("✍️ AI Content Generator")
st.caption("WeIntern Week 2 — Project 3 | Free starter version")
st.write("Generate blog drafts, social captions, or summaries from your topic. This starter uses prompt templates and Python so you can learn each part before connecting a free AI backend.")

CONTENT_TYPES = ["Blog Post", "Social Media Caption", "Text Summary"]
TONES = ["Professional", "Friendly", "Creative", "Informative", "Persuasive"]

def build_prompt(topic, tone, content_type, length):
    """Build the instruction that will guide a content generator."""
    return (
        f"Create a {content_type.lower()} about: {topic}. "
        f"Tone: {tone.lower()}. Target length: {length}. "
        "Stay relevant to the topic, use clear language, and avoid unsupported facts."
    )

def generate_template_content(topic, tone, content_type, length):
    """A transparent offline starter generator; not a real language model."""
    topic = topic.strip().rstrip(".")
    if content_type == "Social Media Caption":
        endings = {
            "Professional": "Small steps and thoughtful choices can make a meaningful difference.",
            "Friendly": "Let’s learn, try something new, and grow together!",
            "Creative": "A fresh idea today could become tomorrow’s big thing ✨",
            "Informative": "Keep exploring the details and turn knowledge into action.",
            "Persuasive": "Start today—your next step could make all the difference."
        }
        return f"{topic}: ideas worth exploring, lessons worth sharing, and progress worth celebrating. {endings[tone]} #Learning #Ideas"
    if content_type == "Text Summary":
        return (
            f"Summary of {topic}: This topic focuses on its main ideas, practical value, "
            "and possible applications. A useful summary should identify the central message, "
            "highlight the most important supporting points, and explain why they matter. "
            "Add verified source details when accuracy is important."
        )
    paragraphs = [
        f"## Introduction\n{topic} is an important subject to explore because it connects ideas with practical decisions. "
        f"This draft takes a {tone.lower()} approach and introduces the topic in clear, accessible language.",
        f"## Key ideas\nA useful way to understand {topic.lower()} is to break it into smaller questions: what it means, "
        "why it matters, and how it can be applied. Looking at these questions separately makes the subject easier to understand.",
        f"## Practical applications\nIn practice, progress starts with a clear goal, reliable information, and manageable steps. "
        f"For {topic.lower()}, readers can begin by learning the fundamentals, comparing options, and testing ideas carefully.",
        f"## Conclusion\n{topic} offers several points worth considering. Continue learning from trustworthy sources, "
        "check important claims, and adapt the ideas to the needs of your audience."
    ]
    return "\n\n".join(paragraphs)

with st.form("content_form"):
    topic = st.text_input("Topic", placeholder="e.g., How AI helps students learn")
    content_type = st.selectbox("Content type", CONTENT_TYPES)
    tone = st.selectbox("Tone", TONES)
    length = st.select_slider("Target length", options=["Short", "Medium", "Long"], value="Medium")
    submitted = st.form_submit_button("Generate content")

if submitted:
    if not topic.strip():
        st.error("Please enter a topic before generating content.")
    else:
        st.session_state["topic"] = topic.strip()
        st.session_state["content_type"] = content_type
        st.session_state["tone"] = tone
        st.session_state["length"] = length
        st.session_state["draft"] = generate_template_content(topic, tone, content_type, length)
        st.session_state["prompt"] = build_prompt(topic, tone, content_type, length)

if "draft" in st.session_state:
    st.divider()
    st.subheader("Generated draft")
    st.info("Starter mode: this is template-based output, not an actual AI model response. In a later step, we will connect a free AI backend.")
    st.markdown(st.session_state["draft"])
    words = re.findall(r"\b[\w'-]+\b", st.session_state["draft"])
    st.caption(f"Word count: {len(words)}  |  Character count: {len(st.session_state['draft'])}")
    st.download_button("Download draft (.txt)", data=st.session_state["draft"], file_name="generated_content.txt", mime="text/plain")
    with st.expander("View prompt template"):
        st.code(st.session_state["prompt"], language="text")
    if st.button("Regenerate / refine draft"):
        st.session_state["draft"] = generate_template_content(
            st.session_state["topic"], st.session_state["tone"],
            st.session_state["content_type"], st.session_state["length"]
        )
        st.rerun()

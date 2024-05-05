import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Portfolio", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/OIP.png")
img_lottie_animation = Image.open("images/download.png")
img_project_1 = Image.open("images/project_1.png")
img_project_2 = Image.open("images/project_2.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hii, I am Roshan :wave:")
    st.title("I'm a software engineer")
    st.write(
        "I'm all about crafting cool stuff with technology. I work with Python, Flutter, IoT, and a bit of MERN stack.\n"
        "My motto is simple: Anything's possible with the right mix of tech.\n"
        "My specialty? Bringing together hardware and software to make awesome things happen."



    )


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            During my tenure as a product manager, I was entrusted with the management of all real-time projects within the organization.:
            - Drawing upon my background as a software engineer, I seamlessly integrated my application and web development skills into my role as a product manager.
            - Leveraging Python's rich ecosystem of libraries and frameworks, we were able to deliver robust and efficient solutions that exceeded client expectations.
            - Whether it was designing embedded systems, developing device drivers, or optimizing performance-critical code, my expertise in C language played a pivotal role in ensuring the success of IoT initiatives.
            - Python was our go-to for most projects. It helped with everything from integration of hardware for real-time physical products to web development.

            
            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Motion Detection Alert System for Private Housing")
        st.write(
            """
             Enhancing security for private housing communities.
             This involved defining user requirements, designing system architecture, and ensuring timely delivery.
            
             
            """
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Distress Hand Signal Detection with Object Alert System")
        st.write(
            """
            Managing the development of an intelligent distress signal detection system.
            I collaborated with engineers to implement advanced computer vision algorithms. 
            The system detects distress signals and alerts authorities while also tracking and marking relevant objects for enhanced situational awareness.
            """
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_1)
    with text_column:
        st.subheader("Low-Code Projects - Travel Booking")
        st.write(
            """
            I've done the implementation of low-code solutions such as a complete travel booking system using the Pega framework. 
            This involved leveraging my expertise in low-code development to deliver robust and scalable solutions within tight deadlines.
            """
        )

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project_2)
    with text_column:
        st.subheader("AI-Based Mental Health Detection - Upcoming Freelance College Project")
        st.write(
            """
            Spearheading a groundbreaking project, I guided the development of an AI-based mental health detection system. 
            By analyzing users' music history and phone data, the system detects early signs of mental health issues and provides personalized treatment suggestions. 
            This project is currently in the final stages of development and holds immense potential for societal impact.
            """
        )

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/roshanrajofficial.f@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

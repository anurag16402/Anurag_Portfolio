from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file= current_dir / "Images" / "Anurag_Resume_GV.pdf"
resume_file= ("Images/Anurag_Resume_GV.pdf")
css_file = current_dir / "Style" / "style.css"
st.set_page_config(layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()


lottie_coder= load_lottieurl('https://lottie.host/ef3cc8e5-2736-485f-9066-20119843c294/1CPJAT5QIl.json')
lottie_contact=load_lottieurl('https://lottie.host/2a28fb7b-89ba-4947-8a81-469acb95e234/M1wTU18DNm.json')
image = Image.open(current_dir / "Images" / "project.png")
image2 = Image.open(current_dir / "Images" / "programming.png")
image_mine = Image.open(current_dir / "Images" / "image_copy.png")
image_data = Image.open(current_dir / "Images" / "business-analyst.png")
github = Image.open(current_dir / "Images" / "github.png")
linkedin = Image.open(current_dir / "Images" / "linkedin.png")
CV = Image.open(current_dir / "Images" / "cv.png")

with st.container():
    col7, col8, = st.columns([2,1])
    with col7:
        st.subheader("Hey Guys :wave:")
        st.title("I'm Anurag Nagvanshi")
        st.write("""Web Developer | Back-end Developer | Python Developer""")
        with st.container():
            col9, col10,col11,= st.columns(3, gap="small")
            with col9:
                st.image(github, width=25) 
                st.markdown("[Github](https://github.com/anurag16402)")
            with col10:
                st.image(linkedin, width=25)
                st.markdown("[LinkedIn](https://www.linkedin.com/in/anurag-nagvanshi-519640232/)")
            with col11:
                st.image(CV, width=25)
                st.download_button(
                    label=" Download Resume",
                    data= PDFbyte,
                    file_name="Anurag_Resume_GV.pdf",
                    mime="application/octet-stream"
                )

    with col8:
        st.image(image_mine, width=200, )


with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Projects','Contact'],
        icons=['person','code-slash','chat-left-text-fill'],
        orientation = 'horizontal'
    )
if selected =='About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.title("Undergrad at PSIT")
            st.write("I am a BTech graduate majored in Electronics and Communication Engineering. I have understanding of DSA, Python, OOPs Concepts.")
            st.write("I have expirience HTML/CSS, Django, Streamlit and Generative AI.")
            st.write("I'm actively looking for oppurtunities to kickstart my journey,learn from experts and make difference within a forward thinking organization")
        with col2:
            st_lottie(lottie_coder)
    
    st.write("---")

    with st.container():
        col3,col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
            - PSIT(2020-2024)
                - Electronics and Communication Enginnering(ECE)
                - 7.6 cgpa
            - Intermediate School(2020)
                - K.V. No.1,A.F.S,Chakeri, Kanpur
                - 85.2%
            - High School (2018)
                - K.V No.1,A.F.S,Chakeri, Kanpur
                - 82%
                         
""")
        with col4:
            st.subheader("""
            Experience
            - Accenture
                ~ Virtual Internship
                - 1 month
                - Remote
            """)
if selected=="Projects":
    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns((1,2))
        with col5:
            st.image(image_data, width=200)
            st.write("##")
            st.write("##")
            st.image(image2, width=200)
            st.write("##")
            st.write("##")
            st.image(image, width=200)
        with col6:

            st.subheader("Spell Corrector")
            st.write("""
- Implements a part-of-speech tagger using the Viterbi algorithm to correct spelling mistakes in text.
- Identifies and corrects errors by analyzing parts of speech, using edit distance for closest word matching.
- Utilizes NLTK, dynamic programming, robust error handling, and logging for efficient, accurate spelling correction.
                      """)
            st.markdown("[Visit Github Repo](https://github.com/anurag16402/Spell-Corrector)")
            st.write("##")
            st.write("##")
            st.subheader("Pencil Sketch with Python and Machine Learning")
            st.write("""
- Convert images to pencil sketches using Python and OpenCV
- Apply grayscale conversion to the input image using OpenCV.
- Invert the grayscale image and blend with edge-detected image for sketch effect.""")
            st.markdown("[Visit Github Repo](https://github.com/anurag16402/Pencil-Sketch-with-Python-and-Machine-Learning)")
            st.write("##")
            st.write("##")
            st.subheader("Library Management system with User Authentication")
            st.write("""
- To develop a comprehensive Library Management System which also includes user authentication to 
manage access and roles effectively.
- Users can register and log in to the system with a username and password.
- Command-line interface with intuitive prompts for user interaction. Clear and concise messages to guide 
users through various operations.
""")
            st.markdown("[Visit Github Repo](https://github.com/anurag16402/Library-Management-System-With-User-Autentication)")

if selected == "Contact":
    st.header("Get in touch")
    st.write('##')

    contact_form = """
<div class="container">
  <form target="_blank" action="https://formsubmit.co/anuragnagvanshi164@gmail.com" method="POST">
    <div class="form-group">
      <div class="form-row">
        <div class="col">
          <input type="text" name="name" class="form-control" placeholder="Full Name" required>
        </div>
        <div class="col">
          <input type="email" name="email" class="form-control" placeholder="Email Address" required>
        </div>
      </div>
    </div>
    <div class="form-group">
      <textarea placeholder="Your Message" class="form-control" name="message" rows="5" required></textarea>
    </div>
    <button type="submit" class="btn btn-lg btn-dark btn-block">Send</button>
  </form>
</div>
    

    """
    left_col,right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html= True)
    with right_col:
        st_lottie(lottie_contact, height=300)



from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="My webpage",page_icon= ":tada:",layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
      return None
    return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

    local_css("New folder/style.css 1.txt")

lottie_coding = load_lottieurl("https://lottie.host/727b15f5-a7e0-4214-994e-005185c2cc82/OoO1qHf1sU.json")
img_lottie_animation = Image.open("images/Calories.jpg")
img_food = Image.open("images/Food.jpg")
img_pie_chart_F= Image.open("images/pie chart F.jpg")
img_pie_chart_U= Image.open("images/pie chart U.jpg")
Thumbnail_1=Image.open("images/Thumbnail 1.jpg")
Thumbnail_2=Image.open("images/Thumbnail 2.jpg")

with st.container():
    st.subheader("Welcome To")
    st.header("CC FITNESS & SPORTS:wave:")
    st.write("##")
    st.write("""This site is designed to guide people to maintain themselves according to their need. 
            It will give you a path to get your requirements without any expenses. """)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Fitness,sports and Health")
        st.write("##")
        st.write("""- Fitness is a state of health and well being and more specifically ,The ability to perfome aspects of sports,Occupation and Daily activities.""")
        st.write("- Sports is an activity where Physical exertion and skills are involved,and an individual or team competes againts another or other teams/players for entertainment.")
        st.write("- Health is a state of complete physical,mental,absence of disease or infirmity .")

        with st.container():
            st.write("---")
            st.header("Rate of Fit and Unfit peoples")
            st.write("###")
            image_column,text_column = st.columns((4,6))
            with image_column:
                st.image(img_pie_chart_F)
            with text_column:
                st.subheader("Among fit people 53% are male and 47% are female.")
        with st.container():
            image_column, text_column = st.columns((4,6))
            with image_column:
                st.image(img_pie_chart_U)
            with text_column:
                st.subheader("Among unfit people 47% are male and 53% are female.")

        with st.container():
            st.write("---")
            st.header("Calories & Food Should Be Consumes")
            st.write("##")
            image_column,text_column = st.columns((12,9))
            with image_column:
                st.image(img_lottie_animation)
            with text_column:
                st.subheader("Calories should be consumed by different age group of people:")
                st.write("From this graph you can see how much calories a male body or a female body requires in a particular age.")
        with st.container():
            image_column,text_column=st.columns((12,9))
            with image_column:
                st.image(img_food)
            with text_column:
                st.subheader("Types of foods should be consumed by different age group of people:")
                st.write("""From this graph, we can know which types of foods our body requires.
                       You can clearly see the rate of requirements of root products, i.e. 36.15%.""")
            with right_column:
                st_lottie(lottie_coding,height=300,key="coding")

            with st.container():
                st.write("---")
                st.header("Related Videos")
                st.write("##")
                image_column, text_column = st.columns((20, 20))
                with image_column:
                    st.image(Thumbnail_1)
                with text_column:
                    st.subheader("Fitness tips for 18-20 years age groups")
                    st.write("Learn what's right for the natural growth of your body. With this, along with maintaining your body, you can also keep your mental health healthy. Click the link given below.")
                    st.markdown("[Watch Video...](https://youtu.be/BeUMnnDJIy8?si=ragOgIr3Is-WsB85)")
            with st.container():
                st.write("-")
                st.write("#")
                image_column, text_column = st.columns((8, 9))
                with image_column:
                    st.image(Thumbnail_2)
                with text_column:
                    st.subheader("Fitness tips for 20-31 years age groups")
                    st.write("Learn what is right for you after teen age. This information will give you a reason to get attracted towards natural exercises and sports. Click the link given below.")
                    st.markdown("[Watch Video...](https://youtu.be/lQgccv3ed10?si=XLA7wi1H4Ilhh7Qw)")
            with st.container():
                st.write("--- ")
                st.header("Get in touch with us! ")
                st.write("## ")
                contact_form = """
                        <form action="https://formsubmit.co/ccfitnessandsports@gmail.com" method="POST">
                            <input type="hidden" name="_captcha" value="false">
                            <input type="text" name="name" placeholder="your name" required>
                            <input type="email" name="email" placeholder="your email" required>
                            <textarea name="message" placeholder="your message here" required></textarea>
                            <button type="submit">Send</button>
                        </form>
                        """
                st.markdown(contact_form, unsafe_allow_html=True)

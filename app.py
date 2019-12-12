import streamlit as st
st.title("sai vamshi")
st.header(" this is my first code in streamlit")
st.subheader("this is sub header")
st.text("hello")
st.markdown("Iam a markdown")
st.success("Error")
st.info("information")
st.warning("yoo iam warning")
st.error("Variable not found ")
st.warning("Iam the warning")
st.exception("NullPointerException ('why why is it always you')")
st.help(range)
st.write("Text with write")
st.write(range(1,10))
from PIL import Image
img=Image.open("token.png")
st.image(img)
#v_file=open("sample.mp4","rb").read()
#st.video(v_file)
if st.checkbox("Show/Hide"):
    st.text("Yoo iam here")
#radi btn

status=st.radio("what is your stauts",["Active","Inactive"])
if status=='Active':
    st.success("Yoo")
else:
    st.success("Iam inactive")
occupation=st.selectbox("That are you",["Dog","cat","Man","Eagle"])
st.write("You are :",occupation)
mlsel=st.multiselect("Where are you",["India","Amarica","Africa","Nepal","Bhutan"])
st.write("ok u selected",len(mlsel),"u have selected")
level=st.slider("Drag me ",1,5)
st.write("You Draged:",level)

if st.button("say! hi"):
    st.write("Hi! bro")

firstname=st.text_input("Hi agin! what is u r name","Type here")
st.write("Your name is :",(firstname))

st.balloons()

st.sidebar.header(" yoo iam a sidbar")
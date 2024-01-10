import streamlit as st

st.set_page_config(
    page_title="Kaiwen Men - University of Washington",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    # st.markdown(
    #     """
    # ![avatar](/Users/mkw/Documents/MSTI/TECHIN510/TECHIN510_lab1/IMG_0118.JPG)
    # <style>
    # img {
    #     width: 100%;
    #     border-radius: 50%;
    # }
    # </style>

    # """,
    #     unsafe_allow_html=True,
    # )
    st.image('IMG_0118.JPG')
with col2:
    st.markdown(
        """
    # Kaiwen Men (She/Her)
                
    - Graduate Student in [University of Washington](https://www.washington.edu/) and [Tsinghua University](https://www.tsinghua.edu.cn/)
    - Graduate Student Researcher at [Knowledge Engineering Group(KEG) Lab](https://keg.cs.tsinghua.edu.cn/)
    """
    )

st.markdown(
    """
# Education

- Global Innovation EXchange @[University of Washington](https://www.washington.edu/) & [Tsinghua University](https://www.tsinghua.edu.cn/)
- Department of Automation @[Tsinghua University](https://www.tsinghua.edu.cn/)
"""
)

st.markdown(
    """
# Work Experience

- NLP research intern @[Zhipu.AI](https://zhipuai.cn/)
- Algorithm research intern @[Beijing Megvii Co., Ltd](https://en.megvii.com/)
- Software Development Engineer Intern @[Beijing Academy of Blockchain and Edge Computing](https://riscv.org/member/beijing-academy-of-edge-computing/)
"""
)

st.markdown(
    """
# Hobbies and Interests

- :running: Running
- :swimmer: Swimming
- :bicyclist: Bicycling
"""
)

st.markdown(
    """
# Interesting Projects

- [Lateral Thinking Puzzle](https://mkw18-lateralthinkingpuzzle.hf.space)
- [Crowdsourcing Translation Platform](https://github.com/mkw18/Crowdsourcing-translation-platform)
- [Phone Charging Circuit System](https://github.com/mkw18/ChargePhone)
"""
)

# st.markdown(
#     """
# # Contact
# """)
# col1, col2, col3 = st.columns(3)

# # Card with image and text
# for col in [col1, col2, col3]:
#     col.markdown(
#         """
#         <style>
#         .profile-img img {
#             width: 100%;
#             border-radius: 10%;
#         }
#         </style>

#         <div class="profile-img">

#         ![](https://avatars.githubusercontent.com/u/7678108?v=4)
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

# col1, col2, col3 = st.columns(3)

# # Card with image and text
# for col in [col1, col2, col3]:
#     col.markdown(
#         """
#         <style>
#         .profile-img img {
#             width: 100%;
#             border-radius: 10%;
#         }
#         </style>

#         <div class="profile-img">

#         ![](https://avatars.githubusercontent.com/u/7678108?v=4)
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )


# ft = """
# <style>
# a:link , a:visited{
# color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
# background-color: transparent;
# text-decoration: none;
# }

# a:hover,  a:active {
# color: #0283C3; /* theme's primary color*/
# background-color: transparent;
# text-decoration: underline;
# }

# #page-container {
#   position: relative;
#   min-height: 10vh;
# }

# footer{
#     visibility:hidden;
# }

# .footer {
# position: relative;
# left: 0;
# top:230px;
# bottom: 0;
# width: 100%;
# background-color: transparent;
# color: #808080; /* theme's text color hex code at 50 percent brightness*/
# text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
# }
# </style>

# <div id="page-container">

# <div class="footer">
# <p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
# with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
# </div>

# </div>
# """
# st.write(ft, unsafe_allow_html=True)
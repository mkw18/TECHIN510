import streamlit as st

st.set_page_config(
    page_title="Kaiwen Men - University of Washington",
    page_icon=":woman_student:",
    layout="centered",
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![avatar](https://raw.githubusercontent.com/mkw18/TECHIN510-Lab1/main/IMG_0118.JPG)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('IMG_0118.JPG')
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

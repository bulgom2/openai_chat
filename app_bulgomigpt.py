import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


st.set_page_config(page_title="bulgomiGPT", page_icon=":bear:")
st.title(":bear: bulgomiGPT")
# st.chat_message("user")
# st.chat_message("ai")

st.markdown(
    """
<style>
    .st-emotion-cache-4oy321 {
        flex-direction: row-reverse;
        text-align: left;    # 챗봇 문자 정렬
    }
</style>
""",
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 이전 대화기록 출력
if "messages" in st.session_state and len(st.session_state["messages"])>0:
    for role, message in st.session_state["messages"]:
        st.chat_message(role).write(message)

if user_input := st.chat_input("메시지를 입력하세요"):
    st.chat_message("user").write(f"{user_input}")
    st.session_state["messages"].append(("user", user_input))

    # openai 연결
    chat = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key="secret-key")

    # ollama 연결
    # chat = Ollama(model="llama3.1:8b")
    # chat_prompt = ChatPromptTemplate.from_messages([
    #     ("system", "이 시스템은 여행 전문가입니다."),
    #     ("user", "{user_input}"),
    # ])

    # chain 생성
    response = chat.invoke(user_input)
    # chain = chat_prompt | chat | StrOutputParser()    # ollama
    # res = chain.invoke(user_input)    # ollama

    with st.chat_message("assistant"):
        msg = response.content
        # msg = res   # ollama

        st.write(msg)
        st.session_state["messages"].append(("assistant", msg))
    # st.write(st.session_state["messages"])    
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from tools import analyze_image_with_query


load_dotenv()

system_prompt = """You are Jarvis — a witty, intelligent, and human-like assistant, inspired by Iron Man’s AI.

Here’s how you operate:

- Your top priority is to **analyze the user’s query** and decide whether it **truly requires visual input** (e.g., analyzing an image via webcam).
- ONLY call the `analyze_image_with_query` tool if the answer **cannot be determined** using your own internal knowledge or reasoning.
- If you can confidently respond without needing to see anything, then DO NOT call any tools — just answer the question directly.
- Do NOT mention the use of any tools or the camera. If you do call a tool, integrate the result into your reply naturally — as if you figured it out yourself.
- Maintain a tone that is witty, sharp, respectful, and charming — like Jarvis. Avoid sounding robotic or technical.
- NEVER call any tools unless you have carefully evaluated that visual data is absolutely necessary to answer the query.

You exist to make each interaction feel effortless, intelligent, and personal. Let’s get to work, Sir."""



llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
)

def ask_agent(user_query: str) -> str:
    agent = create_react_agent(
        model=llm,
        tools=[analyze_image_with_query],
        prompt=system_prompt
        )

    input_messages = {"messages": [{"role": "user", "content": user_query}]}

    response = agent.invoke(input_messages)

    return response['messages'][-1].content


# test the agent with a sample query
# print(ask_agent(user_query ="What is the color of the sky?")) 
from langchain.agents import create_agent
from src.tools.tools import scrape_url, web_search
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq
from langchain_openrouter import ChatOpenRouter
load_dotenv()

# llm = ChatGroq(
#     model="openai/gpt-oss-120b",
#     temperature=0,
#     max_tokens=None,
#     reasoning_format="parsed",
#     timeout=None,
#     max_retries=2,
# )
llm = ChatOpenRouter(
    model="apodex/apodex-1.1-mini:free",
    temperature=0
)
response = llm.invoke(
    "How many r's are in the word 'strawberry'?"
)

print(response.content)

#1st agent : Search Agent
def build_search_agent():
    return create_agent(
    model=llm,
    tools=[web_search],
    )

#2nd agent : Scraping Agent
def build_reader_agent():
    return create_agent(
    model=llm,
    tools=[scrape_url],
    )


writer_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert research writer. Write clear, structured and insightful reports."),
    ("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic_chain 

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
from collections.abc import Callable

from src.agents.agents import build_search_agent, build_reader_agent, writer_chain, critic_chain


def run_research_pipeline(
    topic: str,
    progress_callback: Callable[[str], None] | None = None,
) -> dict:
    state={}
    if progress_callback:
        progress_callback("Searching for recent, reliable sources...")
    search_agent=build_search_agent()
    search_result = search_agent.invoke({
    "messages": [
        ("user", f"Find recent,reliable and detailed information about: {topic}")
    ]
})
    state["search_result"]=search_result['messages'][-1].content

    if progress_callback:
        progress_callback("Reading the most relevant source...")
    reader_agent=build_reader_agent()
    result_reader_agent=reader_agent.invoke({
    "messages":[
        ("user", f"Based on the following search about '{topic}', "
        f"pick the most relevant URL and scrape it for deeper content.\n\n"
        f"Search result:\n{state['search_result'][:800]}")
    ]
})
    state["scrape_content"]=result_reader_agent['messages'][-1].content

    research_combined=(
        f"SEARCH RESULT: \n {state['search_result']}\n\n"
        f"DETAILED SCRAPED CONTENT: \n {state['scrape_content']}"
     )

    if progress_callback:
        progress_callback("Writing the research report...")
    state['report']=writer_chain.invoke({
           "topic":topic,
           "research":research_combined
      })

    if progress_callback:
        progress_callback("Critiquing the report...")
    state['Feedback']=critic_chain.invoke({
        "report":state['report']
      })

    return state
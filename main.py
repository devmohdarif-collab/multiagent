import streamlit as st

from src.pipeline.pipelines import run_research_pipeline

st.set_page_config(
	page_title="Margin | Research Studio",
	page_icon="M",
	layout="wide",
	initial_sidebar_state="collapsed",
)

st.markdown(
	"""
	<style>
	@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Manrope:wght@400;500;600;700;800&display=swap');

	:root {
		--ink: #20231f;
		--muted: #74776f;
		--paper: #f6f7f3;
		--line: #dfe1d9;
		--accent: #b84f3b;
		--accent-dark: #963b2a;
		--highlight: #e8edcf;
		--surface: #ffffff;
	}
	.stApp { background: var(--paper); color: var(--ink); }
	.block-container { max-width: 1480px; padding: 2.8rem 2.8rem 4rem !important; }
	h1, h2, h3, p, label, input, textarea, button { font-family: 'Manrope', sans-serif !important; }
	h1, h2, h3, p, label { color: var(--ink); }
	h1 { font-size: 2.65rem !important; font-weight: 700 !important; line-height: 1.08 !important; margin: 0.45rem 0 0.35rem !important; }
	h2 { font-size: 1.35rem !important; font-weight: 700 !important; }
	h3 { font-size: 1.05rem !important; font-weight: 700 !important; }
	.eyebrow, .mono-label { font: 500 0.68rem 'DM Mono', monospace; letter-spacing: 0.04em; text-transform: uppercase; }
	.eyebrow { color: var(--accent); }
	.deck { color: var(--muted); font-size: 0.92rem; }
	.status-text { font: 500 0.68rem 'DM Mono', monospace; color: var(--muted); text-align: right; padding-top: 0.6rem; }
	.brand-lockup { display: flex; align-items: center; gap: 0.65rem; min-height: 2rem; margin: 0 0 1rem; overflow: visible; color: var(--ink); font: 700 0.73rem 'DM Mono', monospace; letter-spacing: 0.04em; text-transform: uppercase; }
	.brand-mark { display: inline-flex; width: 1.7rem; height: 1.7rem; align-items: center; justify-content: center; background: var(--accent); color: white; border-radius: 50%; font: 700 0.85rem 'Manrope', sans-serif; }
	.st-key-brief-panel { background: #eeefe9; border-top: 2px solid var(--ink); padding: 1.35rem; }
	.st-key-brief-panel .mono-label { color: var(--accent); }
	.st-key-brief-panel [data-testid="stTextArea"] textarea { background: var(--surface); border: 1px solid #d6d8d0; border-radius: 3px; color: var(--ink); font-size: 0.9rem; }
	.st-key-brief-panel [data-testid="stTextArea"] textarea:focus { border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent); }
	.st-key-brief-panel [data-testid="stFormSubmitButton"] button { width: 100%; min-height: 2.9rem; background-color: var(--accent) !important; color: #ffffff !important; border: 1px solid var(--accent) !important; border-radius: 3px; font-size: 0.86rem; font-weight: 800; transition: background-color 140ms ease, border-color 140ms ease, transform 140ms ease; }
	.st-key-brief-panel [data-testid="stFormSubmitButton"] button * { color: #ffffff !important; }
	.st-key-brief-panel [data-testid="stFormSubmitButton"] button:hover { background-color: var(--accent-dark) !important; border-color: var(--accent-dark) !important; color: #ffffff !important; transform: translateY(-1px); }
	.st-key-brief-panel [data-testid="stFormSubmitButton"] button:focus-visible { outline: 3px solid var(--highlight); outline-offset: 2px; }
	.st-key-results-workspace { background: var(--surface); border-top: 2px solid var(--ink); padding: 1.35rem 1.6rem; min-height: 30rem; }
	.st-key-results-workspace .stMarkdown p { line-height: 1.75; }
	.output-meta { display: flex; justify-content: space-between; border-bottom: 1px solid var(--line); padding-bottom: 0.7rem; margin-bottom: 1.1rem; }
	.output-meta span { font: 500 0.66rem 'DM Mono', monospace; color: var(--muted); text-transform: uppercase; }
	.step-row { border-top: 1px solid var(--line); padding: 0.75rem 0; color: var(--muted); font-size: 0.8rem; }
	.step-row b { display: inline-block; width: 2rem; color: var(--accent); font: 500 0.7rem 'DM Mono', monospace; }
	.empty-title { margin-top: 3rem; font-size: 1.4rem; font-weight: 700; }
	.empty-copy { max-width: 30rem; color: var(--muted); line-height: 1.7; }
	button[data-baseweb="tab"] { font: 600 0.75rem 'DM Mono', monospace; text-transform: uppercase; }
	[role="tablist"] { gap: 1rem; }
	[data-testid="stExpander"] { border: 1px solid var(--line); border-radius: 3px; }
	[data-testid="stExpander"] summary { font: 600 0.8rem 'Manrope', sans-serif; }
	[data-testid="stStatusWidget"] { border: 1px solid var(--line); border-radius: 3px; }
	.stAlert { border-radius: 3px; }
	@media (max-width: 760px) {
		.block-container { padding: 2rem 1rem 2.5rem !important; }
		h1 { font-size: 2rem !important; }
		.st-key-brief-panel, .st-key-results-workspace { padding: 1rem; }
		.status-text { text-align: left; padding: 0.2rem 0 0.8rem; }
	}
	</style>
	""",
	unsafe_allow_html=True,
)

st.markdown(
	'<div class="brand-lockup"><span class="brand-mark">M</span> Margin <span style="color:#b84f3b">/</span> AI research studio</div>',
	unsafe_allow_html=True,
)
header, run_status = st.columns([4, 1])
with header:
	st.markdown('<div class="eyebrow">AI research assistant &nbsp; / &nbsp; 01</div>', unsafe_allow_html=True)
	st.title("Your AI research workspace.")
	st.markdown('<p class="deck">Ask a question. Research agents find sources, build a memo, and critically review their findings.</p>', unsafe_allow_html=True)
with run_status:
	status = "COMPLETE" if st.session_state.get("research_result") else "READY"
	st.markdown(f'<div class="status-text">RUN STATUS &nbsp; {status}</div>', unsafe_allow_html=True)
st.divider()

brief_column, workspace_column = st.columns([0.9, 2.1], gap="large")

with brief_column:
	with st.container(key="brief-panel"):
		st.markdown('<div class="mono-label">01 &nbsp; / &nbsp; New inquiry</div>', unsafe_allow_html=True)
		st.markdown("## What do you want to know?")
		st.caption("Give the AI research team a focused question to investigate.")
		with st.form("research_form"):
			topic = st.text_area(
				"Research question",
				placeholder="For example: How is AI changing entry-level software roles?",
				height=125,
				label_visibility="collapsed",
			)
			submitted = st.form_submit_button("Start AI research", type="primary", use_container_width=True)
		st.markdown('<div class="mono-label" style="margin-top:1.4rem">The process</div>', unsafe_allow_html=True)
		st.markdown('<div class="step-row"><b>01</b> Discover credible sources</div>', unsafe_allow_html=True)
		st.markdown('<div class="step-row"><b>02</b> Extract supporting evidence</div>', unsafe_allow_html=True)
		st.markdown('<div class="step-row"><b>03</b> Draft and critically review</div>', unsafe_allow_html=True)

with workspace_column:
	with st.container(key="results-workspace"):
		result = st.session_state.get("research_result")

		if submitted:
			if not topic.strip():
				st.warning("Add a research question before starting the run.")
			else:
				try:
					with st.status("Assembling the research...", expanded=True) as progress:
						def update_progress(message: str) -> None:
							progress.update(label=message, state="running")

						result = run_research_pipeline(topic.strip(), progress_callback=update_progress)
						progress.update(label="Research complete", state="complete", expanded=False)
					st.session_state["research_result"] = result
					st.session_state["research_topic"] = topic.strip()
				except Exception as error:
					st.error(f"The research run could not be completed: {error}")

		if result:
			st.markdown('<div class="output-meta"><span>Research memo</span><span>Reviewed output &nbsp; / &nbsp; 01</span></div>', unsafe_allow_html=True)
			st.subheader(st.session_state.get("research_topic", "Research findings"))
			report_tab, critique_tab, source_tab = st.tabs(["The memo", "Critical review", "Sources"])
			with report_tab:
				st.markdown(result.get("report", "No report was returned."))
			with critique_tab:
				st.markdown(result.get("Feedback", "No critique was returned."))
			with source_tab:
				st.markdown("### Search findings")
				st.text(result.get("search_result", "No search results were returned."))
				st.markdown("### Extracted source")
				st.text(result.get("scrape_content", "No source content was extracted."))
		else:
			st.markdown('<div class="output-meta"><span>Research memo</span><span>Awaiting brief</span></div>', unsafe_allow_html=True)
			st.markdown('<div class="empty-title">Your next question, clearly answered.</div>', unsafe_allow_html=True)
			st.markdown('<p class="empty-copy">Submit an inquiry to create a research memo. Findings, a critical review, and source material will live together here.</p>', unsafe_allow_html=True)

import os
from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the language model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

# --- DEFINE THE SEARCH TOOL ---
# Use SerperDevTool for reliable web search
search_tool = SerperDevTool()

# --- AGENT DEFINITIONS ---
# All agent definitions below are correct and do not need to be changed.

# 1. Research Strategist Agent
research_strategist = Agent(
    role="Research Strategist",
    goal="To break down a user's query into a set of specific, answerable research questions.",
    backstory=(
        "You are an expert strategist at a top-tier consulting firm. "
        "Your skill is in taking broad, complex topics and deconstructing them "
        "into a clear, logical, and actionable research plan. You identify the "
        "key facets of a topic—political, economic, technological, social—to ensure "
        "a comprehensive analysis."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# 2. Web Search Specialist Agent
web_search_specialist = Agent(
    role="Web Search Specialist",
    goal="To find the most relevant, up-to-date, and credible information on the web based on a set of research questions.",
    backstory=(
        "You are a master of digital investigation. Armed with advanced search techniques "
        "and a critical eye for source credibility, you can unearth key facts, data, "
        "and expert opinions from the vast expanse of the internet. You prioritize "
        "reputable sources like academic papers, official reports, and established news outlets."
    ),
    llm=llm,
    tools=[search_tool],
    verbose=True,
    allow_delegation=False,
)

# 3. Data Analyst Agent
data_analyst = Agent(
    role="Data Analyst",
    goal="To synthesize raw data and search results into a structured, factual analysis.",
    backstory=(
        "You are a meticulous data analyst with a knack for seeing the story in the numbers. "
        "You take raw information—articles, reports, statistics—and distill it into "
        "key findings, trends, and structured bullet points. You identify conflicting data "
        "and highlight the most critical facts for the forecasting team."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# 4. Probability Forecaster Agent (Quantitative Version)
probability_forecaster = Agent(
    role="Quantitative Risk Analyst and Forecaster",
    goal=(
        "To analyze the synthesized data and produce a quantitative, step-by-step probability assessment "
        "of an event's occurrence as a percentage."
    ),
    backstory=(
        "You are a highly skilled quantitative analyst, trained in probabilistic forecasting and risk assessment. "
        "You do not rely on intuition. Instead, you follow a strict, transparent methodology. You break down complex "
        "problems into their component parts, identify key drivers and inhibitors, assign them weights and probabilities "
        "based on the evidence provided, and then mathematically synthesize these factors into a final, reasoned "
        "percentage chance. Your work is meticulous, evidence-based, and your 'chain of thought' is as important "
        "as the final number itself."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# 5. Report Writer Agent
report_writer = Agent(
    role="Communications Director",
    goal="To draft a comprehensive, well-structured, and human-readable report from the analyzed data and forecast.",
    backstory=(
        "You are a skilled writer who can transform complex analysis and forecasts into a clear, "
        "compelling narrative. You excel at structuring information with an executive summary, "
        "key findings, and a detailed analysis section, ensuring the final report is professional "
        "and easy for decision-makers to understand."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# 6. Final Reviewer Agent (The Editor-in-Chief)
final_reviewer = Agent(
    role="Editor-in-Chief",
    goal="To meticulously review and polish the final report for clarity, coherence, and accuracy.",
    backstory=(
        "You are the demanding Editor-in-Chief at a prestigious publication. Your reputation "
        "is built on impeccable quality. You review the final draft report, checking for logical "
        "fallacies, ensuring it directly answers the initial query, and polishing the language "
        "to be authoritative and crystal clear. Your approval is the final step before publication."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)
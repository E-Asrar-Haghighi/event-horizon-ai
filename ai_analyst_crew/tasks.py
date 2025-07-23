from crewai import Task
from agents import (
    research_strategist,
    web_search_specialist,
    data_analyst,
    probability_forecaster,
    report_writer,
    final_reviewer,
)

# --- TASK DEFINITIONS ---

# Task 1: Create a research plan (time-aware)
strategy_task = Task(
    description=(
        "Analyze the user's query: '{topic}'.\n"
        "For context, today's date is {current_date}. Focus your research questions on the period "
        "relevant to the user's query, considering this date and the next {months} months.\n"
        "Break the query down into a list of 3-7 specific, answerable questions that will form the basis of our web research. "
        "Focus on different angles like economic, political, and technological factors."
    ),
    expected_output="A bulleted list of 3-7 focused, time-relevant research questions.",
    agent=research_strategist,
)

# Task 2: Conduct web research
research_task = Task(
    description=(
        "Using the research questions provided, conduct a thorough web search to find relevant information. "
        "Gather data, expert opinions, recent news, and any relevant reports. "
        "Ensure the sources are credible."
    ),
    expected_output="A compilation of raw data and links from the web search based on the research plan.",
    agent=web_search_specialist,
    context=[strategy_task],
)

# Task 3: Analyze the gathered data
analysis_task = Task(
    description=(
        "Synthesize the information gathered from the web search. "
        "Organize the data into key findings, identifying trends, important figures, and conflicting viewpoints. "
        "Create a structured summary with clear bullet points."
    ),
    expected_output="A structured report of key findings, including data points, trends, and a summary of expert opinions.",
    agent=data_analyst,
    context=[research_task],
)

# Task 4: Forecast the probability (Upgraded with a strict format and example)
forecasting_task = Task(
    description=(
        "Analyze the synthesized data to produce a quantitative forecast for the original query: '{topic}'.\n"
        "You MUST make your probability assessment for the next {months} months only (from {current_date} to the end of the window).\n"
        "You MUST follow this **strict, step-by-step methodology** and output format. Do not deviate.\n\n"
        "**Step 1: Establish a Base Rate.**\n"
        "   - Start with a neutral base probability of 50%. State this clearly.\n\n"
        "**Step 2: Identify and Analyze Key Factors.**\n"
        "   - From the analysis, identify 3-7 'Driving Factors' (that INCREASE probability) "
        "and 'Inhibiting Factors' (that DECREASE probability).\n\n"
        "**Step 3: Assign Weights and Adjustments.**\n"
        "   - For each factor, assign a 'Weight' (Impact: 1-10) and a 'Probability Adjustment' (e.g., +15%, -10%).\n\n"
        "**Step 4: Calculate the Adjusted Probability.**\n"
        "   - Show the step-by-step calculation from the 50% base rate.\n\n"
        "**Step 5: Synthesize the Final Forecast.**\n"
        "   - State the final percentage and summarize the reasoning.\n\n"
        "### EXAMPLE OUTPUT FORMAT ###\n"
        "**Quantitative Probability Assessment**\n\n"
        "**1. Base Rate Assumption:**\n"
        "I will start with a neutral base probability of 50%.\n\n"
        "**2. Analysis of Factors:**\n"
        "**Driving Factors (Increasing Probability):**\n"
        "   - **Factor 1:** [Description of factor]. (Weight: 8/10, Adjustment: +15%)\n"
        "   - **Factor 2:** [Description of factor]. (Weight: 6/10, Adjustment: +10%)\n"
        "**Inhibiting Factors (Decreasing Probability):**\n"
        "   - **Factor 3:** [Description of factor]. (Weight: 7/10, Adjustment: -10%)\n\n"
        "**3. Calculation:**\n"
        "   - Base Rate: 50%\n"
        "   - Adjustment from Factor 1: +15%\n"
        "   - Adjustment from Factor 2: +10%\n"
        "   - Adjustment from Factor 3: -10%\n"
        "   - **Final Calculation:** 50% + 15% + 10% - 10% = **65%**\n\n"
        "**4. Final Forecast:**\n"
        "The final estimated probability of [event] is **65%**. This is primarily driven by [most important factor], though mitigated by [most important inhibiting factor]."
    ),
    expected_output=(
        "A detailed, step-by-step quantitative forecast following the exact format provided in the description, "
        "including the base rate, factor analysis with weights, the calculation, and the final forecast summary for the next {months} months."
    ),
    agent=probability_forecaster,
    context=[analysis_task],
)


# Task 5: Draft the initial report (Corrected Final Version)
reporting_task = Task(
    description="""
        Combine the key findings from the analysis and the probability forecast into a single, comprehensive draft report.
        The report must have a clear structure with these sections:
        1. Executive Summary: A high-level overview of the topic and the final probability.
        2. Key Findings: A detailed, bulleted list of the most important qualitative insights and data points from the analysis.
        3. Detailed Likelihood Assessment and Reasoning: The quantitative forecast section.
        4. Conclusion: A final summary of the situation.

        **CRUCIAL INSTRUCTION:** The 'Detailed Likelihood Assessment and Reasoning' section MUST BE a
        verbatim, word-for-word copy of the entire output from the probability forecaster.
        Do not summarize, rephrase, or change it in any way. You are only to combine it with the other sections.
    """,
    expected_output=(
        "The complete, well-structured draft report, with the forecast section copied exactly as instructed, "
        "ready for the final review."
    ),
    agent=report_writer,
    context=[analysis_task, forecasting_task],
)

# Task 6: Review and finalize the report
review_task = Task(
    description=(
        "Review the draft report. Your review must be meticulous and follow this checklist:\n"
        "1.  **Clarity & Coherence:** Is the report easy to understand and does it flow logically?\n"
        "2.  **Completeness:** Does the report directly answer the user's original query: '{topic}'?\n"
        "3.  **Methodology Check:** This is the most important step. Verify that the 'Detailed Likelihood Assessment' section "
        "contains the full, step-by-step quantitative analysis (Base Rate, Factors, Weights, Calculation). "
        "If it is missing or incomplete, you must flag it and rewrite the section to be more qualitative and "
        "state that a precise quantitative forecast could not be produced due to a deviation from methodology.\n"
        "4.  **Final Polish:** Correct any grammatical errors and polish the language to be professional and authoritative.\n\n"
        "Produce the final, publishable-quality report."
    ),
    expected_output="The final, polished, and comprehensive report, having passed all checks in the review checklist.",
    agent=final_reviewer,
    context=[reporting_task],
    output_file="final_report.md"
)
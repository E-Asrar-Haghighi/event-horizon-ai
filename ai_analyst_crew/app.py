import streamlit as st
from crewai import Crew, Process
from agents import (
    research_strategist,
    web_search_specialist,
    data_analyst,
    probability_forecaster,
    report_writer,
    final_reviewer,
)
from tasks import (
    strategy_task,
    research_task,
    analysis_task,
    forecasting_task,
    reporting_task,
    review_task,
)
from datetime import datetime

# --- STREAMLIT UI ---

st.set_page_config(page_title="Event Horizon AI: Multi-Agent Forecasting & Research System", page_icon="🌐")

st.title("Event Horizon AI: Multi-Agent Forecasting & Research System 🕵️‍♂️")
st.markdown("""
Welcome! This AI crew is designed to analyze an event, research it on the web, and provide a report on its likelihood. 
Enter a topic below to get started.  
**1- Do 5 runs of the crew and get the average of the reports to get a better report.**  
**2- Use the qualitative analysis to get a better understanding of the event.**
""")

user_query = st.text_input("Enter the event or topic you want to analyze:", 
                           placeholder="e.g., What is the possibility of a global recession in the next 6 months?")

months = st.slider("Forecast window (months):", min_value=1, max_value=12, value=3)

if st.button("Generate Report"):
    if not user_query:
        st.warning("Please enter a topic to analyze.")
    else:
        with st.spinner("The AI crew is researching and writing your report... This may take a few minutes."):
            # Get the current date and format it
            current_date = datetime.now().strftime("%Y-%m-%d")

            # Define the inputs for the crew, now including the current_date and months
            inputs = {
                'topic': user_query,
                'current_date': current_date,
                'months': months
            }

            # Assemble the crew (using static task variables)
            analyst_crew = Crew(
                agents=[
                    research_strategist,
                    web_search_specialist,
                    data_analyst,
                    probability_forecaster,
                    report_writer,
                    final_reviewer,
                ],
                tasks=[
                    strategy_task,
                    research_task,
                    analysis_task,
                    forecasting_task,
                    reporting_task,
                    review_task,
                ],
                process=Process.sequential,
                verbose=True, # Set to True for detailed agent thought processes
            )
            
            # Kick off the crew's work
            try:
                final_report_output = analyst_crew.kickoff(inputs=inputs)
                final_report = final_report_output.raw # Access the raw string output
                
                st.success("Report Generated!")
                st.markdown("---")
                st.header("Final Analyst Report")
                st.markdown(final_report)
                
                st.markdown("---")
                st.download_button(
                    label="Download Report as Markdown",
                    data=final_report,
                    file_name="analyst_report.md",
                    mime="text/markdown",
                )

            except Exception as e:
                st.error(f"An error occurred while generating the report: {e}")
# Event Horizon AI: Multi-Agent Forecasting & Research System

A sophisticated multi-agent AI-powered research and forecasting system that analyzes events, conducts web research, and provides quantitative probability assessments using a crew of specialized AI agents.

## 🌟 Features

- **Multi-Agent AI Crew**: Six specialized AI agents working together to provide comprehensive analysis
- **Web Research**: Real-time web search capabilities using SerperDev
- **Quantitative Forecasting**: Step-by-step probability assessment methodology
- **Professional Reports**: Structured, executive-level reports with clear findings
- **Web Interface**: Streamlit-based user interface for easy interaction
- **Downloadable Reports**: Export analysis results as Markdown files

## 🤖 AI Agent Crew

The system uses six specialized AI agents, each with distinct roles:

1. **Research Strategist** - Breaks down complex queries into specific research questions
2. **Web Search Specialist** - Conducts comprehensive web research using advanced search techniques
3. **Data Analyst** - Synthesizes raw data into structured analysis
4. **Probability Forecaster** - Provides quantitative probability assessments using a rigorous methodology
5. **Report Writer** - Creates comprehensive, well-structured reports
6. **Final Reviewer** - Ensures quality, accuracy, and clarity of the final report

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- SerperDev API key (for web search functionality)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Web Searcher AI Agent"
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   Create a `.env` file in the root directory with your API keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

## 🎯 Usage

### Web Interface (Recommended)

1. **Start the Streamlit app**
   ```bash
   streamlit run ai_analyst_crew/app.py
   ```

2. **Open your browser** and navigate to the provided URL (usually `http://localhost:8501`)

3. **Enter your query** in the text input field
   - Example: "What is the possibility of a global recession in the next 6 months?"

4. **Adjust the forecast window** using the slider (1-12 months)

5. **Click "Generate Report"** and wait for the AI crew to complete their analysis

6. **Download the report** as a Markdown file when complete

### Tips for Better Results

- **Multiple Runs**: The app suggests running 5 iterations and averaging the results for more accurate forecasts
- **Qualitative Analysis**: Use the detailed analysis sections to understand the reasoning behind probability assessments
- **Specific Queries**: Be as specific as possible about the event or topic you want to analyze

## 📊 Output Format

The system generates comprehensive reports in `final_report.md` (located in the project root) including:

- **Executive Summary** - High-level overview of findings
- **Key Findings** - Bullet-pointed list of important discoveries
- **Detailed Likelihood Assessment** - Step-by-step quantitative analysis
- **Conclusion** - Final recommendations and insights

### Quantitative Forecasting Methodology

The probability forecaster uses a rigorous, step-by-step approach:

1. **Base Rate**: Starts with a neutral 50% probability
2. **Factor Analysis**: Identifies driving and inhibiting factors
3. **Weight Assignment**: Assigns impact weights (1-10) and probability adjustments
4. **Calculation**: Mathematically synthesizes factors into final percentage
5. **Synthesis**: Provides final forecast with reasoning

## 🛠️ Project Structure

```
Web Searcher AI Agent/
├── ai_analyst_crew/
│   ├── __init__.py
│   ├── agents.py          # AI agent definitions
│   ├── tasks.py           # Task definitions and workflows
│   └── app.py             # Streamlit web interface
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .env                  # Environment variables (create this)
```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `SERPER_API_KEY`: Your SerperDev API key for web search (required)

### Customization

You can modify the AI agents and tasks by editing:
- `ai_analyst_crew/agents.py` - Agent roles, goals, and backstories
- `ai_analyst_crew/tasks.py` - Task descriptions and workflows

## 📝 Example Queries

The system can analyze various types of events and topics:

- **Economic forecasts**: "What is the probability of a market crash in the next 6 months?"
- **Political events**: "What are the chances of a major policy change in the next year?"
- **Technology trends**: "What is the likelihood of widespread AI adoption in the next 2 years?"
- **Social phenomena**: "What is the probability of a significant social movement emerging?"
- **Business outcomes**: "What is the likelihood of a major merger in the tech industry next quarter?"

## 🛠️ Dependencies

The project uses the following key libraries:
- `crewai` - Multi-agent AI framework
- `crewai-tools` - Tools for AI agents
- `langchain-openai` - OpenAI integration
- `streamlit` - Web interface
- `python-dotenv` - Environment variable management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for informational purposes only. The probability assessments provided are based on available data and AI analysis, but should not be considered as financial, legal, or professional advice. Always consult with qualified professionals for important decisions.

## 🆘 Support

If you encounter any issues:

1. **Check API Keys**: Ensure all API keys are properly configured in your `.env` file
2. **Internet Connection**: Verify you have a stable internet connection for web searches
3. **Dependencies**: Make sure all dependencies are installed correctly
4. **Virtual Environment**: Ensure you're running the app within the activated virtual environment
5. **Error Messages**: Check the console output for detailed error messages

For additional support, please open an issue on the project repository.

## 🔄 Recent Updates

- Streamlined agent workflow for better performance
- Enhanced web search capabilities using SerperDev
- Improved report formatting and structure
- Added download functionality for generated reports

---

**Built with ❤️ using CrewAI, OpenAI, and Streamlit** 
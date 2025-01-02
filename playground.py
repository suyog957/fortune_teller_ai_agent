# Import the necessary libraries for astrology and fortune-telling.
from phi.agent import Agent  # Used to create AI agents.
from phi.model.groq import Groq  # This is the model we use to perform tasks.
from phi.tools.duckduckgo import DuckDuckGo  # We can use this to search for astrology-related information if needed.
from dotenv import load_dotenv  # This helps us securely load sensitive information like API keys from a .env file.

# Load environment variables (like keys or tokens stored securely) from a file called .env.
load_dotenv()

# This function creates an "Astrology Agent" that can generate a Kundli, horoscope, and tell the fortune based on birth details.
def create_astrology_agent(model: str = "llama-3.3-70b-versatile"):
    """
    This function creates an AI agent designed to generate a Kundli, horoscope, and provide a fortune based on birth details.
    The agent uses a machine learning model and can search for extra information online if needed.
    """
    return Agent(
        name="Astrology Agent",  # This is the name of the agent.
        
        # The model used to perform the astrology-related tasks (e.g., birth chart generation, fortune-telling).
        model=Groq(id=model),
        
        # The tools the agent can use. Here, DuckDuckGo is used to search for extra information about astrology if needed.
        tools=[DuckDuckGo()],
        
        # Instructions for the agent to follow when generating a Kundli and fortune.
        instructions=[
            "Ask for the user's date of birth, time of birth, and place of birth",  # The agent should request basic birth details.
            "Generate a Kundli (birth chart) based on the provided birth details",  # The agent will create a birth chart.
            "Provide a horoscope based on the user's birth details",  # The agent will interpret the horoscope.
            "Tell the user's fortune at different age milestones (10, 20, 30, 40, 50, 60)",  # Provide fortune at milestones.
            "Provide suggestions and insights for the user based on the horoscope and fortune",  # Offer personal guidance.
            "Always mention that astrology is for entertainment and personal insight, and professional advice should be sought if needed"  # Always provide a disclaimer.
        ],
        
        # Show when the agent is using its tools (e.g., searching for extra information online).
        show_tool_calls=True,
        
        # Enable markdown output for readable responses.
        markdown=True
    )

# This function creates a "team" of agents that includes the astrology agent and other tools.
def create_astrology_agent_team(astrology_agent, model: str = "llama-3.3-70b-versatile"):
    """
    This function sets up a team of agents that will work together, including the astrology agent.
    """
    return Agent(
        # The team will use the same model as the individual astrology agent.
        model=Groq(id=model),
        
        # This specifies that the team includes the astrology agent we just created.
        team=[astrology_agent],
        
        # Instructions for the team to follow when working together on astrology tasks.
        instructions=[
            "Collect the user's date of birth, time of birth, and place of birth",  # Gather birth details.
            "Generate the user's Kundli (birth chart)",  # Generate the astrological birth chart.
            "Provide the user's horoscope based on their Kundli",  # Provide a horoscope.
            "Offer fortune predictions at age milestones (10, 20, 30, 40, 50, 60)",  # Fortune at milestones.
            "Provide personal insights or guidance based on the horoscope",  # Personal advice.
            "Always remind users that astrology is a form of entertainment and should not replace professional guidance"  # Reminder for users.
        ],
        
        # Show when the team is using tools.
        show_tool_calls=True,
        
        # Set to True for markdown format in responses.
        markdown=True
    )

# This function asks the astrology agent team to generate a Kundli, horoscope, and fortune based on the user's birth details.
def get_astrology_details(agent_team, dob: str, tob: str, pob: str):
    """
    This function takes the user's birth details (date, time, place) and asks the agent team to generate a Kundli,
    horoscope, and fortune based on these details.
    """
    prompt = f"Generate the  fortune for the following details:\n" \
             f"Date of Birth: {dob}\nTime of Birth: {tob}\nPlace of Birth: {pob}"
    # Asking the agent team to provide the astrology insights based on the input details.
    agent_team.print_response(prompt, stream=True)

# Main entry point of the program. This is where the code starts running.
if __name__ == "__main__":
    """
    This is the starting point of the program. It will create the astrology agents and ask them to generate the
    user's Kundli, horoscope, and fortune.
    """
    
    # Create the individual astrology agent by calling the function `create_astrology_agent`.
    astrology_agent = create_astrology_agent()

    # Create the team of agents by calling the `create_astrology_agent_team` function.
    # This includes the astrology agent we just created.
    agent_team = create_astrology_agent_team(astrology_agent)

    # Example task: Let's test the agent by providing it with a set of birth details.
    dob = "22 December 1992"  # Example Date of Birth (Day, Month, Year).
    tob = "07:51 AM"  # Example Time of Birth (Exact time, AM/PM).
    pob = "Nigdi, Pune, India"  # Example Place of Birth (City, State, Country).
    
    # Ask the agent team to generate the Kundli, horoscope, and fortune for the given birth details.
    get_astrology_details(agent_team, dob, tob, pob)

    # You can change the birth details to test different cases, e.g.:
    # dob = "30 July 1991"
    # tob = "02:17 PM"
    # pob = "Shrirampur, Maharashtra, India"
    # get_astrology_details(agent_team, dob, tob, pob)

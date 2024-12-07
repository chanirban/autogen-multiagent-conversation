import streamlit as st
import autogen
from autogen import GroupChatManager, ConversableAgent

# Define agents
def create_agents():
    config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")
    llm_config = {"config_list": config_list}

    storyteller_agent = ConversableAgent(
        name="StoryTeller",
        system_message=(
            "A wildly imaginative writer who thrives on absurdity and loves crafting "
            "stories with outrageous twists and turns that leave readers laughing out loud."
        ),
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    comedian_agent = ConversableAgent(
        name="Comedian",
        system_message=(
            "A master of comedy who infuses every situation with sharp wit, puns, and a touch "
            "of the ridiculous, aiming to elicit uncontrollable laughter."
        ),
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    editor_agent = ConversableAgent(
        name="Editor",
        system_message=(
            "A sarcastic editor who critiques with humor, often using ironic remarks, but ensures "
            "the narrative remains hilariously coherent and on point."
        ),
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    meme_agent = ConversableAgent(
        name="MemeMachine",
        system_message=(
            "A quirky person obsessed with generating side-splitting memes and viral content, "
            "always ready to add an extra layer of humor."
        ),
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    return {
        "StoryTeller": storyteller_agent,
        "Comedian": comedian_agent,
        "Editor": editor_agent,
        "MemeMachine": meme_agent,
    }

agents_dict = create_agents()

def run_chat(agent_name, topic):
    agent = agents_dict[agent_name]
    config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")
    llm_config = {"config_list": config_list}

    # Group Chat setup
    groupchat = autogen.GroupChat(
        agents=list(agents_dict.values()),
        messages=[],
        max_round=4,
        send_introductions=True
    )
    group_chat_manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # Run the chat
    chat_result = agent.initiate_chat(
        group_chat_manager,
        message=f"Let's discuss: {topic}",
        summary_method="reflection_with_llm"
    )
    return chat_result.chat_history

# Streamlit UI
st.title("Multi-Agent Chat with AutoGen")

# st.sidebar.title("View Agent")
# selected_agent = st.sidebar.selectbox(
#     "Choose an agent to view description:",
#     list(agents_dict.keys())
# )

# st.sidebar.write(f"**Description:** {agents_dict[selected_agent].description}")

# Sidebar: View all agents
st.sidebar.title("View All Agents 🤖")

# Define icons for each agent
agent_icons = {
    "StoryTeller": "📖",  # Book icon for storytelling
    "Comedian": "🎭",    # Theater masks for comedy
    "Editor": "✍️",      # Writing hand for editing
    "MemeMachine": "😂",  # Laughing emoji for memes
}

st.sidebar.write("### Agents and Descriptions:")
for agent_name, agent in agents_dict.items():
    icon = agent_icons.get(agent_name, "🤖")  # Default to robot emoji if not found
    st.sidebar.write(f"{icon} **{agent_name}:** {agent.system_message}")


# topic = st.text_input("Enter a topic to discuss:", "Alright team, brace yourselves! Today's topic is a banana duct-taped to a wall selling "
#             "for $6.2 million at an auction. Let's craft the most outrageously funny and epic story "
#             "that will have our blog readers rolling on the floor laughing!")

# Input for topic with a larger text area
topic = st.text_area(
    "Enter a topic to discuss:",
    "Alright team, brace yourselves! Today's topic is a banana duct-taped to a wall selling "
    "for $6.2 million at an auction. Let's craft the most outrageously funny and epic story "
    "that will have our blog readers rolling on the floor laughing!",
    height=100  # Increase height for a bigger input box
)




 # Function to format output
def format_chat_output(chat_history):
    formatted_output = ""
    for i, entry in enumerate(chat_history):
        role = entry.get("role", "Unknown").capitalize()
        name = entry.get("name", "Unknown")
        content = entry.get("content", "")
        
        formatted_output += f"### Step {i}:\n"
        formatted_output += f"**Role:** {role}\n"
        formatted_output += f"**Name:** {name}\n"
        formatted_output += f"**Content:**\n{content}\n\n"
        formatted_output += "---\n\n"
    
    return formatted_output

# Use the formatter in Streamlit
if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        output = run_chat("Editor", topic)
        formatted_output = format_chat_output(output)
        st.subheader("Formatted Agent Responses")
        st.markdown(formatted_output)
        st.subheader(" Agent Trace ")
        st.write(output)    
       

# if st.button("Generate Response"):
#     with st.spinner("Generating response..."):
#         output = run_chat("Editor", topic)
#         st.subheader("Agent Response")
#         st.write(output)
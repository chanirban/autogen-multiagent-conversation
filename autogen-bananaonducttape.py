import autogen
from autogen import GroupChatManager, ConversableAgent

def main():
    # Load configuration
    config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")
    llm_config = {"config_list": config_list}
    ## Us ethe below for OpenAI API
#    llm_config = {"model": "gpt-4o", "api_key": "sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

    # Define agents with distinct personas
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

    # Assign descriptions to agents
    storyteller_agent.description = "An imaginative storyteller who turns any topic into an epic narrative."
    comedian_agent.description = "A jokester who loves adding humor to any situation."
    editor_agent.description = "A no-nonsense editor who values precision and coherence in writing."
    meme_agent.description = "A playful AI obsessed with creating viral content."

    # Set up the group chat
    agents = [storyteller_agent, comedian_agent, editor_agent, meme_agent]
    groupchat = autogen.GroupChat(
        agents=agents,
        messages=[],
        max_round=6,
        send_introductions=True
    )
    group_chat_manager = GroupChatManager(groupchat=groupchat, llm_config=llm_config)

    # Start the conversation
    chat_result = editor_agent.initiate_chat(
        group_chat_manager,
        message=(
            "Alright team, brace yourselves! Today's topic is a banana duct-taped to a wall selling "
            "for $6.2 million at an auction. Let's craft the most outrageously funny and epic story "
            "that will have our blog readers rolling on the floor laughing!"
        ),
        summary_method="reflection_with_llm"
    )

    # Print the summary of the chat
    print(chat_result.summary)
#    print(chat_result.chat_history)

if __name__ == "__main__":
    main()

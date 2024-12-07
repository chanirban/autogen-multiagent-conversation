import autogen
from autogen import GroupChatManager
from autogen import ConversableAgent

def main():
    # Load configuration
    config_list = autogen.config_list_from_json(env_or_file="OAI_CONFIG_LIST.json")
    llm_config = {"config_list": config_list}

    # Define agents with distinct personas
    chef_agent = ConversableAgent(
        name="Chef_Luigi",
        system_message="passionate Italian chef",
        llm_config=llm_config,
        human_input_mode="NEVER")
    

    foodie_agent = ConversableAgent(
        name="Foodie_Fran",
        system_message="enthusiastic food lover who enjoys unconventional combinations",
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    health_guru_agent = ConversableAgent(
        name="Health_Guru",
        system_message="health-conscious expert who emphasizes nutrition in all debates",
        llm_config=llm_config,
        human_input_mode="NEVER")

    meme_agent = ConversableAgent(
        name="Meme_Machine",
        system_message="humorous and playful AI specializing in food-related memes",
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    moderator = ConversableAgent(
        name="Moderator",
        system_message="neutral and impartial moderator",
        llm_config=llm_config,
        human_input_mode="NEVER"
    )

    # The `description` attribute is a string that describes the agent.
    # It can also be set in `ConversableAgent` constructor.
    moderator.description = "A neutral and impartial moderator who ensures fairness in discussions."
    meme_agent.description = "A playful and humorous agent specializing in memes and jokes about food."
    health_guru_agent.description = "A health expert who emphasizes nutrition and healthy eating habits."
    foodie_agent.description = "An adventurous food lover who enjoys unconventional combinations."
    chef_agent.description = "A passionate Italian chef who brings a traditional perspective."

    # Set up the multi-agent debate
    agents = [chef_agent, foodie_agent, health_guru_agent, meme_agent, moderator ]


    groupchat = autogen.GroupChat(agents=agents, messages=[], max_round=6, send_introductions=True)
    group_chat_manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
    # UserProxyAgent acts as the audience

    # User can interject or vote on the winner
    
    chat_result = moderator.initiate_chat(
    group_chat_manager,
    message="Welcome to the Great Pizza Debate! Today's topic: 'Is pineapple on pizza acceptable?' Let's hear your thoughts! Who do you think won the debate?",
    summary_method="reflection_with_llm",
    )

    print(chat_result.summary)
    
if __name__ == "__main__":
    main()
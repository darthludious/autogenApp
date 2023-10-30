import os
import autogen
import memgpt.autogen.memgpt_agent as memgpt_autogen
import memgpt.autogen.interface as autogen_interface 
import memgpt.agent as agent
import memgpt.system as system
import memgpt.utils as utils
import memgpt.presets as presets
import memgpt.constants as constants
import memgpt.personas.personas as personas
import memgpt.humans.humans as humans
from memgpt.persistence_manager import InMemoryStateManager, InMemoryStateManagerWithPreloadedArchivalMemory, InMemoryStateManagerWithFaiss

# Configure connection to local language model
config_list = [{
    "api_type" : "open_ai",
    "api_base" : "http://localhost:1234/v1",
    "api_key" : "NULL"
}]
llm_config = {"config_list": config_list, "seed": 42}

# Set up interface and persistence manager
interface = autogen_interface.AutoGenInterface()
persistence_manager = InMemoryStateManager()

# Jarvis: The main executive assistant
jarvis_persona = "I'm Jarvis, your executive assistant."
jarvis_human = "I'm the user interacting with Jarvis."
jarvis_agent = presets.use_preset(presets.DEFAULT, 'gpt-4', jarvis_persona, jarvis_human, interface, persistence_manager)
jarvis = memgpt_autogen.MemGPTAgent(
    name="Jarvis",
    agent=jarvis_agent,
)

# Coder: A specialized agent for coding tasks
coder_persona = "I'm a coder assistant."
coder_human = "I'm the user interacting with the coder assistant."
coder_agent = presets.use_preset(presets.DEFAULT, 'gpt-4', coder_persona, coder_human, interface, persistence_manager)
coder = memgpt_autogen.MemGPTAgent(
    name="Coder",
    agent=coder_agent,
)

# Configure group chat and manager
groupchat = autogen.GroupChat(agents=[jarvis, coder], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Now you can interact with Jarvis and utilize the coder agent via the manager

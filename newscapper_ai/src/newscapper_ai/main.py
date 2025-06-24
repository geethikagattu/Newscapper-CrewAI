#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from crew import NewscapperAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'date': datetime.now().strftime('%Y-%m-%d'),  # this fixes the missing {date}
        'current_year': str(datetime.now().year)
    }
    
    # inputs_array = [
    #     {
    #         'topic': 'ai agents',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #      }, 
    #     {
    #         'topic': 'openai',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #     },
    #      {
    #         'topic': 'hugging face',
    #         'date': datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #      }
    # ]
    
    try:
        NewscapperAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

run()


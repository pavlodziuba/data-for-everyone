import sys
import os
import openai
import re
import warnings
import io


warnings.filterwarnings("ignore")

from dotenv import load_dotenv, dotenv_values

load_dotenv()

# Set your OpenAI API key here
openai.api_key = os.getenv('OpenAI_KEY')
error_count = 0


def create_and_run_python_file(code, user_prompt):
    global error_count
    buffer = io.StringIO()
    original_stdout = sys.stdout
    try:
        sys.stdout = buffer
        #print('EXEC CODE')
        exec(code)
    except Exception as e:
        error_count += 1
        print(f"Error occurred: {e}")
        if error_count >= 15:
            print("There is a critical error")
        else:
            run_all(user_prompt)
    finally:
        # Restore the original stdout
        sys.stdout = original_stdout
    output = buffer.getvalue()
    # Split the output into lines and return the last line
    print("THIS OUTPUT MESSAGE \n" + output)
    return output


def extract_python_code(text):
    # Regular expression to match Python code blocks within triple backticks
    match = re.search(r"```(?:python)?(.*?)```", text, re.DOTALL | re.IGNORECASE)

    if match:
        # Extract and return the code inside the backticks
        return match.group(1).strip()
    return ""  # Return an empty string if no match is found

def get_chatgpt_response(prompt):
    """
    Sends a prompt to the OpenAI API and retrieves the response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can adjust the model as needed
        messages=[
            {"role": "user",
             "content": "I need answer in first message."},
            {"role": "user",
             "content": "Remember current year 2024!"},
            {"role": "user",
             "content": "I need only code without any explanation or other text (generated text should be ready to be copied and already work)"},
            {"role": "user", "content":"How should i provide source in python code if its World Bank Open Data (use their API)(i need code in 1 code section (python) without explanation i have all packages intalled)"},
            {"role": "user",
             "content": "NEVER USE and VERY IMPORTANT IN PYTHON CODE!!!! ARGUMENTS us 'covert_date' and for 'data_date' USE just 'date' "},
            {"role": "user",
             "content": "After last print of code make new print where you make detailed analyse about what was printed before on this topic!"},
            {"role": "user",
             "content": "Never use plot library for answer"},
            {"role": "user",
             "content": "Final code should give always text result"},
            {"role": "user",
             "content": "Make sure to always print some result in end"},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]
def run_all(user_prompt):
    #user_prompt = sys.argv[1]
    print("\nSending follow-up prompt to ChatGPT...")
    analysis = get_chatgpt_response(user_prompt)

    print("\nChatGPT Analysis:\n")
    print(analysis)

    my_wb_code = extract_python_code(analysis)
    print("\nReady WB code:\n")
    print(my_wb_code)

    print("\n\n\n\n\n\n\n\n\n\nNow try run code:\n")
    if len(my_wb_code) < 10:
        my_wb_code = analysis
    final_message = create_and_run_python_file(my_wb_code, user_prompt)
    return final_message


def main():
    if len(sys.argv) < 2:
        print("Usage: python logic.py \"[Your prompt here]\"")
        sys.exit(1)
    run_all()



if __name__ == "__main__":
    main()

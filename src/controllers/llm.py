from openai import OpenAI

client = OpenAI(
    api_key="GET YOUR OWN KEY"
)


def generate(role, value, workflow_prompt, prompt):
    # Build the prompt
    completion_prompt = f"""
${role}
${value}
${workflow_prompt}
User Input: ${prompt}
"""
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": completion_prompt
            }
        ],
        model="chatgpt-4o-latest"
    )
    return completion.choices[0].message.content


def generate_with_input(role, value, workflow_prompt, prompt, input):
    # Generate the prompt
    input_prompt = ""
    for key in input.keys():
        input_prompt = f"""
${key}
${input[key]}
"""

    completion_prompt = f"""
${role}
${value}
${workflow_prompt}
${input}
"""

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": completion_prompt
            }
        ],
        model="chatgpt-4o-latest"
    )
    return completion.choices[0].message.content

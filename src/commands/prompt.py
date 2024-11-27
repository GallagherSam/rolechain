import yaml

from controllers.llm import generate, generate_with_input


def execute_prompt(workflow_id, prompt):
    workflow_id = int(workflow_id)  # TODO: Santize inputs

    # Load the config
    config = fetch_config()

    # Fetch the workflow
    workflow = fetch_workflow(workflow_id, config['workflows'])

    # Loop through the steps
    data = {}
    for step in workflow['steps']:

        # Loop through the personas
        for persona_id in step['personas']:
            # Fetch the persona
            persona = fetch_persona(persona_id, config['personas'])

            # Check for required input
            if 'inputFrom' in step:
                # Get the input content
                input = data[step['inputFrom']]

                # Generate the content
                content = generate_with_input(
                    persona['role'], persona['value'], step['prompt'], prompt, input
                )

            else:
                # Generate the content
                content = generate(
                    persona['role'], persona['value'], step['prompt'], prompt
                )

            if step['name'] not in data:
                data[step['name']] = {}

            data[step['name']][persona['name']] = content
            print(persona['name'])
            print(content)
            print("\n\n------\n\n")


def fetch_workflow(id, workflows):
    return next((w for w in workflows if w.get('id') == id), None)


def fetch_persona(id, personas):
    return next((p for p in personas if p.get('id') == id), None)


def fetch_config():
    with open('configs/config.yaml', 'r') as f:
        data = yaml.safe_load(f)
    return data

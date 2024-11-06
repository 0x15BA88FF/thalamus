import os
import json


APPLICATION_PATHS =  os.environ['LAI_APP_PATH'] = os.pathsep.join(["~/thalamus.ai/"])


for path in APPLICATION_PATHS.split(os.pathsep):
    instruction_files = []
    path = os.path.expanduser(path)
    applications = [
        os.path.join(path, application_path)
        for application_path in os.listdir(path)
        if os.path.isdir(os.path.join(path, application_path))
    ]

    for application in applications:
        path = os.path.join(application, "instructions")
        if not os.path.isdir(path): pass
        instruction_files.extend([
            os.path.join(path, instruction)
            for instruction in os.listdir(path)
            if instruction.endswith('.json')
            if not os.path.isdir(os.path.join(path, instruction))
        ])

    for file in instruction_files:
        try:
            with open(file, 'r') as file:
                data = json.load(file)
                print(json.dumps(data, indent=4))
                
        except json.JSONDecodeError:
            print(f"Error: The file { file } contains invalid JSON.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
import os
import yaml

def generate_readme_for_ansible_role(role_path):
    # Check if role_path exists
    if not os.path.exists(role_path):
        print(f"Error: The directory {role_path} does not exist.")
        return

    readme_content = "# README for Ansible Role\n\n"

    # Read meta information
    meta_file = os.path.join(role_path, 'meta', 'main.yml')
    if os.path.exists(meta_file):
        with open(meta_file, 'r') as file:
            meta_content = yaml.safe_load(file)
            author = meta_content.get('galaxy_info', {}).get('author', 'Unknown Author')
            description = meta_content.get('galaxy_info', {}).get('description', 'No description available')

        readme_content += f"## Author\n\n{author}\n\n"
        readme_content += f"## Description\n\n{description}\n\n"

    # Add test.yml content under Example section if it exists
    test_file = os.path.join(role_path, 'test.yml')
    if os.path.exists(test_file):
        readme_content += "## Example\n\n"
        readme_content += "```yaml\n"  # Start of code block for YAML content
        with open(test_file, 'r') as file:
            readme_content += file.read()
        readme_content += "\n```\n"  # End of code block

    # Directory structure overview
    readme_content += "## Role Directory Structure Overview\n"

    # Walk through the role directory
    for root, dirs, files in os.walk(role_path):
        # Skip meta as it's already processed
        if 'meta' in root:
            continue

        relative_path = os.path.relpath(root, role_path)
        if relative_path != ".":
            readme_content += f"\n### {relative_path.capitalize()}\n\n"

        for file in sorted(files):
            if file.endswith(".yml"):
                readme_content += f"- `{file}`\n"
                file_path = os.path.join(root, file)

                # Summarize the file contents (optional)
                with open(file_path, 'r') as stream:
                    try:
                        yaml_content = yaml.safe_load(stream)
                        if yaml_content and isinstance(yaml_content, list):
                            readme_content += f"  - Tasks: {len(yaml_content)}\n"
                        elif yaml_content and isinstance(yaml_content, dict):
                            for key in yaml_content.keys():
                                readme_content += f"  - {key}\n"
                    except yaml.YAMLError:
                        readme_content += "  - Error reading YAML content\n"

    # Write the README content to a file
    readme_path = os.path.join(role_path, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(readme_content)

    print(f"README.md generated in {role_path}")

# Example usage
generate_readme_for_ansible_role('/path/to/role')

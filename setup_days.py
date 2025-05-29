import os

for day in range(1, 101):
    folder_name = f"Day{day:03d}"  # Day001, Day002, ..., Day100
    os.makedirs(folder_name, exist_ok=True)

    main_path = os.path.join(folder_name, "main.py")
    readme_path = os.path.join(folder_name, "README.md")

    # Create main.py if it doesn't exist
    if not os.path.exists(main_path):
        with open(main_path, "w") as f:
            f.write("# Start coding here!\n")

    # Create README.md if it doesn't exist
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {folder_name} – [Project Name]\n\n"
                    "## What I Built\n_A short description of today’s project._\n\n"
                    "## What I Learned\n- Point 1\n- Point 2\n\n"
                    "## Hardest Part\n_What was most challenging today?_\n\n"
                    "## Extra Challenges or Features\n_Optional: Did you add anything extra or plan something for later?_\n\n"
                    "## Reflection\n_How did you feel about today’s session? What do you want to improve or revisit?_\n")

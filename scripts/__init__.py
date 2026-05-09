
# File 7: __init__.py files për të bërë direktoritë paketa Python

init_files = {
    "/mnt/agents/output/duffing_poincare_project/src/__init__.py": "",
    "/mnt/agents/output/duffing_poincare_project/src/models/__init__.py": "",
    "/mnt/agents/output/duffing_poincare_project/src/visualization/__init__.py": "",
    "/mnt/agents/output/duffing_poincare_project/src/analysis/__init__.py": ""
}

for path, content in init_files.items():
    with open(path, "w") as f:
        f.write(content)

print("✓ __init__.py files u krijuan me sukses!")
print("\nTë gjitha files e projektit janë gati!")

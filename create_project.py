import sys, os

def c_project(name: str) -> None:
    os.mkdir(f"c/{name}")
    os.mkdir(f"c/{name}/src")
    os.mkdir(f"c/{name}/out")
    main_file = open(f"c/{name}/src/main.c", "w+")
    script = open(f"c/{name}/run", "w+")
    main_file.write('#include <stdio.h>\nint main() {\n\tprintf("Hello World!\\n");\n\treturn 0;\n}')
    script.write(f"""
    gcc src/main.c -o out/{name}
    ./out/{name}
    """)
    main_file.close()
    script.close()
    os.system(f"chmod +x c/{name}/run")
    os.system(f"code c/{name}")

def py_project(name: str) -> None:
    os.mkdir(f"python/{name}")
    main_file = open(f"python/{name}/main.py", "w+")
    main_file.write("print('Hello World!')")
    main_file.close()
    os.system(f"code python/{name}")

def web_project(name: str) -> None:
    os.mkdir(f"web/{name}")
    os.mkdir(f"web/{name}/css")
    os.mkdir(f"web/{name}/js")
    os.mkdir(f"web/{name}/img")
    index = open(f"web/{name}/index.html", "w+")
    index.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name}</title>
</head>
<body>
    
</body>
</html>
""")
    index.close()
    os.system(f"code web/{name}")

def show_help() -> None:
    print("Usage: [c, py, web] name")

def already_exists() -> None:
    print("Project name already exists")

def main():
    if len(sys.argv) != 3:
        return show_help()

    proj = sys.argv[1]
    name = sys.argv[2]
    if proj not in ["c", "py", "web"]:
        return show_help()
    
    names_file = open(f"list_{proj}.txt", "r+")
    projects = names_file.readlines()
    
    if name+"\n" in projects:
        names_file.close()
        return already_exists()

    names_file.write(name+"\n")

    methods = {
        "c": c_project,
        "py": py_project,
        "web": web_project
    }

    return methods[proj](name)
    

if __name__ == "__main__":
    main()

import subprocess
import os

def compile_and_run_java_code(java_code: str):
    # Write Java code to a file
    java_file = "GeneratedCode.java"
    
    with open(java_file, 'w') as f:
        f.write("public class GeneratedCode {\n")
        f.write("public static void main(String[] args) {\n")
        f.write(java_code)
        f.write("\n}\n}")
    
    # Compile the Java file using javac
    try:
        subprocess.run(["javac", java_file], check=True)
        
        # Run the compiled Java code
        subprocess.run(["java", "GeneratedCode"], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation or execution: {e}")
    finally:
        # Clean up the generated files
        os.remove(java_file)
        os.remove("GeneratedCode.class")

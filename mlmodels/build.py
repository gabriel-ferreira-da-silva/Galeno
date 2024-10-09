import os
import subprocess

def run_script_in_directory(directory):
    # Change to the specified directory
    try:
        os.chdir(directory)
        print(f"Running script in directory: {directory}")
        
        # Execute the Python script
        result = subprocess.run(['/usr/bin/python3', 'setmodels.gal.py'], check=True)
        
        if result.returncode == 0:
            print(f"Successfully ran setmodels.gal.py in {directory}")
        else:
            print(f"Error occurred while running setmodels.gal.py in {directory}")

    except Exception as e:
        print(f"An error occurred while changing to {directory}: {e}")

def main():
    # Run the script in the heart-failure directory
    run_script_in_directory("heart-failure")
    
    # Run the script in the breast-cancer directory
    run_script_in_directory("breast-cancer")

if __name__ == "__main__":
    main()

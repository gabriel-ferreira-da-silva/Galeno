import os
import subprocess

def run_script_in_directory(directory):
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return
    
    try:
        os.chdir(directory)
        print(f"Running script in directory: {directory}")
        
        result = subprocess.run(
            ['/usr/bin/python3', 'setmodels.gal.py'],
            check=True,
            capture_output=True,
            text=True
        )
        
        print(result.stdout)  # Print standard output from the script

        if result.returncode == 0:
            print(f"Successfully ran setmodels.gal.py in {directory}")
        else:
            print(f"Script setmodels.gal.py returned non-zero exit status in {directory}")

    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running setmodels.gal.py in {directory}: {e.stderr}")
    except Exception as e:
        print(f"An error occurred while changing to {directory}: {e}")
    finally:
        os.chdir("..")  # Change back to the parent directory

def main():
    for dir_name in ["heart-failure", "lung-cancer", "breast-cancer"]:
        run_script_in_directory(dir_name)

if __name__ == "__main__":
    main()

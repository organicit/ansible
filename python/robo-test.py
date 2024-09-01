#!/usr/bin/env python3

import subprocess
import glob
import os

def run_robot_tests():
    # Define the absolute path to the robot executable
    robot_executable = '/home/ewilson/.local/bin/robot'
    
    # Define the pattern to match .robot files
    robot_pattern = '*rpi_resources.robot'
    
    # Use glob to find all .robot files that match the pattern
    robot_files = glob.glob(robot_pattern)
    
    if not robot_files:
        print("No Robot Framework files found.")
        return
    
    # Print the list of robot files found (for debugging purposes)
    print("Robot files found:", robot_files)
    
    # Run the Robot Framework test suite
    try:
        result = subprocess.run([robot_executable] + robot_files, capture_output=True, text=True)
        
        # Check if the execution was successful
        if result.returncode == 0:
            print("Tests executed successfully.")
        else:
            print("Tests failed.")
        
        # Print the output of the Robot Framework execution
        print("Output:\n", result.stdout)
        print("Errors:\n", result.stderr)
    
    except FileNotFoundError as fnf_error:
        print(f"File not found error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Permission error: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_robot_tests()

# import subprocess
# import glob
# import os

# def run_robot_tests():
#     # Define the pattern to match .robot files
#     robot_pattern = '*rpi_resources.robot'
    
#     # Use glob to find all .robot files that match the pattern
#     robot_files = glob.glob(robot_pattern)
    
#     if not robot_files:
#         print("No Robot Framework files found.")
#         return
    
#     # Print the list of robot files found (for debugging purposes)
#     print("Robot files found:", robot_files)
    
#     # Run the Robot Framework test suite
#     try:
#         result = subprocess.run(['/home/ewilson/.local/bin'] + robot_files, capture_output=True, text=True)
        
#         # Check if the execution was successful
#         if result.returncode == 0:
#             print("Tests executed successfully.")
#         else:
#             print("Tests failed.")
        
#         # Print the output of the Robot Framework execution
#         print("Output:\n", result.stdout)
#         print("Errors:\n", result.stderr)
    
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     run_robot_tests()

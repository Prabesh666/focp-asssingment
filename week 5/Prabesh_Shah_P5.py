#1
import sys

def main():
    print(f"OS platform that's being used is: {sys.platform}")

if __name__ == "__main__":
    main()
# OS platform that's being used is: win32

#2
import sys

def main():
    arguments_num = len(sys.argv) - 1
    # subtract 1 because the program name itself is an argument
    print(f"Number of arguments passed: {arguments_num}")

if __name__ == "__main__":
    main()
    
#  C:\Users\ace\Desktop\SEM 3\FOCP\Assignments>python Prashiddha_Joshi_P5.py 12 33 4
# Number of arguments passed: 3

#3
import sys
# Sort the command-line arguments by length
# the key=len argument is telling sorted() to sort the elements based on their length.
arguements_sorted = sorted(sys.argv[1:], key=len)
print("Shortest argument:", arguements_sorted[0])
# python Prashiddha_Joshi_P5.py 12 33 41 22
# Shortest argument: 12

#5
import sys

if len(sys.argv) > 1:
    Temp = [float(temp) for temp in sys.argv[1:]]
    if Temp:
        max_temp = max(Temp)
        min_temp = min(Temp)
        mean_temp = sum(Temp) / len(Temp)

        print(f"Max temperature: {max_temp}")
        print(f"Min temperature: {min_temp}")
        print(f"Mean temperature: {mean_temp}")
    else:
        print("Provide temperature values.")


#6
import sys
import shutil
import os

# Assume a file name is always provided as a command-line argument
org_file = sys.argv[1]

# If the file exists
if os.path.exists(org_file):
    # Create a backup file with a different name
    copied_file = org_file + '.copied'
    shutil.copy2(org_file, copied_file)

    print(f"Original: {org_file}, Backup : {copied_file}")
else:
    print("Original file not found.")

# python a.py aaple.txt
# Original: aaple.txt, Backup : aaple.txt.new_file

# python a.py aa.txt
# Original file not found.
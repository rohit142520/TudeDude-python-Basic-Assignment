# Write and append data to a file(created by Rohit Gautam)
user_initial_input = input("Enter the initial content to write to the file: ")

with open("file_1","w") as fh:
    fh.write(user_initial_input + "\n")
    print(f"\nSuccessfully wrote initial input into {"file_1"}.")

user_append_input = input("Enter additional content to append to the file.")
with open("file_1","at") as fh_1:
    fh_1.write(user_append_input + "\n")
    print(f"Successfully appended additional data to the file {"file_1"}.")
with open("file_1","rt") as fh_2:
    for line in fh_2:
        print(line.strip())

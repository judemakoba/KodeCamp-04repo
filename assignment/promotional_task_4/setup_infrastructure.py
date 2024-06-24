import os

# Define the organizational structure
users = {
    'Andrew': 'System Administrator',
    'Julius': 'Legal',
    'Chizi': 'Human Resource Manager',
    'Jeniffer': 'Sales Manager',
    'Adeola': 'Business Strategist',
    'Bach': 'CEO',
    'Gozie': 'IT intern',
    'Ogochukwu': 'Finance Manager'
}

directories = [
    'Finance Budgets',
    'Contract Documents',
    'Business Projections',
    'Business Models',
    'Employee Data',
    'Company Vision and Mission Statement',
    'Server Configuration Script'
]

# Create users and assign them to groups (Simulated)
def create_users(users):
    for user, role in users.items():
        print(f"Creating user: {user} with role: {role}")
        # Code to create user and assign to group goes here

# Create directories
def create_directories(directories):
    base_path = os.getcwd()
    for directory in directories:
        dir_path = os.path.join(base_path, directory)
        os.makedirs(dir_path, exist_ok=True)
        print(f"Created directory: {dir_path}")

# Feature to take user input and create a file in the specified directory
def create_file_in_directory(directories):
    file_name = input("Enter the name of the file: ")
    directory = input("Enter the directory to create the file in: ")

    if directory in directories:
        file_path = os.path.join(os.getcwd(), directory, file_name)
        with open(file_path, 'w') as file:
            file.write("")  # Creates an empty file
        print(f"File created at: {file_path}")
    else:
        print("Error: Directory name is not one of the company directories.")

# Main execution
if __name__ == "__main__":
    create_users(users)
    create_directories(directories)
    create_file_in_directory(directories)

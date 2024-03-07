import paramiko

# Set the hostname, username, and password
hostname = "151.80.64.159"
username = "ubuntu"
password = "JQ7uvHWuDd"

# Create an SSH client object
ssh = paramiko.SSHClient()

# Set the missing host key policy
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the remote server
ssh.connect(hostname, username=username, password=password)

# Prompt the user to input commands
while True:
    command = input("Enter a command (or 'exit' to quit): ")
    if command.lower() == "exit":
        break

    # Execute the command immediately
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.read().decode()
    error = stderr.read().decode()

    # Print the output and error (if any) of the command
    print(f"Command: {command}")
    print(f"Output:\n{output}")
    print(f"Error:\n{error}")

# Close the SSH connection
ssh.close()

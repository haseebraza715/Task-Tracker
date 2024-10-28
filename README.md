

# Task Tracker CLI

Task Tracker CLI is a simple command-line tool to help you manage your tasks effectively. Using this tool, you can add, update, delete, and mark tasks with different statuses such as "todo", "in-progress", and "done". All tasks are stored in a `tasks.json` file in the current directory, making it easy to keep track of your tasks persistently.

## Features

- **Add** new tasks
- **Update** task descriptions
- **Delete** tasks
- **Mark** tasks as in-progress or done
- **List** tasks by status (all, done, todo, in-progress)

## Getting Started

### Prerequisites

- Python 3.6 or higher is required to run this CLI application.

### Installation

1. **Clone** the repository or **download** the `task_cli.py` file to your local machine.

    ```bash
    git clone https://github.com/yourusername/task-tracker-cli.git
    cd task-tracker-cli
    ```

2. Make sure the `task_cli.py` file is executable.

    ```bash
    chmod +x task_cli.py
    ```

### Usage

You can run the CLI commands from the terminal using the format below:

```bash
python task_cli.py <command> [arguments]
```

## Commands

### 1. Adding a New Task

Add a new task to the task list. Each task requires a short description.

```bash
python task_cli.py add "Your task description"
```

**Example**:

```bash
python task_cli.py add "Buy groceries"
```

**Output**:
```
Task added successfully (ID: 1)
```

### 2. Updating a Task

Update an existing task’s description. You need to specify the task ID and the new description.

```bash
python task_cli.py update <task_id> "Updated task description"
```

**Example**:

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

**Output**:
```
Task updated successfully
```

### 3. Deleting a Task

Delete a task by its ID.

```bash
python task_cli.py delete <task_id>
```

**Example**:

```bash
python task_cli.py delete 1
```

**Output**:
```
Task deleted successfully
```

### 4. Marking a Task as In-Progress or Done

Change the status of a task by marking it as "in-progress" or "done".

```bash
python task_cli.py mark-in-progress <task_id>
python task_cli.py mark-done <task_id>
```

**Example**:

```bash
python task_cli.py mark-in-progress 1
python task_cli.py mark-done 1
```

**Output**:
```
Task marked as in-progress
Task marked as done
```

### 5. Listing Tasks

List tasks based on their status. The available options are:
- `list`: Shows all tasks
- `list done`: Shows only completed tasks
- `list todo`: Shows tasks that are not started
- `list in-progress`: Shows tasks that are currently in progress

**Examples**:

```bash
python task_cli.py list          # Lists all tasks
python task_cli.py list done     # Lists only completed tasks
python task_cli.py list todo     # Lists only tasks not started
python task_cli.py list in-progress  # Lists only tasks in progress
```

**Output**:
```
[1] Buy groceries - done (Created at: 2023-10-27T12:34:56)
[2] Clean the house - in-progress (Created at: 2023-10-27T13:20:45)
```

## Task Properties

Each task in the `tasks.json` file has the following properties:

- **id**: Unique identifier for the task
- **description**: Short description of the task
- **status**: Status of the task (`todo`, `in-progress`, `done`)
- **createdAt**: Date and time the task was created
- **updatedAt**: Date and time the task was last updated

## Error Handling

The CLI application handles common errors such as:

- Missing or invalid task IDs for update, delete, or status change commands.
- Empty or non-existent `tasks.json` file.
- Invalid JSON format in the `tasks.json` file.

## Example Workflow

Here’s an example of using the Task Tracker CLI to manage tasks:

1. **Add a new task**:
    ```bash
    python task_cli.py add "Finish the report"
    ```

2. **Mark the task as in-progress**:
    ```bash
    python task_cli.py mark-in-progress 1
    ```

3. **Update the task description**:
    ```bash
    python task_cli.py update 1 "Finish the annual report"
    ```

4. **Mark the task as done**:
    ```bash
    python task_cli.py mark-done 1
    ```

5. **List all tasks**:
    ```bash
    python task_cli.py list
    ```

## Notes

- Ensure the `task_cli.py` script and `tasks.json` file are in the same directory.
- Task IDs are automatically assigned and managed by the application.
- When listing tasks, tasks are displayed with their ID, description, status, and timestamps.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy managing your tasks with the Task Tracker CLI!

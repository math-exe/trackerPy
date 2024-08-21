# TrackerPy

**TrackerPy** is a powerful logging tool for Python scripts, designed to facilitate the monitoring and tracking of running processes.

### Dependencies
```bash
pip install -r requirements.txt
```

### Instalation
To install TrackerPy, follow the steps below:

1. Navigate to the main directory where you downloaded the files from this repository. Your path should look something like this:
```bash
C:\Users\your_user\trackerpy
```

2. With the terminal open in this directory, run the following command to install TrackerPy:
```bash
pip install trackerpy
```

After the installation, you will be ready to integrate TrackerPy into your Python scripts, taking advantage of its features to improve control and traceability of your operations.

### How to Use
**Step 1:** Database Connection.

First, you need to configure the config.py file. Replace the variable values based on your credentials and database information.
``` bash
C:\Users\your_user\trackerpy\config.py
```

**Stpe 2:** Instance Configuration.

After configuring config.py, you need to initialize an instance of the TrackerPy class in your script. The initialization requires you to provide some parameters, such as the script ID, script name, log source, and process step.

```python
from trackerpy import TrackerPy

# Initialize TrackerPy
tracker = TrackerPy(script_id=1, script_name="Script Name", source_name="Data Source", process_step="PROCESSING")
```

**Step 3:** Logging.

With the `TrackerPy` instance initialized, you can log different types of messages throughout your script. `TrackerPy` provides three main methods for logging:

    1. log_info(): To log general information.
    2. log_success(): To log the successful completion of a process.
    3. log_error(): To log errors that occurred during script execution.

Here is an example of how to use each of these methods:

```python
# Log an information message
tracker.log_info(message="The process has started.")

# Log a success message
tracker.log_success(message="The process was completed successfully.")

# Log an error message
try:
    # Code that may generate an error
    result = 10 / 0
except Exception as e:
    tracker.log_error(message="An error occurred during the execution of the process.", output=str(e))
```
# BUMP - Basic Uptime Monitoring Program

A simple, locally executed tool for monitoring the availability and performance of web resources.

## ⚠️ Disclaimer

This is a learning project. Do not rely on this tool for critical monitoring purposes.
Use externally-hosted solutions for actual real-world monitoring of web resources.

## Features

- **URL Monitoring**
- **Real-Time Alert**
- **User-Friendly GUI**
- **Logging / History**

## Technologies Used

- **Backend:** Python
- **Frontend:** HTML, CSS, JavaScript (integrated via [pywebview](https://pywebview.flowrl.com/) )
- **Data Storage:** JSON for configuration and logging

## Installation and Setup

You can set up BUMP using one of the following methods:

### Option 1: Download the PyInstaller Executable

1. **Download the Latest Release:**
   - Get the latest release as a portable executable bundled using PyInstaller from the [Releases](https://github.com/JeanMariePrevost/basic-uptime-monitoring-program/releases) page.

2. **Run the Application:**
   - Execute the downloaded `.exe` file.
   - **Note:** Configuration files will be created in the same folder as the executable. It is recommended to run it from a dedicated folder.

### Option 2: Run the Python Scripts

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/JeanMariePrevost/basic-uptime-monitoring-program.git
   cd bump
   ```

2. **Install Dependencies:**
	**Note:** We recommend using a virtual environment.

     ```bash
     pip install -r requirements.txt
     ```

3. **Run the Application:**

   ```bash
   python main.py
   ```

## Usage

### Accessing the GUI

- The GUI automatically opens on launch.
- You can also access it by clicking the system tray icon.

### Adding New Resource Monitors

- Use the interface to add and configure resources (URLs) you want to monitor.
- Configure check intervals and notification preferences.

### Receiving Alerts

- Receive toast notifications when a monitored resource becomes unavailable.
- Receive email and SMS alerts by configuring them in the settings.
- View logs of all checks and events within the application.

## License

This project is licensed under the [MIT License](LICENSE).
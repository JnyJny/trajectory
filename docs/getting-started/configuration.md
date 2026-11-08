# Configuration

Trajectory simulator. uses Pydantic Settings for configuration management, which allows you to configure the application using environment variables, configuration files, or both.

## Environment Variables

You can configure trajectory using environment variables:

```bash
export TRAJECTORY_SETTING_NAME=value
trajectory [command]
```

## Configuration File

You can also use a configuration file. Create a `.env` file in your project directory:

```bash
# .env
TRAJECTORY_SETTING_NAME=value
```

## Available Settings

The following settings are available:

### Logging Settings

- `TRAJECTORY_LOG_LEVEL`: Set the logging level (default: INFO)
- `TRAJECTORY_LOG_FILE`: Path to log file (default: trajectory.log)
### Application Settings

Add your application-specific settings here.

## Priority Order

Settings are loaded in the following priority order (highest to lowest):

1. Environment variables
2. Configuration file (`.env`)
3. Default values

## Example

```bash
# Set log level to DEBUG
export TRAJECTORY_LOG_LEVEL=DEBUG

# Run the CLI
trajectory [command]
```


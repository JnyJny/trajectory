# Examples

This page provides practical examples of using Trajectory simulator..

## Basic Usage

### Getting Help

```bash
# Show main help
trajectory --help

# Show help for a specific command
trajectory [command] --help
```

### Check Version

```bash
trajectory --version
```

## Advanced Usage

### Using with Different Log Levels

```bash
# Run with debug logging
trajectory --log-level DEBUG [command]

# Run with minimal logging
trajectory --log-level ERROR [command]
```

### Using with Configuration

```bash
# Set configuration via environment variables
export TRAJECTORY_SETTING_NAME=value
trajectory [command]

# Or create a .env file
echo "TRAJECTORY_SETTING_NAME=value" > .env
trajectory [command]
```
## Common Workflows

### Example Workflow 1

```bash
# Step 1: Initialize
trajectory init

# Step 2: Process
trajectory process --input file.txt

# Step 3: Output
trajectory output --format json
```

### Example Workflow 2

```bash
# One-liner example
trajectory process --input file.txt --output result.txt --verbose
```

## Error Handling Examples

### Common Errors

```bash
# File not found
trajectory process --input nonexistent.txt
# Error: Input file 'nonexistent.txt' not found

# Invalid option
trajectory --invalid-option
# Error: No such option: --invalid-option
```

### Debugging

```bash
# Run with debug logging to troubleshoot
trajectory --log-level DEBUG process --input file.txt
```

## Integration Examples

### Use in Scripts

```bash
#!/bin/bash
set -e

# Check if trajectory is installed
if ! command -v trajectory &> /dev/null; then
    echo "trajectory is not installed"
    exit 1
fi

# Run the command
trajectory process --input "$1" --output "$2"
echo "Processing complete"
```

### Use with Make

```makefile
.PHONY: process
process:
	trajectory process --input input.txt --output output.txt

.PHONY: clean
clean:
	rm -f output.txt trajectory.log
```

## Performance Tips

- Use appropriate log levels in production
- Process files in batches when possible
- Use configuration files for repeated settings

## Next Steps

- Learn more about the [API Reference](../reference/)
- Check out the [Contributing Guide](../contributing.md)
- Visit the [GitHub repository](https://github.com/JnyJny/trajectory)
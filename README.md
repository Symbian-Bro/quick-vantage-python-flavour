# Quick-Vantage-Python-Flavour

## About

This is a Python port of the original Quick-Vantage, a tool designed to bring the convenient hardware controls of Lenovo Vantage to Linux systems. The development of the original shell script version has been discontinued, and only this Python version is maintained for now.

The tool provides a simple command-line interface and a graphical user interface (GUI) to control features like:

  * **Conservation Mode:** Limit battery charging to 80% to prolong battery life.
  * **Function Lock:** Toggle the behavior of the function keys on your keyboard.
  * **Keyboard Backlight:** Adjust the brightness of your keyboard's backlight.

<img width="1242" height="827" alt="Nah" src="https://github.com/user-attachments/assets/16126aa5-37b2-4f46-9a98-d0708d0284df">

## Features

  * **Command-Line Interface:** A simple and intuitive CLI for quick access to all features.
  * **Graphical User Interface (In Development):** An easy-to-use GUI for those who prefer a visual approach.
  * **System Information:** View your CPU model, system temperature, and memory usage right from the CLI.
  * **Docker Support:** A Dockerfile is included for easy containerization and deployment.

## Installation

### From .deb Package

The recommended way to install Quick-Vantage is to download the latest `.deb` package from the releases and install it with your preferred package manager.

### Manual Installation

You can also run the script directly:

```bash
git clone https://github.com/symbian-bro/quick-vantage-python-flavour.git
cd quick-vantage-python-flavour
sudo python3 Quick-Vantage.py
```

For convenience, you can add an alias to your `.zshrc` or `.bash_aliases` file:

```bash
alias vantage="sudo python3 /path/to/Quick-Vantage.py"
```

## How to Use

### Command-Line Interface

To use the CLI, simply run the `vantage` command (if you set up the alias) or `sudo python3 Quick-Vantage.py`. You will be presented with a menu of options to choose from.

### Graphical User Interface

To launch the GUI, you will need to have PyQt6 installed. You can then run the `vantage.py` file in the `GUI` directory:

```bash
python3 GUI/vantage.py
```

## Contributing

We welcome contributions from everyone\! If you're new to open source, this is a great project to get started with. Here are some ways you can contribute:

  * **Reporting Bugs:** If you find a bug, please open an issue and provide as much detail as possible.
  * **Suggesting Enhancements:** Have an idea for a new feature or an improvement to an existing one? Open an issue to discuss it.
  * **Writing Code:** If you're a developer, you can help by fixing bugs, adding new features, or improving the existing codebase.
  * **Improving Documentation:** Good documentation is essential. If you see something that could be clearer or more detailed, please let us know.

To contribute code, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear and concise messages.
4.  Push your changes to your fork.
5.  Open a pull request to the main repository.

We're excited to see what you'll bring to the project\!

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for more details.

# Motor control node

The motor configuration is set in a TOML file (cf. [r_hand.toml](config/r_hand.toml)).
In this file you can set the motors ID, and angle offsets for each finger.

# Tools
- *change_id*: to help you change the id of a motor. `cargo run --bin=change_id -- -h` for a list of parameters
- *goto*: to move a single motor to a given position. `cargo run --bin=goto -- -h` for a list of parameters
- *get_zeros*: to help you set the motor zeros, it sets the motors in the compliant mode and write the TOML file to the console. `cargo run --bin=get_zeros -- -h` for a list of parameters
- *set_zeros*: to move the hand in the "zero" position according to the config file. `cargo run --bin=set_zeros -- -h` for a list of parameters

# Troubleshooting
When running Rust in VSCode / Git Bash outside of a Visual Studio development environment, upon build you may encounter the error `Error calling dlltool 'dlltool.exe': program not found`.  If this happens, see this guide for a walkthrough on setting up the GNU toolchain: https://dev.to/realacjoshua/-ditching-visual-studio-how-i-built-rust-on-windows-the-open-source-way-4m9e

When trying to run this in WSL you may encounter the following errors:
- `Failed to read config file: Os { code: 2, kind: NotFound, message: "No such file or directory" }` This message means that the `/dev/ttyACM0` cannot be found on your system. In order to resolve this error you must install [usbipd](https://github.com/dorssel/usbipd-win/releases) and map the USB device from the Windows host to your WSL2 instance:
  - Open Command Prompt and run `usbipd list`
  - Find the device with the COM port matching your device
  - Run `usbipd bind --busid 1-10 --force`
  - Run `usbipd attach --busid 1-10 --wsl`

- `Error: Error { kind: Io(PermissionDenied), description: "Permission denied" }` This error indicates that your user account within the WSL environment does not have the necessary permissions to interact with `/dev/ttyACM0`. This is a common issue when trying to use devices like Arduino boards or other USB-to-serial converters. 
  - The solution to address this is to grant full read/write permissions to the device: `sudo chmod 666 /dev/ttyACM0`
# PlatformIO Wokwi Arduino Uno

A reusable Arduino Uno starter project for PlatformIO, Wokwi and Velxio.

Use this repository as a base for Arduino Uno projects that need local development with PlatformIO and circuit simulation with Wokwi or Velxio. It works in VS Code and in Zed.

## Included

- PlatformIO configuration for Arduino Uno
- Arduino framework
- Wokwi simulation configuration
- Velxio simulation configuration
- Wokwi/Velxio circuit with just the Arduino Uno board, ready for customization
- Zed tasks and clangd setup
- `mise.toml` with pinned `pio` and `wokwi-cli`
- Standard PlatformIO project structure

## Use as a template

Click **Use this template** on GitHub, or create a new project from the terminal:

```bash
gh repo create my-project --template gm64x/platformio-wokwi-arduino-uno --public --clone
```

Looking for the ESP32 DevKit version? See [platformio-wokwi-esp32](https://github.com/gm64x/platformio-wokwi-esp32).

## Getting started

This project works best in conjunction with [Visual Studio Code](https://code.visualstudio.com/), [PlatformIO IDE](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide), and [Wokwi Simulator for VS Code](https://marketplace.visualstudio.com/items?itemName=Wokwi.wokwi-vscode).

Install the tools before opening the project:

1. [Install Visual Studio Code](https://code.visualstudio.com/download)
2. [Install PlatformIO IDE in VS Code](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide)
3. [Install Wokwi Simulator in VS Code](https://marketplace.visualstudio.com/items?itemName=Wokwi.wokwi-vscode)

Clone this repository and open it in VS Code.

### Using Zed

The project also works in [Zed](https://zed.dev/) through the [PlatformIO Core CLI](https://docs.platformio.org/en/latest/core/installation/index.html) (`pio`) and, optionally, the [Wokwi CLI](https://docs.wokwi.com/wokwi-ci/cli-installation) (`wokwi-cli`, needs a `WOKWI_CLI_TOKEN`).

1. Install PlatformIO Core and make sure `pio` is on your `PATH`, or run `mise install` to get `pio` and `wokwi-cli` from `mise.toml` with [mise](https://mise.jdx.dev/)
2. Open the folder in Zed
3. Run `task: spawn` (`alt-shift-t`) and pick a task from `.zed/tasks.json`:
   - `PlatformIO: Build`, `Upload`, `Upload and Monitor`, `Serial Monitor`, `Clean`, `Test`
   - `PlatformIO: Generate compile_commands.json (clangd)`
   - `Wokwi: Simulate` (build first)
4. Run the `compile_commands.json` task once (and again after changing `platformio.ini` or libraries) so clangd can resolve `Arduino.h` and the AVR headers. `.clangd` removes GCC-only AVR flags that clang does not understand.

### Using Velxio

[Velxio](https://velxio.dev/) is an open-source Arduino/ESP32/RP2040 simulator ([GitHub](https://github.com/davidmonterocrespo24/velxio)) that reads the same Wokwi-format `diagram.json`. `velxio.toml` points it at the PlatformIO build output, so it runs the firmware from `pio run` instead of compiling the sketch itself. Velxio has no CLI, so there is no mise tool or Zed task for it.

- Web (free): build with `pio run`, open the [Velxio editor](https://velxio.dev/editor) with the Arduino Uno board, then use `File > Upload firmware` and pick `.pio/build/uno/firmware.hex` (or `firmware.elf`). To bring the circuit along, zip `diagram.json` and load it first with `File > Import project`.
- VS Code: the [Velxio Simulator extension](https://github.com/davidmonterocrespo24/velxio/tree/master/vscode-extension) (needs a Velxio Pro subscription or its 30-day trial) picks up `velxio.toml`; build first, then run `Velxio: Run Simulation`.

Build the project with:

```bash
pio run
```

The Wokwi and Velxio configurations use the PlatformIO build output:

- Firmware: `.pio/build/uno/firmware.hex`
- ELF: `.pio/build/uno/firmware.elf`

Edit `src/main.cpp` to add your application code and `diagram.json` to add components and wiring for your simulation.

## Linux and Windows setup

Both setups use [mise](https://mise.jdx.dev/) to install the pinned `pio` and `wokwi-cli` from `mise.toml`. If you already have PlatformIO Core on your `PATH`, skip the mise steps.

### Linux

1. Install mise and enable it in your shell:

   ```bash
   curl https://mise.run | sh
   echo 'eval "$(~/.local/bin/mise activate bash)"' >> ~/.bashrc   # or ~/.zshrc with "activate zsh"
   ```

2. In the project folder, install the tools:

   ```bash
   mise trust && mise install
   ```

3. Allow uploads to the board without `sudo` (PlatformIO udev rules and serial group), then log out and back in:

   ```bash
   curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
   sudo udevadm control --reload-rules && sudo udevadm trigger
   sudo usermod -a -G dialout $USER   # on Arch-based distros the group is "uucp"
   ```

4. Optional: install Zed with `curl -f https://zed.dev/install.sh | sh`.
5. Optional, for `wokwi-cli`: `export WOKWI_CLI_TOKEN=<token>` (add it to `~/.bashrc` to keep it).

The board shows up as `/dev/ttyACM0` (original Uno) or `/dev/ttyUSB0` (CH340 clones). **WSL:** build and simulate inside WSL, but USB devices are not visible there by default. Upload from Windows, or attach the board with [usbipd-win](https://learn.microsoft.com/windows/wsl/connect-usb).

### Windows

1. Install mise from PowerShell, with `winget install jdx.mise` or `scoop install mise`.
2. Make the tools available in every terminal: add `%LOCALAPPDATA%\mise\shims` to your user `PATH`, or add `mise activate pwsh | Out-String | Invoke-Expression` to your PowerShell `$PROFILE`.
3. In the project folder, install the tools:

   ```powershell
   mise trust; mise install
   ```

4. Install the USB-to-serial driver if Windows doesn't detect the board: an original Uno uses the built-in Windows driver; most clones use a CH340 chip ([WCH CH340 driver](https://www.wch-ic.com/downloads/CH341SER_EXE.html)).
5. Optional: install [Zed for Windows](https://zed.dev/download).
6. Optional, for `wokwi-cli`: `setx WOKWI_CLI_TOKEN "<token>"`, then open a new terminal.

The board shows up as a `COM` port (for example `COM3`). Check **Device Manager > Ports (COM & LPT)** or run `pio device list`.

PlatformIO picks the upload port automatically on both systems. To force one, add `upload_port = COM3` (Windows) or `upload_port = /dev/ttyUSB0` (Linux) to the `[env]` section of `platformio.ini`.

## Project structure

```
.
├── diagram.json      # Wokwi/Velxio circuit definition
├── platformio.ini    # PlatformIO configuration
├── mise.toml         # Dev tools (pio, wokwi-cli) for mise
├── wokwi.toml        # Wokwi simulation configuration
├── velxio.toml       # Velxio simulation configuration
├── compiledb.py      # Adds toolchain headers to compile_commands.json
├── .clangd           # clangd settings for Zed
├── .zed/             # Zed tasks and project settings
├── src/
│   └── main.cpp      # Application entry point
├── include/          # Project headers
├── lib/              # Project libraries
└── test/             # PlatformIO tests
```

## License

[MIT](LICENSE)

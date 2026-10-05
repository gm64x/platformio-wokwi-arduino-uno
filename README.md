# PlatformIO Wokwi Arduino Uno

A reusable Arduino Uno starter project for PlatformIO and Wokwi.

Use this repository as a base for Arduino Uno projects that need local development with PlatformIO and circuit simulation with Wokwi.

## Included

- PlatformIO configuration for Arduino Uno
- Arduino framework
- Wokwi simulation configuration
- Velxio simulation configuration
- Wokwi/Velxio circuit with just the Arduino Uno board, ready for customization
- Standard PlatformIO project structure

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

Add a license to the repository if you plan to distribute or reuse projects based on it.

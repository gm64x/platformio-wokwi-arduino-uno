# PlatformIO Wokwi Arduino Uno

A reusable Arduino Uno starter project for PlatformIO and Wokwi.

Use this repository as a base for Arduino Uno projects that need local development with PlatformIO and circuit simulation with Wokwi.

## Included

- PlatformIO configuration for Arduino Uno
- Arduino framework
- Wokwi simulation configuration
- Empty Wokwi circuit ready for customization
- Standard PlatformIO project structure

## Getting started

Clone this repository and open it in VS Code with the PlatformIO extension installed.

Build the project with:

```bash
pio run
```

The Wokwi configuration uses the PlatformIO build output:

- Firmware: `.pio/build/uno/firmware.hex`
- ELF: `.pio/build/uno/firmware.elf`

Edit `src/main.cpp` to add your application code and `diagram.json` to add components and wiring for your simulation.

## Project structure

```
.
├── diagram.json      # Wokwi circuit definition
├── platformio.ini    # PlatformIO configuration
├── wokwi.toml        # Wokwi simulation configuration
├── src/
│   └── main.cpp      # Application entry point
├── include/          # Project headers
├── lib/              # Project libraries
└── test/             # PlatformIO tests
```

## License

Add a license to the repository if you plan to distribute or reuse projects based on it.

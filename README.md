# PlatformIO Wokwi Arduino Uno

A minimal Arduino Uno project using PlatformIO and Wokwi for development and simulation.

## Stack

- PlatformIO
- Arduino framework
- Arduino Uno
- Wokwi

## Project structure

```
.
├── diagram.json      # Wokwi circuit definition
├── platformio.ini    # PlatformIO configuration
├── wokwi.toml        # Wokwi simulation configuration
├── src/
│   └── main.cpp      # Application code
├── include/          # Project headers
├── lib/              # Project libraries
└── test/             # PlatformIO tests
```

## Getting started

Install PlatformIO, then build the project:

```bash
pio run
```

The Wokwi configuration uses the PlatformIO build output:

- Firmware: `.pio/build/uno/firmware.hex`
- ELF: `.pio/build/uno/firmware.elf`

The default `diagram.json` is intentionally empty so you can add the components and wiring for your project.

## License

Add a license to this repository if you plan to distribute or reuse the project.

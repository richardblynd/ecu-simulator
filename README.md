# ECU Simulator

A simple ECU emulator specifically designed to simulate a **BOSCH MED 17** ECU from a Volkswagen Golf 1.4 MK7.

## Overview

This project provides a virtual ECU environment that allows OBDII applications running on an Android emulator (on the same computer) to connect, perform handshake, and request sensor data. The simulator responds to OBD-II commands with pre-configured sensor values, mimicking a real ECU.

## Purpose

The main goal of this simulator is to:
- Test OBDII applications in a controlled environment without a physical vehicle
- Discover which sensor addresses are being requested by OBD applications
- Analyze how sensor values are being interpreted by different applications
- Reverse engineer and determine the formulas used to calculate sensor readings

This is particularly useful for developers working on OBD-II diagnostic applications or those trying to understand the communication protocol and data formatting used by specific ECUs.

## Network Configuration

The simulator uses a **fixed IP address of 10.0.2.2** on **port 35000**.

### Why 10.0.2.2?

This is the special IP address that Android emulators use to reach the host machine (Windows). When an Android emulator wants to communicate with services running on the Windows host, it must connect to `10.0.2.2` instead of `localhost` or `127.0.0.1`.

### OBD Application Setup

To connect your OBD-II application to this simulator:

1. **Connection Type**: Select **WIFI** connection
2. **IP Address**: Enter `10.0.2.2`
3. **Port**: Enter `35000`
4. **Protocol**: ELM327 compatible

## Supported Sensors

The simulator currently responds to the following PIDs:

- **0100**: Supported PIDs
- **2215C1**: Temperature before throttle
- **2211BD**: Oil temperature
- **22128A**: Fuel temperature
- **2215CD**: Coolant temperature (radiator outlet)
- **2211A3**: Boost pressure regulator commanded
- **2211F1**: Boost pressure commanded (hPa)

## Usage

1. Start the simulator:
   ```bash
   python src/sim.py
   ```

2. The simulator will start listening on `0.0.0.0:35000` and display:
   ```
   Golf MK7 MQB Simulator - waiting connection on 10.0.2.2:35000
   ```

3. Launch your Android emulator

4. Configure your OBD-II application with:
   - **Connection**: WIFI
   - **IP**: 10.0.2.2
   - **Port**: 35000

5. Connect from the application

6. The simulator will log all incoming requests and outgoing responses in the console, helping you understand the communication flow and data format.

## Requirements

- Python 3.x
- Android emulator (if testing mobile OBD applications)

## License

This is a simple educational/development tool for ECU simulation and OBD-II protocol analysis.
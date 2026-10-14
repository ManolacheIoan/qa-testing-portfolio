# HIL and Validation Basics (automotive)

## Test levels
- MIL (Model-in-the-Loop): the model is tested in simulation (e.g. Simulink)
- SIL (Software-in-the-Loop): the compiled software runs on a PC
- HIL (Hardware-in-the-Loop): the real ECU is connected to a simulator that imitates the vehicle (sensors, signals, CAN messages)

## Why HIL
- Test the real ECU without a real vehicle
- Safe: dangerous cases (failures, extreme values) can be simulated
- Repeatable and automatable

## Verification vs validation
- Verification: did we build the product right? (against the specification)
- Validation: did we build the right product? (against the real need)

## Typical validation flow
1. Read the requirement
2. Follow or create a validation plan
3. Run the test on the HIL bench or in the vehicle
4. Analyze results, report non-compliant steps
5. Open a ticket with logs and reproduction steps
6. Find the root cause together with the team

## CAN basics
- Messages with an ID and data bytes, sent on a shared bus
- A DBC file describes how bytes map to signals (name, scale, unit)
- Tools: CANalyzer (analysis), INCA / ControlDesk (measurement and calibration)

## Links to my portfolio
- Bug report structure: notes/ on bug report anatomy
- CAN and DBC decoding practice: python-can and cantools

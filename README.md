#Get Data From Gov

## Requirement

- python

## Use

For Max or ubuntu:

```
  python get_data.py (argument) (filename)
```
- You can use many file if you want.

For window:

- Click `get_data.bat`.
- You must add you command in `get_data.bat`.
- You can use notepad to edit `get_data.bat`.

## File example

```
{
  "RainTenMin": "http://opendata.epa.gov.tw/ws/Data/RainTenMin/?$format=json",
  "SGWC": "http://opendata.epa.gov.tw/ws/Data/SGWC/?$format=json"
}
```

## Argument

- `-t` -> add local time in file name.

## Development environment

- Mac OS X 10.11

## Issue

You can add issue [here](https://github.com/HsuTing/get_data_from_gov/issues).

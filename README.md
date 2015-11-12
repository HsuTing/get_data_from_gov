#Get Data From Gov

## Requirement

- python

## Use

For Max or ubunti:

```
  python get_data.py (argument) (filename)
```
- You can use many file if you want.

For window:

```
  commond = "python get_data.py (argument) (filename)"
```
- You must add you command in window.py

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

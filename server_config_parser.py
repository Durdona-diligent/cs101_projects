def parse_settings(config_lines):
    settings = {}
    for line in config_lines:
        try:
            splitted = line.split(":")
            if len(splitted) != 2:
                raise IndexError
            name = splitted[0]
            converted_value = int(splitted[1])
            
            if converted_value < 0 or converted_value > 100:
                raise ValueError("Out of range")
            settings[name] = converted_value
        except IndexError:
            print(f"Format error in: {line}")
        except ValueError as e:
            print(f"Invalid value in: {line} ({e})")
    return settings

configs = [
    "volume:80",          # Valid
    "brightness:120",     # Invalid Range
    "difficulty:hard",    # Invalid Type
    "mute",               # Invalid Format (no colon)
    "contrast:50"         # Valid
]
settings = parse_settings(configs)
print(f"Loaded Settings: {settings}")
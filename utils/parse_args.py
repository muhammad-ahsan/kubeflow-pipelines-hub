def parse_args_to_dict(args):
    parsed_args = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            parsed_args[key] = value
    return parsed_args

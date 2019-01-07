import yaml


def read_config_file():
    with open('configuration.yaml', 'r') as config:
        settings = yaml.load(config)
    return settings
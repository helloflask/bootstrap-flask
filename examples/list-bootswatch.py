"""List Bootstrap themes RadioField."""

from os import listdir


def list(version):
    """List template file names."""
    print(f"To add to bootstrap{version}/app.py")
    print("    theme_name = RadioField(")
    print("        default='default',")
    print("        choices=[")
    print("            ('default', 'none'),")
    base = f'../flask_bootstrap/static/bootstrap{version}/css/bootswatch'
    name = ''
    for directory in sorted(listdir(base)):
        with open(f'{base}/{directory}/_bootswatch.scss') as scss:
            for line in scss:
                name = line.strip()[3:]
                break
        print(f"            ('{directory}', '{name}'),")
    print("        ]")
    print("    )")


for value in (4, 5):
    list(value)

import os
import subprocess

def main() -> None:
    subprocess.call(
            [
                'jekyll',
                'build',
            ]
        )
    subprocess.call(
            [
                'zip',
                '-r',
                'contents.zip',
                '_site'
            ]
        )

if __name__ == '__main__':
    main()

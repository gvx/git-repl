import shlex
import subprocess
import sys

def run_git_command(intext):
    tokens = shlex.split(intext, comments=True)
    tokens.insert(0, 'git')
    return subprocess.call(tokens, stdin=sys.stdin, stdout=sys.stdout,
                           stderr=sys.stderr)

if __name__ == '__main__':
    while True:
        try:
            run_git_command(input('git '))
        except EOFError:
            break

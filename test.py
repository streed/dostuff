import asyncio
import contextlib

from dostuff.commands import *

commands = [
    Check(exists='foo'),
    File('/foo/bar'),
    Package('p1', 'p2', 'p3'),
    Package('p2', 'p3', 'p4'),
    Package('p5', action='remove'),
    Service('s1', config=File('/etc/s1.conf')),
    Service('s2', action='disable', config=File('/etc/s2/s2.conf')),
    User('bob', homedir=True, system=True),
]

stuff = asyncio.gather(*(command.do() for command in commands))

with contextlib.closing(asyncio.get_event_loop()) as loop:
    loop.run_until_complete(stuff)

# assign inputs
_solution = IN
skippedProbes = None


try:
    from butterfly_dynamo.geometry import xyzToPoint
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/dynamo/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'


if _solution:
    try:
        pts = _solution.skippedProbes()
    except AssertionError as e:
        raise ValueError('{}.\nDid you run the solution before loading the probes?'.format(e))
    except AttributeError:
        raise ValueError('{} is not a butterfly Solution.'.format(_solution))
    try:
        skippedProbes = tuple(xyzToPoint(v) for v in pts)
    except:
        skippedProbes = pts

# assign outputs to OUT
OUT = (skippedProbes,)
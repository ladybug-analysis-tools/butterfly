# assign inputs
controlDict_, probes_, additionalParams_ = IN
solutionParams = None

try:
     from butterfly.solution import SolutionParameter
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/dynamo/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

if controlDict_:
    controlDict_ = SolutionParameter.fromCppDictionary('controlDict', str(controlDict_))

if probes_:
    probes_ = SolutionParameter.fromCppDictionary('probes', str(probes_))


params = [controlDict_, probes_] + additionalParams_

solutionParams = (p for p in params if p)


# assign outputs to OUT
OUT = (solutionParams,)
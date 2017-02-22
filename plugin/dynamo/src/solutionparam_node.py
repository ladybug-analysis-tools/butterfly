# assign inputs
_filename, _values, tRange_, replace_ = IN
solutionParam = None

try:
    from butterfly.solution import SolutionParameter
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/dynamo/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

if _filename and _values:
    solutionParam = SolutionParameter.fromCppDictionary(_filename, _values,
                                                     replace_, tRange_)

# assign outputs to OUT
OUT = (solutionParam,)
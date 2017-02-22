# assign inputs
_XYZDiv_, _delta_ = IN
decomposeParDict = None

try:
    from butterfly.decomposeParDict import DecomposeParDict
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/dynamo/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

try:
    x, y, z = _XYZDiv_
except:
    x, y, z = 2, 1, 1

decomposeParDict = DecomposeParDict.simple((x, y, z), _delta_)


# assign outputs to OUT
OUT = (decomposeParDict,)
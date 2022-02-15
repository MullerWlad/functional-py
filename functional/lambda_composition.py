o_helper = lambda functions, x: functions and functions[0](o_helper(functions[1:], x)) or (lambda x: x)(x)
o = lambda functions: lambda x: o_helper(functions, x)

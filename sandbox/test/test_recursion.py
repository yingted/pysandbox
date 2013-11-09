from sandbox import Sandbox
from sandbox.test import createSandboxConfig

def test_recursion():
    def factorial(n):
        if n >= 2:
            return n * factorial(n - 1)
        else:
            return 1

    config = createSandboxConfig()
    max_frames = config.recursion_limit + 1
    try:
        Sandbox(config).call(factorial, max_frames)
    except RuntimeError as err:
        assert str(err) == 'maximum recursion depth exceeded'
    else:
        assert False

    factorial(max_frames)


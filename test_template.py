import os
from template import Sample

def test_increment():
    sample = Sample()
    assert sample.increment(1) == 2

def test_env_var():
    env_var = os.environ.get('MY_SECURE_ENV_VAR', '')
    assert env_var == 'THIS-IS-SECURE-VAR'

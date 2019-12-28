from packages.gen import hello


def test_gen_feature(runner):
    result = runner.invoke(hello)
    assert result.output == 'hello'

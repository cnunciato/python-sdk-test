from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({
    'agents': {
        'queue': 'hosted-linux'
    },
    'commands': [
        'brew install uv',
        'uv run main.py'
    ],
    'image': 'ubuntu:24.04'
})

print(pipeline.to_yaml())

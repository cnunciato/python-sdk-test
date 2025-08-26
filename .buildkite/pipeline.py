from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({
    'commands': [
        'brew install uv',
        'uv run main.py'
    ],
    'image': 'ubuntu:24.04'
})

print(pipeline.to_json())

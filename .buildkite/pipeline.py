from buildkite_sdk import Pipeline

pipeline = Pipeline()
pipeline.add_step({
    'agents': {
        'queue': 'hosted-linux'
    },
    'commands': [
        'curl -LsSf https://astral.sh/uv/install.sh | sh',
        'export PATH=$$HOME/.local/bin:$PATH',
        'uv run main.py'
    ],
    'image': 'ubuntu:24.04'
})

print(pipeline.to_yaml())

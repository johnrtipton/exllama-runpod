from huggingface_hub import snapshot_download
from config import repo_name, model_name, repo_revision

model_directory = f"/runpod-volume/{model_name}"

snapshot_download(repo_id=repo_name, local_dir=model_directory, revision=repo_revision)
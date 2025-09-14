import sys
import subprocess
import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1416587342751207584/oC1hpv9ABrWYEbc4KrxK3UN-LHnjlgliPiB3qBzPjG6i98-7kS0By9TLpLb-lZBTrdGY"

def get_last_commit():
    result = subprocess.run([
        "git", "log", "-1", "--pretty=format:%h %s by %an"],
        stdout=subprocess.PIPE,
        text=True
    )
    return result.stdout

def get_changed_files():
    result = subprocess.run([
        "git", "diff-tree", "--no-commit-id", "--name-status", "-r", "HEAD"],
        stdout=subprocess.PIPE,
        text=True
    )
    # Output format: 'A	filename', 'M	filename', 'D	filename'
    return result.stdout.strip().split('\n')


def send_discord_message(content):
    data = {"content": content}
    requests.post(WEBHOOK_URL, json=data)

if __name__ == "__main__":
    commit_info = get_last_commit()
    changed_files = get_changed_files()
    # Format: status and filename
    files_list = '\n'.join(changed_files)
    message = (
        "# Main Update\n"
        "Main Added features (A=Added, M=Modified, D=Deleted):\n"
        f"{files_list}\n"
        "Notes:\n"
        f"Commit: {commit_info}"
    )
    send_discord_message(message)

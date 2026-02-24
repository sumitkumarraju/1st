# Daily Contribution Automation

This repository includes an automated system to generate daily GitHub contributions.

## How it works

1.  **Script**: `daily_contribution.py` generates 10 commits with the message "verify files" and updates `contribution_log.txt`.
2.  **Workflow**: `.github/workflows/daily_contribution.yml` runs this script daily at 00:00 UTC.

## Setup

To ensure contributions count towards your profile:
1.  Edit `.github/workflows/daily_contribution.yml`.
2.  Update the `git config --global user.email` line with your GitHub email address.

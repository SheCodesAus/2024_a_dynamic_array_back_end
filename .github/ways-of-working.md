# Ways of Working: A Dynamic Array
## Introduction
This document outlines our team's practices and procedures for working effectively on our project. Our goal is to maintain a high standard of quality, consistency, and collaboration.
## Communication
- **Regular Meetings**: Weekly team meetings every Tuesday at 530pm and Saturday at 9am.
- **Chat Platform**: Use Slack for daily communication.
- **Issues/Discussions**: For code-related discussions, use GitHub Issues or Discussions.
## Branching Strategy - GitHub Flow
- **GitHub Flow**: This strategy is set up so that there is a main branch, which serves as our production branch - and will only be merged once everything is working as it should be in DEV, a default branch - DEV - that serves as the development branch, and individual feature branches where team members can work on adding new features without compromising the DEV or main branch. 
- **Main Branch**: The `main` branch is our production branch.
- **DEV Branch**: The `DEV` branch is our development branch.
- **Feature Branches**: Create a new branch for each feature, named `[name/issue-or-feature-you-are-working-on]`.
- **Hotfixes**: Hotfix branches, named `[hotfix/issue-name]`, are for urgent fixes.

*The basic GitHub Flow process*:
1. Create a branch 
2. Edit the branch
3. Create a pull request
4. Merge the pull request
5. Delete the branch

## Coding Practices
- **Code Style**: 
- **Documentation**: Comment your code and update the README as needed.
- **Testing**: 
## Pull Requests and Code Reviews
- **Pull Requests (PRs)**: All changes must be made through PRs. Describe your changes clearly, use the template. 
- **Review Process**: Each PR requires at least 2 reviews.
- **Merge Criteria**: Reviews must be conducted by someone other than the developer who intitated the PR. No pending conversations. No pending change requests. 
- **Stale PRs**: If you’ve created a PR, gotten a review, then made a change to the PR (by making a commit to that PR, for example), the existing review will be dismissed and you will be required to make a new PR.
## Issue Tracking
- **Creating Issues**: Clearly describe the issue or feature request with a meaningful title and detailed description. Use the template. 
- **Assigning Issues**: Assign yourself to an issue you're working on and label it appropriately.
- **Updating Progress**: Regularly update the issue to reflect the current status.
## Security Practices
- **Sensitive Data**: Never commit sensitive data to the repository.
## Continuous Improvement
- **Feedback on Practices**: Regularly discuss and update our ways of working to reflect best practices and team needs.
# Evidence-first bug fixing

Given a bug report in a repository:

- Inspect the relevant implementation, tests, repository guidance, and current worktree before editing.
- Before editing, attempt the smallest available reproduction when the report and repository make one runnable. If reproduction is unavailable, state why and do not claim it succeeded.
- Ask only when a missing product decision would materially change user-visible behavior, a public interface, permission, an external side effect, or the requested target. Otherwise use reasonable reversible implementation defaults and continue.
- Make the smallest scoped fix that preserves unrelated user changes.
- Run focused verification and any broader relevant checks proportionate to the change. If a check cannot run, report the exact limitation.
- Distinguish failures caused by the change from failures that were already present.
- Report the diagnosis, changed files, reproduction evidence, verification results, and unresolved risks. Include a distinct changed-files list; do not rely on the diagnosis or fix narrative to imply which files changed.

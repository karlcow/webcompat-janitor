# webcompat-janitor
Check the status of [webcompat](https://webcompat.com) labels every week.

With a JSON dump of all webcompat issues, the code will check if some labels are missing or being in conflict.

This code was to address some [recurring issues](https://github.com/webcompat/webcompat.com/issues/1251) we had with mislabeling issues on [webcompat.com](https://webcompat.com) project.

## Business Rules

* [x] ERROR: Closed issues must have a label in [`status-fixed`, `status-duplicate`, `status-incomplete`, `status-wontfix`, `status-worksforme`, `status-invalid`].
* [x] ERROR: Closed and open issues have one and only one `status-*` label.
* [ ] WARNING: issues without a `browser-*` label.
* [ ] WARNING: issues without a `type-*` label.


## Example:

Example of output

```
15:25:32: Issue 1
15:25:32: Issue 1 has no status label
15:25:34: Issue 1099
15:25:34: Too many labels for 1099: [u'status-contactready', u'status-needscontact']
15:25:34: Issue 1100
15:25:34: Wrong label for 1100: closed <> [u'status-needsdiagnosis']
15:25:35: Issue 1101
15:25:35: Wrong label for 1101: open <> [u'status-fixed']
```
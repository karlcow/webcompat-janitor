# webcompat-janitor
Check the status of [webcompat](https://webcompat.com) labels every week.

With a JSON dump of all webcompat issues, the code will check if some labels are missing or being in conflict.

This code was to address some [recurring issues](https://github.com/webcompat/webcompat.com/issues/1251) we had with mislabeling issues on [webcompat.com](https://webcompat.com) project.

## Business Rules

* ERROR: Closed issues must have a label in [`status-fixed`, `status-duplicate`, `status-incomplete`, `status-wontfix`, `status-worksforme`, `status-invalid`].
* ERROR: Closed and open issues have one and only one `status-*` label.
* WARNING: issues without a `browser-*` label.
* WARNING: issues without a `type-*` label.

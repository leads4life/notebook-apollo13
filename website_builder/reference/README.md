# Retrofit references

R3 does not require one universal design template.

For RETROFIT mode, supply an approved local HTML baseline in the build spec:

```json
{
  "mode": "retrofit",
  "retrofit_baseline": "/path/to/approved-reference.html"
}
```

The complete packaged R3 release retains the Atlantic Meridian R2 baseline as the compatibility reference. Repositories may omit that large benchmark file and supply any approved reference explicitly.

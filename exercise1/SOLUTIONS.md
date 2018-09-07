This bug causes the function to pass the incorrect string in the recursive case.

Fix:
Change the line
```
return palindrome(s[0:-1])
```
to
```
return palindrome(s[1:-1])
```
.
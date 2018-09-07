This will run forever.

Change the lines:
```
l = fusion_sort(left[0:len(left)/2-1:1], left[len(left)/2-1::1])
```
and
```
r = fusion_sort(right[0:len(right)/2-1:1], right[len(right)/2-1::1])
```
to 
```
l = fusion_sort(left[0:len(left)/2:1], left[len(left)/2::1])
```
and
```
r = fusion_sort(right[0:len(right)/2:1], right[len(right)/2::1])
```
.
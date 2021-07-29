def merge(data,start,mid,end):
     temparr = data
     i,j,k = start,mid+1,0


def mergeSort(data,start,end):
     if start < end:
          mid = (start + end) // 2
          mergeSort(data,start,mid)
          mergeSort(data,mid+1,end)
          merge(data,start,mid,end)

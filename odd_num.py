start,end= 1,10
print(f"odd numbers from {start} to {end} are:")
for num in range(start,end+1):
    if num%2!=0:

        print(num,end="\n")
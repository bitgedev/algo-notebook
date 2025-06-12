music=list(map(int,input().split()))
c=music.index(1)
if sorted(music[:c])==music[:c] and sorted(music[c:])==music[c:]:
    print("ascending")
elif sorted(music[:c], reverse=True)==music[:c] and sorted(music[c:], reverse=True)==music[c:]:
    print("descending")
else:
    print("mixed")
def character_count(string):
    all_chars = {}
    count = 0
    for i in range(0,len(string)):
        if ( len(all_chars[string[i]]) == 0):
            all_chars[string[i]][0]=1
        else:
            all_chars[string[i]][0] = all_chars[string[i]] + 1
        count= count + 1

    print(count , all_chars)


character_count("aaabbcccccd")


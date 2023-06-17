def timeConversion(s):
    time_ = s.split(":")
    print(time_)

    if "P" in s:
        if time_[0] != "12":
            hour = int(time_[0])+12
        else:
            hour = 12
    else:
        if time_[0] == "12":
            hour = "00"
        else:
            hour = time_[0]

    return f"{hour}:{time_[1]}:{time_[-1][:2]}"


def read_file():
    with open("validity_reason.csv","r") as f:
        file_list = list()
        while True:
            line = f.readline()
            if not line:
                break
            line = line.replace("{","")
            line = line.replace("}","")
            line = line.replace("\n","")
            split_line = line.split(",")
            file_list.append(split_line)
        return file_list


def count():
    ip_list = read_file()
    count = dict()
    reason_set = ()
    for ip in ip_list:
        reason = ip[2].split(":")[1]
        if count.get(reason) != None:
            count[reason] += 1
        else:
            count.update({reason:0})
    return count

def main():
    reasons = count()
    for key in reasons.keys():
        print(key,": ",reasons[key])

if __name__ == '__main__':
    main()
